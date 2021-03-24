# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from lib.escena import *
from lib.sprites.sprite import *


class UI(MiSprite):

    #   Init
    #   Update()

    def __init__(self, posicion):
    
        MiSprite.__init__(self)
        self.posicionUI = posicion

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.image.get_rect())
