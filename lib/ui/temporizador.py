# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from lib.escena import *
from lib.ui.ui import *

class Temporizador(TextoGUI):


    def __init__(self,pantalla, posicion, tiempoLimite):

        self.tiempoLimite = tiempoLimite
        self.fuente = pygame.font.Font('fuenteMenu.ttf', 30);
        self.color = (0,0,0)
        TextoGUI.__init__(self, pantalla, self.fuente, self.color, '000', posicion)

    def update(self, tiempo):
        if int(self.tiempoLimite) >= 0:
            self.tiempoLimite -= (tiempo/1000)
        
            self.imagen = self.fuente.render(str(int(self.tiempoLimite)), True, self.color)
        else:
            self.imagen = self.fuente.render('TIEMPO!!', True, self.color)

