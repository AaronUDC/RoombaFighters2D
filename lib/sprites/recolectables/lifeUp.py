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

    def update(self, tiempo, jugadores):
        Recolectable.update(self,tiempo,jugadores, 0.3, Jugador.curarVida)
