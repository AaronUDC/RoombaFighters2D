# -*- coding: utf-8 -*-

import pygame, sys, os, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.enemigos import *
from lib.escena import ALTO_PANTALLA,ANCHO_PANTALLA
from math import *

class EnemigoSeguidor(Enemigos):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadCarrera, velGiro, objetivo):
        Enemigos.__init__(self, archivoImagen ,archivoCoordenadas, numImagenes, velocidadCarrera, velGiro)
        self.objetivo = objetivo


    def mover_cpu(self):
        (centroJX,centroJY) = self.objetivo.rect.center
        (centroGX,centroGY) = self.rect.center
        radian = math.atan2(centroGX - centroJX, centroGY - centroJY)
        angulo = degrees(radian)
        Enemigos.mover_cpu(self, angulo,1)
    
    def update(self, tiempo):

        if self.movimientoLineal == ADELANTE: 
            # Mover hacia adelante
            velocidadX = -self.adelante[0] * self.velocidadCarrera
            velocidadY = -self.adelante[1] * self.velocidadCarrera
         
        self.velocidad = (velocidadX, velocidadY)    
        Enemigos.update(self, tiempo,0)

class Fantasma(EnemigoSeguidor):

    def __init__(self, objetivo):
        EnemigoSeguidor.__init__(self, 'personajes/enemigos/fantasma/Fantasma.png' ,'personajes/enemigos/fantasma/coordFantasma.txt', [1,0,0], 15, 5, objetivo)

    
    def update(self,tiempo,grupoJugadores):
        EnemigoSeguidor.update(self,tiempo)

        #Comprobar si colisiona con el jugador

        jugadores = pygame.sprite.spritecollide(self, grupoJugadores, False, pygame.sprite.collide_circle_ratio(0.3))

        if jugadores != None:
            for jugador in jugadores:
                jugador.perderVida()

                #Lado de la pantalla al que se teletransportara
                cuadrante = random.randint(0,3)
                #Segun el cuadrante, lo colocamos en un lugar aleatorio en el borde correspondiente
                if cuadrante == 0:
                    #Arriba
                    (newPosX, newPosY) = (random.randint(-80,ANCHO_PANTALLA+80), -80)
                elif cuadrante == 1:
                    #Derecha
                    (newPosX, newPosY) = (ANCHO_PANTALLA+80,random.randint(-80,ALTO_PANTALLA+80))
                elif cuadrante == 2:
                    #Abajo
                    (newPosX, newPosY) = (random.randint(-80,ANCHO_PANTALLA+80),ALTO_PANTALLA+80)
                elif cuadrante == 3:
                    #Izquierda
                    (newPosX, newPosY) = (-80,random.randint(-80,ALTO_PANTALLA+80))


                self.establecerPosicion((newPosX, newPosY))

        EnemigoSeguidor.update(self,tiempo)






        

