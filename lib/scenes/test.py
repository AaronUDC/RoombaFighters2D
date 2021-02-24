# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from lib.escena import *
from lib.actors.roomba import *

class EscenaTest(EscenaPygame, pyglet.window.Window):

    def __init__(self, director):

        EscenaPygame.__init__(self, director)
    
        self.Jugador = Jugador()

        
    