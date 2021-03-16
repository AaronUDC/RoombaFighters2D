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
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def disparar(self, x,y, estado):
        if estado:
            self.adelante

    def update(self, tiempo):
        self.actualizarDireccion()
        MiSprite.update(self, tiempo)

        return
