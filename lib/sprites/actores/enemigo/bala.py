# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from math import *

ESTADO_ESPERA = 0
ESTADO_DISPARO = 1
ESTADO_AVANCE = 2

class Bala(Enemigos):


    def __init__(self, archivoImagen, archivoCoordenadas,tipoBala, posicionDisparo):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self,archivoImagen, archivoCoordenadas, [2,0,0], 20, 10);
        self.visible = True
        self.numImagenPostura = tipoBala
        self.posicionDisparo = posicionDisparo
        self.establecerPosicion(self.posicionDisparo)
        self.estado = ESTADO_ESPERA

        self.distanciaMax = 300

    def mover_cpu(self,jugador):

        if self.estado == ESTADO_ESPERA:
            #No se mueve
            Enemigos.mover_cpu(self,0,0)
        elif self.estado == ESTADO_DISPARO:
            #Actualiza su direccion a la del jugador en ese frame
            (centroJX,centroJY) = jugador.rect.center
            (centroGX,centroGY) = self.rect.center
            radian = math.atan2(centroGX - centroJX, centroGY - centroJY)
            self.angulo = degrees(radian)
            Enemigos.mover_cpu(self,self.angulo,0)
        elif self.estado == ESTADO_AVANCE:
            # No actualizamos el movimiento
            Enemigos.mover_cpu(self,self.angulo,1)

    def update(self, tiempo, grupoJugadores):

        Actor.update(self,tiempo)

        if self.estado == ESTADO_ESPERA:
            # La bala es invisible, y se queda en la posicion inicial
            self.establecerPosicion(self.posicionDisparo)
            self.visible = False

        elif self.estado == ESTADO_DISPARO:
            # La bala es visible, se queda en la posicion inicial e inicia el estado de avance
            self.establecerPosicion(self.posicionDisparo)
            self.visible = True
            if self.numImagenPostura == 0:
                sound = GestorRecursos.CargarSonido("others/maullido.mp3")
            else:
                sound = GestorRecursos.CargarSonido("others/baby.mp3")
            sound.play()
            self.estado = ESTADO_AVANCE

        elif self.estado == ESTADO_AVANCE:
            # La bala avanza hacia adelante
            (velocidadX,velocidadY) = self.velocidad

            if self.movimientoLineal == ADELANTE:
                velocidadX = -self.adelante[0] * self.velocidadCarrera
                velocidadY = -self.adelante[1] * self.velocidadCarrera
                self.velocidad = (velocidadX, velocidadY)
            else:
                self.velocidad = (0,0)

            jugadores = pygame.sprite.spritecollide(self, grupoJugadores, False, pygame.sprite.collide_circle_ratio(0.6))
            if jugadores != None:
                for jugador in jugadores:
                        sound = GestorRecursos.CargarSonido("others/impacto.mp3")
                        jugador.perderVida(sound)
                        self.estado = ESTADO_ESPERA
                        break
                

            (posX,posY) = self.rect.center
            (origX,origY) = self.posicionDisparo
            distancia = sqrt(pow((posX-origX),2) + pow((posY-origY),2))
            if  distancia > self.distanciaMax:
                self.estado = ESTADO_ESPERA
            
    def draw(self,pantalla):
        if self.visible:
            pantalla.blit(self.image,self.rect)

    
    def disparar(self, objetivo):
        self.estado = ESTADO_DISPARO
        self.objetivo = objetivo

    def estaEspera(self):
        return self.estado == ESTADO_ESPERA


class Vomito(Bala):

    def __init__(self,posicionDisparo):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Bala.__init__(self, 'personajes/enemigos/bala/proyectiles.png','personajes/enemigos/bala/coordBala.txt',1, posicionDisparo);


class Pelo(Bala):

    def __init__(self,posicionDisparo):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Bala.__init__(self, 'personajes/enemigos/bala/proyectiles.png','personajes/enemigos/bala/coordBala.txt',0, posicionDisparo);