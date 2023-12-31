# -*- coding: utf-8 -*-

import pygame, sys, os, math
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.sprite import *
from sounds import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Recolectable(MiSprite):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, tipo):
        MiSprite.__init__(self)
        
        self.hoja = GestorRecursos.CargarImagen(archivoImagen,-1)

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
        self.mask = pygame.mask.from_surface(self.image)
        self.activo = False

    def update(self,tiempo, jugadores, ratio, accion, *args):
        
        MiSprite.update(self,tiempo)
        #Si estamos activos, gestionamos las colisiones y realizamos 
        # una accion del jugador si colisionamos con este
        if self.activo:
            jugadores = pygame.sprite.spritecollide(self, jugadores, False, pygame.sprite.collide_circle_ratio(ratio))
            if jugadores != None:
                for jugador in jugadores:
                    self.activo = False
                    accion(jugador,*args)
                    break

    def dibujar(self, pantalla):
        #Solo la dibujamos si esta activo
        if self.activo:
            pantalla.blit(self.image, self.rect)
        