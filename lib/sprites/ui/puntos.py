# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from lib.escena import *
from lib.sprites.ui.ui import *


class Puntos(UI):


    def __init__(self, posicion):

        UI.__init__(self, posicion)
       
        self.tipoLetra = pygame.font.SysFont('fuenteMenu.ttf', 30)
        
        self.marcador = 0
        self.image = self.tipoLetra.render(str(self.marcador), True, (0,0,0))
        self.rect = self.image.get_rect()


    def update(self, tiempo, jugador):

        self.marcador = jugador.puntuacion
        self.image = self.tipoLetra.render(str(self.marcador), True, (0,0,0))
        #self.rect = self.image.get_rect()
        self.establecerPosicion(self.posicionUI)

