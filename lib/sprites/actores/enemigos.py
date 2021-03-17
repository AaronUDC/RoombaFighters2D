# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from math import *


class Enemigos(Actor):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadCarrera, velGiro):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self, archivoImagen ,archivoCoordenadas, numImagenes, velocidadCarrera, velGiro);

    def mover_cpu(self, jugador,angle):
        self.angulo = ((1 * self.velGiro) / 200 * angle)
        """"(adelanteY, adelanteX) = self.adelante
        adelanteX = math.cos(math.radians(self.angulo))
        adelanteY = math.sin(math.radians(self.angulo))
        self.adelante = (adelanteY, adelanteX)"""

    def disparar(self, x,y, estado,angle):
        if estado:
            (velocidadX,velocidadY) = self.velocidad
            velocidadX = -self.adelante[0] * self.velocidadCarrera
            velocidadY = -self.adelante[1] * self.velocidadCarrera
            self.velocidad = (velocidadX, velocidadY)
            if self.posicion[1] < 350:
               (posAntX, posAntY) = self.posicion
        #else:
            #self.angulo = ((100 * self.velGiro) / 1 + angle)




    def update(self, tiempo):
        Actor.update(self, tiempo)

        return
