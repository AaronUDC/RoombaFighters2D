# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from lib.escena import *
from lib.ui.ui import *


class Puntos(TextoGUI):


    def __init__(self,pantalla, posicion):

        self.fuente = pygame.font.Font('fuenteMenu.ttf', 30);
        self.color = (0,0,0)
        TextoGUI.__init__(self, pantalla, self.fuente, self.color, '000', posicion)

    def update(self, tiempo, jugador):
        self.imagen = self.fuente.render(str(jugador.puntuacion), True, self.color)


