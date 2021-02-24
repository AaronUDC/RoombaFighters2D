# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from lib.escena import *
#from lib.actors.r import *

class Test(EscenaPygame, pyglet.window.Window):

    def __init__(self, director):

        EscenaPygame.__init__(self, director)
    
        
    def update(self, *args):
        raise NotImplemented("Tiene que implementar el metodo update.")

    def eventos(self, *args):
        raise NotImplemented("Tiene que implementar el metodo eventos.")

    def dibujar(self):
        raise NotImplemented("Tiene que implementar el metodo dibujar.")
        
    