# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.sprite import *


class Prop(MiSprite):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes):

        MiSprite.__init__(self)

        self.hoja = GestorRecursos.CargarImagen(archivoImagen, -1)
        self.image = self.hoja.convert_alpha()

        self.rect = self.image.get_rect()