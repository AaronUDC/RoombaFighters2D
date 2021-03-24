# -*- coding: utf-8 -*-

import pygame, sys, os, math
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.sprite import *

QUIETO = 0
IZQUIERDA = 1
DERECHA = 2
ADELANTE = 1
ATRAS = 2

class Actor(MiSprite):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadCarrera, velGiro):

        MiSprite.__init__(self)

        self.hoja = GestorRecursos.CargarImagen(archivoImagen,-1)
        self.image = self.hoja.convert_alpha()

        self.angulo = 0
        self.adelante = (0,1)

        self.velGiro = velGiro
        self.velocidadCarrera = velocidadCarrera
        
        self.numPostura = 0
        self.numImagenPostura = 0
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
        
        self.rect = pygame.Rect(0,0,self.coordenadasHoja[self.numPostura][self.numImagenPostura][2],self.coordenadasHoja[self.numPostura][self.numImagenPostura][3])

        self.actualizarDireccion()
        
        
    def actualizarDireccion(self):
        #self.image = pygame.transform.rotate(self.hoja,self.angulo)
        self.image = self.rot_center(self.hoja.subsurface(self.coordenadasHoja[self.numPostura][self.numImagenPostura]).copy(),self.angulo)

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def mover(self, movimientoLineal,movimientoAngular):
        self.movimientoLineal = movimientoLineal
        self.movimientoAngular = movimientoAngular

    def girar(self,tiempo, sentido):
        self.angulo = ((sentido * self.velGiro)/tiempo + self.angulo)
        (adelanteY, adelanteX) = self.adelante
        adelanteX = math.cos(math.radians(self.angulo))
        adelanteY = math.sin(math.radians(self.angulo))
        self.adelante = (adelanteY,adelanteX)
 
    def update(self, tiempo):
        
        self.actualizarDireccion()
        MiSprite.update(self,tiempo)

        return

    

    




