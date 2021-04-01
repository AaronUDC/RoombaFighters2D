# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import GestorRecursos
from lib.sprites.actores.actores import *
from math import *

class Jugador(Actor):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self,'personajes/roomba/roomba.png','personajes/roomba/coordRoomba.txt', [3,3,3], 50, 50)

        self.puntuacion = 0
        self.modificadorVel = 1
        self.modificadorGiro = 1
        self.powerupActual = 0
        self.vida = 3
        self.maxVida = 3
        self.escudo = 0
        self.mascara = pygame.mask.from_surface(self.image)

        self.actualizarPostura()

    def actualizarPostura(self):
        if self.escudo == 0:
            self.numImagenPostura = self.maxVida - (self.vida)
        else:
            self.numImagenPostura = self.maxVida - (self.escudo)
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

        '''
        colisionesBasura = pygame.sprite.spritecollide(self, lBasuras, False, pygame.sprite.collide_circle_ratio(0.3))
        if colisionesBasura != None:
            for basura in colisionesBasura:
                if basura.activo == True:
                    basura.activo = False
                    self.puntuacion += basura.puntuacion
                    #print(self.puntuacion)

        thunderColision = pygame.sprite.spritecollide(self, thunder, False, pygame.sprite.collide_circle_ratio(0.6))
        if thunderColision != None:
            for thunder in thunderColision:
                if thunder.activo == True:
                    thunder.activo = False
                    thunder.cantidad = 0
                    #self.music = GestorRecursos.CargarMusica("powerups/thunderMusic.wav")
                    #thunder.thunderSoundEffect()
                    #thunder.thunderMusic(True)
                    self.powerupActual = 1
                    self.modificadorVel = 2
                    self.actualizarPostura()

        wrenchColision = pygame.sprite.spritecollide(self, wrench, False, pygame.sprite.collide_circle_ratio(0.6))
        if wrenchColision != None:
            for wrench in wrenchColision:
                if wrench.activo == True:
                    wrench.activo = False
                    wrench.cantidad = 0
                    #wrench.wrenchSoundEffect()
                    if self.escudo > 0:
                        if self.escudo < self.maxVida:
                            self.escudo += 1
                    else:
                        if self.vida < self.maxVida:
                            self.vida += 1
                    self.actualizarPostura()
        
        shieldColision = pygame.sprite.spritecollide(self, shield, False, pygame.sprite.collide_circle_ratio(0.6))
        if shieldColision != None:
            for shield in shieldColision:
                if shield.activo == True:
                    shield.activo = False
                    shield.cantidad = 0
                    #shield.shieldMusic(True)
                    self.powerupActual = 2
                    self.escudo = 3
                    self.actualizarPostura()'''


    ##Metodos para que otras entidades actuen sobre el jugador
    def perderVida(self):
        self.vida -= 1
        if (self.vida >= 1):
            self.actualizarPostura()
    
    def curarVida(self):
        if self.vida < self.maxVida:
            self.vida += 1
            self.actualizarPostura()

    def obtenerPowerUp(self, powerup, tiempo):
        self.tiempoPowerUp = tiempo
        self.powerupActual = powerup

    def ganarPuntos(self, puntos):
        self.puntuacion += puntos