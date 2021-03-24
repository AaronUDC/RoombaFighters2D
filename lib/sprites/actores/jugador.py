# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from math import *

class Jugador(Actor):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self,'personajes/roomba/roomba.png',None, [6, 12, 6], 50, 50)
        self.mascara = pygame.mask.from_surface(self.image)
        self.puntuacion = 0
        self.modificadorVel = 1
        self.modificadorGiro = 1

        

    def mover(self, teclasPulsadas, arriba, abajo, izquierda, derecha):
        # Indicamos la acción a realizar segun la tecla pulsada para el jugador
        lineal = QUIETO
        angular = QUIETO
        if teclasPulsadas[arriba]:
            lineal = ADELANTE
        elif teclasPulsadas[abajo]:
            lineal = ATRAS
        else:
            lineal = QUIETO
        if teclasPulsadas[izquierda]:
            angular = IZQUIERDA
        elif teclasPulsadas[derecha]:
            angular = DERECHA
        else:  
            angular = QUIETO
        Actor.mover(self,lineal,angular)

    def update(self, tiempo, mascaraEstaticos, lBasuras, thunder):
       

        (velocidadX,velocidadY) = self.velocidad

        if self.movimientoLineal == ADELANTE: 
            # Mover hacia adelante
            velocidadX = -self.adelante[0] * self.velocidadCarrera * self.modificadorVel
            velocidadY = -self.adelante[1] * self.velocidadCarrera * self.modificadorVel

        elif self.movimientoLineal == ATRAS:
            # Mover hacia atras
            velocidadX = self.adelante[0] * self.velocidadCarrera * self.modificadorVel
            velocidadY = self.adelante[1] * self.velocidadCarrera * self.modificadorVel
        elif self.movimientoLineal == QUIETO:
            velocidadX = 0
            velocidadY = 0


        if self.movimientoAngular == IZQUIERDA:
            #Girar a la Izquierda
            self.girar(tiempo,self.modificadorGiro)
        elif self.movimientoAngular == DERECHA:
            #Girar a la Derecha
            self.girar(tiempo,-self.modificadorGiro)
        
        self.velocidad = (velocidadX, velocidadY)


        (posAntX ,posAntY ) = self.posicion
        
        Actor.update(self,tiempo)

        (posActX, posActY) = self.posicion

        posMaskX = int(posActX)
        posMaskY = int(posActY)-self.image.get_height()
    
        dx = mascaraEstaticos.overlap_area(self.mascara, (posMaskX+1,posMaskY)) - mascaraEstaticos.overlap_area(self.mascara, (posMaskX-1, posMaskY))
        dy = mascaraEstaticos.overlap_area(self.mascara, (posMaskX,posMaskY+1)) - mascaraEstaticos.overlap_area(self.mascara, (posMaskX, posMaskY-1))
        if mascaraEstaticos.overlap_area(self.mascara, (int(posActX) ,int(posActY)-self.image.get_height() ) ) > 0:
            posActX = posActX -((2*dx)/self.velocidadCarrera)* self.modificadorVel
            posActY = posActY -((2*dy)/self.velocidadCarrera)* self.modificadorVel
        
                
        MiSprite.establecerPosicion(self, (posActX,posActY))


        colisionesBasura = pygame.sprite.spritecollide(self, lBasuras, False, pygame.sprite.collide_circle_ratio(0.3))
        if colisionesBasura != None:
            for basura in colisionesBasura:
                if basura.activo == True:
                    basura.activo = False
                    self.puntuacion += basura.puntuacion
                    print(self.puntuacion)
        
        thunderColision = pygame.sprite.spritecollide(self, thunder, False, pygame.sprite.collide_circle_ratio(0.3))
        if thunderColision != None:
            for thunder in thunderColision:
                if thunder.activo == True:
                    thunder.activo = False