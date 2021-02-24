# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from escena import *
#from gestorRecursos import *

class MiSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.posicion = (0,0)
        self.velocidad = (0,0)
        self.scroll = (0,0)

    def setPosicion(self, pos):
        self.posicion = pos
        self.rect.left = self.posicion[0] - self.scroll[0]
        self.rect.bottom = self.posicion[1] - self.scroll[0]

    
    



