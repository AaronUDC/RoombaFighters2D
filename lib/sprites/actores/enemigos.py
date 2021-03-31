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

        self.hoja = GestorRecursos.CargarImagen(archivoImagen,-1)
        self.image = self.hoja.convert_alpha()
        self.rect = self.image.get_rect()
        self.current_frame = 0
        self.frames = 16
        self.frame_width = 64
        self.frame_height = 64
        self.contador = 0
        self.actualizarPostura()

    def mover_cpu(self, movimientoAngular,movimientoLineal):
        
        self.angulo = movimientoAngular
        adelanteX = math.cos(math.radians(self.angulo))
        adelanteY = math.sin(math.radians(self.angulo))
        self.adelante = (adelanteY, adelanteX)
        
        self.movimientoLineal = movimientoLineal

    def actualizarPostura(self):
        self.numImagenPostura = self.current_frame

    def update(self, tiempo):
        Actor.update(self, tiempo)

        return
