# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigo.proyectil import *
from math import *


class Bala(Proyectil):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Proyectil.__init__(self, 'roomba/roomba.png', None, [6, 12, 6], 40, 0);

    def update(self, tiempo):
        Actor.update(self,tiempo)
        MiSprite.update(self,tiempo)

        return