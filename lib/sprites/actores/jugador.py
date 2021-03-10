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
        obstaculo = pygame.sprite.spritecollideany(self,grupoElementosEstaticos)

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


        #Colisiones WIP
        if(obstaculo != None):
            newPosX = self.posicion[0]-(velocidadX)
            newPosY = self.posicion[1]-(velocidadY)
            
            MiSprite.establecerPosicion(self, (newPosX,newPosY) )

        if self.movimientoAngular == IZQUIERDA:
            #Girar a la Izquierda
            self.girar(tiempo,1)
        elif self.movimientoAngular == DERECHA:
            #Girar a la Derecha
            self.girar(tiempo,-1)
        
        self.velocidad = (velocidadX, velocidadY)

        Actor.update(self,tiempo)