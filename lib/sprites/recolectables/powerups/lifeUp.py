# -*- coding: utf-8 -*-

import pygame, sys, os, time, random, math
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import *
from lib.sprites.actores.jugador import Jugador


class Wrench(Recolectable):

    def __init__(self):
        Recolectable.__init__(self, "recolectables/powerups/wrench.png", "recolectables/powerups/coordWrench.txt", [1,0,0],0)

    def wrenchSoundEffect(self):
        wrenchSound = pygame.mixer.Sound("recolectables/powerups/wrenchEffect.mp3")
        wrenchSound.play()

    def update(self, tiempo):
        Recolectable.update(self,tiempo,jugadores, 0.3, Jugador.curarVida)

class WrenchGestor():

    def __init__(self, cantidad, fSpawn, mascaraCol, wrench, tamanoV):
        self.cantidad = cantidad
        self.fSpawn = fSpawn
        self.contador = 0.0
        random.seed()

        if not wrench.activo and cantidad < 1:
            wrench.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
            (wrenchX, wrenchY) = wrench.posicion
            if mascaraCol.overlap_area(wrench.mask, (int(wrenchX), int(wrenchY - wrench.image.get_height()))) == 0:
                wrench.activo = True
                wrench.cantidad = 1

    def update(self, tiempo, mascaraCol, wrench, tamanoV):
        self.contador += tiempo/60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            apparition = random.randint(0, 100)
            if not wrench.activo and apparition < 30:
                wrench.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
                (wrenchX, wrenchY) = wrench.posicion
                if mascaraCol.overlap_area(wrench.mask, (int(wrenchX), int(wrenchY - wrench.image.get_height()))) == 0:
                    wrench.activo = True
