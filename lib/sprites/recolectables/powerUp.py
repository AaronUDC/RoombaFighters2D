import pygame, sys, os, math, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import Recolectable


class Powerup(Recolectable):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, tipo):
        Recolectable.__init__(self, archivoImagen, archivoCoordenadas, numImagenes, 0)
        self.mask = pygame.mask.from_surface(self.image)
        


