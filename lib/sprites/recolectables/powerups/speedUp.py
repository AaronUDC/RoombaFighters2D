# -*- coding: utf-8 -*-

import pygame, sys, os, time, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import *
from math import *
from sounds import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 51)

class Thunder(Recolectable):

    def __init__(self):
        Recolectable.__init__(self, "recolectables/powerups/powerUps.png", "recolectables/powerups/coordPowerUps.txt", [2,0,0], 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.activo = False
        self.cantidad = 0

    def dibujar(self, pantalla):
        if self.activo:
            pantalla.blit(self.image, self.rect)

    def thunderSoundEffect(self):
        thunderSound = pygame.mixer.Sound("powerups/thunderEffect.mp3")
        thunderSound.play()

    def thunderMusic(self, play):
        if play:
            pygame.mixer.music.load("powerups/thunderMusic.mp3")
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.stop()

    def update(self, tiempo):
        return

class ThunderGestor():

    def __init__(self, cantidad, fSpawn, mascaraCol, thunder, tamanoV):
        self.cantidad = cantidad
        self.fSpawn = fSpawn
        self.contador = 0.0
        random.seed()

        if not thunder.activo and cantidad < 1:
            thunder.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
            (thunderX, thunderY) = thunder.posicion
            if mascaraCol.overlap_area(thunder.mask, (int(thunderX), int(thunderY - thunder.image.get_height()))) == 0:
                thunder.activo = True
                thunder.cantidad = 1
                self.drawSpeedBar

    def drawSpeedBar(self, surface, x, y, percentage): #No funciona
        barLength = 50
        barHeight = 10
        fill = (percentage / 100) * barHeight
        border = pygame.Rect(x, y, barLength, barHeight)
        fill = pygame.Rect(x, y, fill, barHeight)
        pygame.draw.rect(surface, YELLOW, fill)
        pygame.draw.rect(surface, BLACK, border, 2)

    def update(self, tiempo, mascaraCol, thunder, tamanoV):
        self.contador += tiempo/60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            apparition = random.randint(0, 100)
            if not thunder.activo and apparition < 3:
                thunder.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
                (thunderX, thunderY) = thunder.posicion
                if mascaraCol.overlap_area(thunder.mask, (int(thunderX), int(thunderY - thunder.image.get_height()))) == 0:
                    thunder.activo = True
