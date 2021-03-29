# -*- coding: utf-8 -*-

import pygame, sys, os, math
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.sprite import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Recolectables(MiSprite):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, efectoSonido, archivoMusica, tipo):
        MiSprite.__init__(self)
        self.hoja = GestorRecursos.CargarImagen(archivoImagen,-1)
        self.sound = efectoSonido
        self.music = archivoMusica

        self.numPostura = 0
        self.numImagenPostura = tipo
        self.coordenadasHoja = []
        if archivoCoordenadas != None:
            datos = GestorRecursos.CargarArchivoCoordenadas(archivoCoordenadas)
            datos = datos.split()
            cont = 0
            for linea in range(0,3):
                self.coordenadasHoja.append([])
                tmp = self.coordenadasHoja[linea]
                for postura in range(1, numImagenes[linea]+1):
                    tmp.append(pygame.Rect((int(datos[cont]), int(datos[cont+1])), (int(datos[cont+2]), int(datos[cont+3]))))
                    cont += 4
        self.image = self.hoja.convert_alpha()
        self.image = self.hoja.subsurface(self.coordenadasHoja[self.numPostura][self.numImagenPostura]).copy()


        self.rect = pygame.Rect(self.coordenadasHoja[self.numPostura][self.numImagenPostura][0],
                                self.coordenadasHoja[self.numPostura][self.numImagenPostura][1],
                                self.coordenadasHoja[self.numPostura][self.numImagenPostura][2],
                                self.coordenadasHoja[self.numPostura][self.numImagenPostura][3])
        


    '''def drawText (self, surface, text, size, x, y):
        font = pygame.font.SysFont("serif", size)
        textSurface = font.render(text, True, WHITE)
        textRect = textSurface.get_rect()
        textRect.midtop = (x, y)
        surface.blit(textSurface, textRect)'''

    '''def update(self, tiempo):
        MiSprite.update(self)
        return'''