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

    def mover_cpu(self, image, angle):
        self.angulo = angle
        (adelanteY, adelanteX) = self.adelante
        adelanteX = math.cos(math.radians(self.angulo))
        adelanteY = math.sin(math.radians(self.angulo))
        self.adelante = (adelanteY, adelanteX)

    def disparar(self, x,y, estado):
        if estado:
            self.adelante

    def update(self, tiempo):
        Actor.update(self, tiempo)

        return
