# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from math import *


class Bala(Enemigos):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self,'personajes/enemigos/bala/bala.png','personajes/enemigos/bala/coordBala.txt', [3,3,3], 20, 10);
        self.activo = True
        self.mascara = pygame.mask.from_surface(self.image)

    def mover_cpu(self,jugador):
        (centroJX, centroJY) = jugador.rect.center
        (centroGX, centroGY) = (360, 310)
        (centroBX, centroBY) = self.rect.center
        if (self.posicion[0] == centroGX and self.posicion[1] == centroGY):
            radian = math.atan2(centroBX - centroJX, centroBY - centroJY)
            self.angulo = degrees(radian)
            adelanteX = math.cos(math.radians(self.angulo))
            adelanteY = math.sin(math.radians(self.angulo))
            self.adelante = (adelanteY, adelanteX)
        if ((jugador.posicion[0] - self.posicion[0]) < 200 and (jugador.posicion[0] - self.posicion[0]) > -200) and (
                (jugador.posicion[1] - self.posicion[1]) < 200 and (jugador.posicion[1] - self.posicion[1]) > -200):
            self.movimientoLineal = 1
        else:
            self.movimientoLineal = 0

        if self.movimientoLineal:
            if self.posicion[1] < 200:
                self.posicion = (centroGX, centroGY)
        else:
            self.activo = True
            self.posicion = (centroGX, centroGY)
            # self.angulo = ((100 * self.velGiro) / 1 + angle)

    def update(self, tiempo, mascaraEstaticos):

        (velocidadX,velocidadY) = self.velocidad

        if self.movimientoLineal == ADELANTE:
            velocidadX = -self.adelante[0] * self.velocidadCarrera
            velocidadY = -self.adelante[1] * self.velocidadCarrera
            self.velocidad = (velocidadX, velocidadY)
        else:
            self.velocidad = (0,0)
        Actor.update(self,tiempo)
        
        return