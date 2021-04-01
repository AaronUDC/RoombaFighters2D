# -*- coding: utf-8 -*-

import pygame, sys, os, time, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import *
from math import *

class Shield(Recolectable):

    def __init__(self):
        Recolectable.__init__(self, "recolectables/powerups/powerUps.png","recolectables/powerups/coordPowerUps.txt", [2,0,0],1)
        self.mask = pygame.mask.from_surface(self.image)
        self.activo = False
        self.cantidad = 0

    def dibujar(self, pantalla):
        if self.activo:
            pantalla.blit(self.image, self.rect)

    def shieldMusic(self, play):
        if play:
            pygame.mixer.music.load("recolectables/powerups/shieldMusic.mp3")
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.stop()

    def update(self, tiempo):
        return

class ShieldGestor():

    def __init__(self, cantidad, fSpawn, mascaraCol, shield, tamanoV):
        self.cantidad = cantidad
        self.fSpawn = fSpawn
        self.contador = 0.0
        random.seed()

        if not shield.activo and cantidad < 1:
            shield.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
            (shieldX, shieldY) = shield.posicion
            if mascaraCol.overlap_area(shield.mask, (int(shieldX), int(shieldY - shield.image.get_height()))) == 0:
                shield.activo = True
                shield.cantidad = 1

    def update(self, tiempo, mascaraCol, shield, tamanoV):
        self.contador += tiempo/60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            apparition = random.randint(0, 100)
            if not shield.activo and apparition < 30:
                shield.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
                (shieldX, shieldY) = shield.posicion
                if mascaraCol.overlap_area(shield.mask, (int(shieldX), int(shieldY - shield.image.get_height()))) == 0:
                    shield.activo = True