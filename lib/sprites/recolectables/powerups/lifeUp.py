# -*- coding: utf-8 -*-

import pygame, sys, os, time, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import *
from math import *

class Wrench(Recolectables):

    def __init__(self):
        Recolectables.__init__(self, "powerups/wrench.png", "powerups/coordWrench.txt", [1,0,0], "powerups/wrenchEffect.mp3", "",0)
        self.mask = pygame.mask.from_surface(self.image)
        self.activo = False
        self.cantidad = 0

    def dibujar(self, pantalla):
        if self.activo:
            pantalla.blit(self.image, self.rect)

    def wrenchSoundEffect(self):
        wrenchSound = pygame.mixer.Sound("powerups/wrenchEffect.mp3")
        wrenchSound.play()

    def update(self, tiempo):
        return

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