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
        elif self.movimientoLineal == QUIETO:
            velocidadX = 0
            velocidadY = 0

        self.velocidad = (velocidadX, velocidadY)    
        Enemigos.update(self, tiempo)

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

SEGUIR_JUGADOR = 0
MOVERSE_JAULA = 1
ESPERAR_JAULA = 2

class Loro(EnemigoSeguidor):

   

    def __init__(self, objetivo, posicionJaula, tiempoEspera, velocidadPerseguir, velocidadVolver):
        
        
        self.velocidadPerseguir = velocidadPerseguir
        self.velocidadVolver = velocidadVolver
        
        EnemigoSeguidor.__init__(self, 'personajes/enemigos/loro/Loro.png' ,'personajes/enemigos/loro/coordLoro.txt', [1,0,0], self.velocidadPerseguir, 5, objetivo)
        self.posicionJaula = posicionJaula
        self.tiempoEspera = tiempoEspera
        self.esperaActual = 0
        self.visible = False


        self.estado = ESPERAR_JAULA

    def mover_cpu(self):

        if self.estado == ESPERAR_JAULA:
            ## No hacer nada
            Enemigos.mover_cpu(self, 0,0)
        elif  self.estado == SEGUIR_JUGADOR:
            ## Seguir al jugador (Comportamiento base de enemigo seguidor)
            EnemigoSeguidor.mover_cpu(self) 
        elif  self.estado == MOVERSE_JAULA:
            ## Volver a la jaula
            (centroJX,centroJY) = self.posicionJaula
            centroJX += self.rect.width/2
            centroJY -= self.rect.height/2
            (centroLX,centroLY) = self.rect.center
            radian = math.atan2(centroLX - centroJX, centroLY - centroJY)
            angulo = degrees(radian)
            Enemigos.mover_cpu(self, angulo,1)


    def update(self,tiempo,grupoJugadores):

        if  self.estado == ESPERAR_JAULA:
            ## Estado de esperar en la jaula.
            # vamos a mantener un temporizador para que espere 
            # sin moverse, hasta que toque cambiar de estado
            if self.esperaActual < self.tiempoEspera:
                
                self.esperaActual += (tiempo/1000)
                self.establecerPosicion(self.posicionJaula)
                EnemigoSeguidor.update(self,tiempo)
            else:
                self.estado = SEGUIR_JUGADOR
                self.esperaActual = 0
                self.visible = True
                self.velocidadCarrera = self.velocidadPerseguir

        elif self.estado == SEGUIR_JUGADOR:
            EnemigoSeguidor.update(self,tiempo)

            jugadores = pygame.sprite.spritecollide(self, grupoJugadores, False, pygame.sprite.collide_circle_ratio(0.3))
            if jugadores != None:
                for jugador in jugadores:
                    jugador.perderVida()
                    
                    #Cambiar al estado de volver a la jaula
                    self.estado = MOVERSE_JAULA
                    self.velocidadCarrera = self.velocidadVolver
        
        elif self.estado == MOVERSE_JAULA:
            EnemigoSeguidor.update(self,tiempo)
            (centroJX,centroJY) = self.posicionJaula
            centroJX += self.rect.width/2
            centroJY -= self.rect.height/2 - self.rect.height/4

            if self.rect.collidepoint((centroJX,centroJY)):
                self.establecerPosicion(self.posicionJaula)
                self.visible = False
                self.estado = ESPERAR_JAULA
        
    def dibujar(self,pantalla):
        if self.visible:
            pantalla.blit(self.image,self.rect)

                    

            

        

