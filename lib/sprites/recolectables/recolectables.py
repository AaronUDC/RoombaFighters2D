# -*- coding: utf-8 -*-

import pygame, sys, os, math
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.sprite import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Recolectables(MiSprite):

    def __init__(self, archivoImagen, efectoSonido, archivoMusica):
        MiSprite.__init__(self)
        self.hoja = GestorRecursos.CargarImagen(archivoImagen,-1)
        self.image = self.hoja.convert_alpha()
        self.sound = efectoSonido
        self.music = archivoMusica
        self.rect = self.image.get_rect()

    '''def drawText (self, surface, text, size, x, y):
        font = pygame.font.SysFont("serif", size)
        textSurface = font.render(text, True, WHITE)
        textRect = textSurface.get_rect()
        textRect.midtop = (x, y)
        surface.blit(textSurface, textRect)'''

    '''def update(self, tiempo):
        MiSprite.update(self)
        return'''