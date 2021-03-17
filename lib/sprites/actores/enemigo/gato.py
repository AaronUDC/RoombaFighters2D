# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from math import *


class Gato(Enemigos):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Enemigos.__init__(self, 'gato/gato.png', None, [6, 12, 6], 20,20);

    def mover_cpu(self, jugador):
        #sentido = IZQUIERDA
        """if jugador.posicion[0] < self.posicion[0] and jugador.posicion[1] < self.posicion[1] and jugador.movimientoLineal == ADELANTE:
            sentido = IZQUIERDA
        elif jugador.posicion[0] < self.posicion[0] and jugador.posicion[1] < self.posicion[1] and jugador.movimientoLineal == ATRAS:
            sentido = DERECHA
        elif jugador.posicion[0] > self.posicion[0] and jugador.posicion[1] < self.posicion[1] and jugador.movimientoLineal == ADELANTE:
            sentido = DERECHA
        elif jugador.posicion[0] > self.posicion[0] and jugador.posicion[1] < self.posicion[1] and jugador.movimientoLineal == ATRAS:
            sentido = IZQUIERDA
        elif jugador.posicion[0] < self.posicion[0] and jugador.posicion[1] > self.posicion[1] and jugador.movimientoLineal == ADELANTE:
            sentido = DERECHA
        elif jugador.posicion[0] < self.posicion[0] and jugador.posicion[1] > self.posicion[1] and jugador.movimientoLineal == ATRAS:
            sentido = IZQUIERDA
        elif jugador.posicion[0] > self.posicion[0] and jugador.posicion[1] > self.posicion[1] and jugador.movimientoLineal == ADELANTE:
            sentido = IZQUIERDA
        elif jugador.posicion[0] > self.posicion[0] and jugador.posicion[1] > self.posicion[1] and jugador.movimientoLineal == ATRAS:
            sentido = DERECHA"""
        coordx = jugador.posicion[0] - self.posicion[0]
        coordy = jugador.posicion[1] - self.posicion[1]
        modulo = sqrt((coordx)**2 + (coordy)**2)
        coordx = coordx / modulo
        coordy = coordy / modulo
        radian = math.atan2(coordy, coordx) * (180.0 / math.pi)
        angulo = degrees(radian)
        Enemigos.mover_cpu(self,jugador,angulo)

    def disparar(self, jugador):
        if ((jugador.posicion[0] - self.posicion[0]) < 200 and (jugador.posicion[0] - self.posicion[0]) > -200 ) and ((jugador.posicion[1] - self.posicion[1]) < 200 and (jugador.posicion[1] - self.posicion[1]) > -200 ):
            estado = 1
        else:
            estado = 0
        Enemigos.disparar(self, jugador.posicion[0], jugador.posicion[1], estado)
        return

    def update(self, tiempo, grupoElementosEstaticos):
       """ if self.angulo == DERECHA:
            Enemigos.mover_cpu(self, self.angulo)
        else:
            Enemigos.mover_cpu(self, self.angulo)"""
       Enemigos.update(self,tiempo)