# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from math import *

class Jugador(Actor):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self,'roomba/roomba.png',None, [6, 12, 6], 50, 20);
        self.

        

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

    def update(self, tiempo, grupoElementosEstaticos):
       

        (velocidadX,velocidadY) = self.velocidad

        if self.movimientoLineal == ADELANTE: 
            # Mover hacia adelante
            velocidadX = -self.adelante[0] * self.velocidadCarrera
            velocidadY = -self.adelante[1] * self.velocidadCarrera

        elif self.movimientoLineal == ATRAS:
            # Mover hacia atras
            velocidadX = self.adelante[0] * self.velocidadCarrera
            velocidadY = self.adelante[1] * self.velocidadCarrera
        elif self.movimientoLineal == QUIETO:
            velocidadX = 0
            velocidadY = 0


        if self.movimientoAngular == IZQUIERDA:
            #Girar a la Izquierda
            self.girar(tiempo,1)
        elif self.movimientoAngular == DERECHA:
            #Girar a la Derecha
            self.girar(tiempo,-1)
        
        self.velocidad = (velocidadX, velocidadY)


        (posAntX ,posAntY ) = self.posicion
        
        Actor.update(self,tiempo)

        (posActX, posActY) = self.posicion

        obstaculos = pygame.sprite.spritecollide(self,grupoElementosEstaticos,False)
        #Colisiones WIP
        if(obstaculos != None):
            for obstaculo in obstaculos:
                if obstaculo.rect.left  < self.rect.right and obstaculo.rect.right < self.rect.right:
                #if obstaculo.rect.left < self.rect.right:
                    #Colision por la izquierda
                    #print("obstL:", obstaculo.rect.right, " ", obstaculo.rect.right + self.image.get_width()," " ,  self.rect.right)
                    posActX = posAntX

                elif obstaculo.rect.left > self.rect.left and obstaculo.rect.right > self.rect.left:
                #elif obstaculo.rect.left > self.rect.left:
                    #Colision por la derecha
                    posActX = posAntX

                if obstaculo.rect.top < self.rect.bottom and obstaculo.rect.bottom  < self.rect.bottom:
                #if obstaculo.rect.top < self.rect.bottom:
                    #Colision por arriba
                    posActY = posAntY

                elif obstaculo.rect.top > self.rect.top and obstaculo.rect.bottom > self.rect.top:
                #elif obstaculo.rect.top > self.rect.top:
                    #Colision por abajo

                    posActY = posAntY
                

                
        MiSprite.establecerPosicion(self, (posActX,posActY))