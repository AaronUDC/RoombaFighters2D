# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from math import *


class Bala(Enemigos):

    def __init__(self, archivoImagen, archivoCoordenadas):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self,archivoImagen, archivoCoordenadas, [3,3,3], 20, 10);
        self.activo = True
        self.tipoBala = 0
        self.mascara = pygame.mask.from_surface(self.image)

    def mover_cpu(self,jugador):
        (centroJX, centroJY) = jugador.rect.center
        (centroGX, centroGY) = self.centroT
        (centroBX, centroBY) = self.rect.center
        if (self.posicion[0] == centroGX and self.posicion[1] == centroGY):
            radian = math.atan2(centroBX - centroJX, centroBY - centroJY)
            self.angulo = degrees(radian)
            adelanteX = math.cos(math.radians(self.angulo))
            adelanteY = math.sin(math.radians(self.angulo))
            self.adelante = (adelanteY, adelanteX)
        if ((jugador.posicion[0] - self.posicion[0]) < 250 and (jugador.posicion[0] - self.posicion[0]) > -250) and (
                (jugador.posicion[1] - self.posicion[1]) < 200 and (jugador.posicion[1] - self.posicion[1]) > -200):
            self.movimientoLineal = 1
        else:
            self.movimientoLineal = 0

        if self.movimientoLineal:
            if self.posicion[1] < centroGY - 150 or self.posicion[1] > centroGY + 150:
                self.posicion = (centroGX, centroGY)
                self.movimientoLineal = 0
                self.activo = True
            if self.posicion[0] < centroGX - 200 or self.posicion[0] > centroGX + 200:
                self.posicion = (centroGX, centroGY)
                self.movimientoLineal = 0
                self.activo = True
        else:
            self.activo = True
            self.posicion = (centroGX, centroGY)
            # self.angulo = ((100 * self.velGiro) / 1 + angle)

    def actualizarPostura(self):
        self.numImagenPostura = self.tipoBala

    def update(self, tiempo, mascaraEstaticos, grupoJugadores,tipo):
        if (tipo == 1):
            self.tipoBala= 1
            self.actualizarPostura()
        else:
            self.tipoBala = 0
            self.actualizarPostura()
        if self.activo == True:
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
                    if self.activo == True:
                        self.activo = False
                        jugador.perderVida()
            Actor.update(self,tiempo)
        
    def draw(self,pantalla):
        if self.activo == True:
            pantalla.blit(self.image,self.rect)