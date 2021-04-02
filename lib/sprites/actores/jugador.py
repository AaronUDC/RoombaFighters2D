# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import GestorRecursos
from lib.sprites.actores.actores import *
from math import *


NO_POWERUP = 0
SPEED_UP = 1
SHIELD_UP = 2

class Jugador(Actor):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self,'personajes/roomba/roomba.png','personajes/roomba/coordRoomba.txt', [3,3,3], 50, 50)

        self.puntuacion = 0
        self.vida = 3
        self.maxVida = 3
        self.mascara = pygame.mask.from_surface(self.image)

        self.powerupActual = 0
        self.tiempoPowerUp = 0
        
        self.modificadorVel = 1
        self.modificadorGiro = 1
        self.escudo = False

        self.actualizarPostura()

    def actualizarPostura(self):
        self.numImagenPostura = self.maxVida - (self.vida)
        self.numPostura = self.powerupActual

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

    def update(self, tiempo, mascaraEstaticos, lBasuras, thunder, wrench, shield):
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

        (posAntX ,posAntY) = self.posicion

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

        #Contador del powerUp
        if self.powerupActual != NO_POWERUP:
            self.tiempoPowerUp -= tiempo/1000
            if self.tiempoPowerUp < 0:
                self._resetPowerUp()
                
    def _resetPowerUp(self):
        self.modificadorVel = 1
        self.modificadorGiro = 1
        self.escudo = False
        self.tiempoPowerUp = -1
        self.powerupActual = NO_POWERUP
        self.actualizarPostura()

    ##Metodos para que otras entidades actuen sobre el jugador
    def perderVida(self):
        if not self.escudo:
            self.vida -= 1
            if (self.vida >= 1):
                self.actualizarPostura()
        else:
            self._resetPowerUp()
    
    def curarVida(self):
        if self.vida < self.maxVida:
            self.vida += 1
            self.actualizarPostura()

    def obtenerPowerUp(self, powerup, tiempo):
        self._resetPowerUp()
        self.tiempoPowerUp = tiempo
        self.powerupActual = powerup
        if powerup == SPEED_UP:
            self.modificadorVel = 1.75
            self.modificadorGiro = 2
        elif powerup == SHIELD_UP:
            self.escudo = True
        self.actualizarPostura()

    def ganarPuntos(self, puntos):
        self.puntuacion += puntos