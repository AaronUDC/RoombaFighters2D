# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from math import *


class Bala(Enemigos):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self, 'bala/bala.png', None, [6, 12, 6], 20, 10);

    def disparar(self, jugador):
        coordx = jugador.posicion[0] - self.posicion[0]
        coordy = jugador.posicion[1] - self.posicion[1]
        modulo = sqrt((coordx) ** 2 + (coordy) ** 2)
        coordx = coordx / modulo
        coordy = coordy / modulo
        radian = math.atan2(coordy, coordx) * (180.0 / math.pi)
        angulo = degrees(radian)
        if ((jugador.posicion[0] - self.posicion[0]) < 200 and (jugador.posicion[0] - self.posicion[0]) > -200) and ( (jugador.posicion[1] - self.posicion[1]) < 200 and (jugador.posicion[1] - self.posicion[1]) > -200):
            estado = 1
        else:
            estado = 0
        Enemigos.disparar(self, jugador.posicion[0], jugador.posicion[1], estado,angulo)
        return

    def update(self, tiempo,grupoElementosEstaticos):
        Actor.update(self,tiempo)
        MiSprite.update(self,tiempo)

        return