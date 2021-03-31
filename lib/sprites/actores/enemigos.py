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


    def mover_cpu(self, movimientoAngular,movimientoLineal):
        
        self.angulo = movimientoAngular%360
        adelanteX = math.cos(math.radians(self.angulo))
        adelanteY = math.sin(math.radians(self.angulo))
        self.adelante = (adelanteY, adelanteX)
        
        self.movimientoLineal = movimientoLineal

    def update(self, tiempo):
        Actor.update(self, tiempo)

        return
