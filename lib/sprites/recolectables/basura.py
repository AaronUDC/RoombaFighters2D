# -*- coding: utf-8 -*-

import pygame, sys, os, math, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import *


class Basura(Recolectables):

    
    def __init__(self, tipo):

        Recolectables.__init__(self, 'basura/Basura-Sheet.png','basura/coordBasura.txt', [3,3,3], "", "")

        self.mask = pygame.mask.from_surface(self.image)
        self.tipo = tipo
        self.puntuacion = 0
        self.random = random.randint(0, 90)
        self.hoja = GestorRecursos.CargarImagen('basura/Basura-Sheet.png',-1)
        self.image = self.hoja.convert_alpha()
        #self.coordenadasHoja = GestorRecursos.CargarArchivoCoordenadas('basura/coordBasura.txt')
        if tipo == 0:
            self.puntuacion = 10 
        elif tipo == 1:
            self.puntuacion = 50 
        elif tipo == 2:
            self.puntuacion = 100
        else: 
            raise ValueError("Tipo de basura no soportado")


        self.activo = False


    def dibujar(self, pantalla):
        if self.activo:
            if self.tipo == 0:
                self.image = self.rot_center(self.hoja.subsurface(0,0,64,64).copy(),self.random)
                pantalla.blit(self.image, self.rect)
            if self.tipo == 1:
                self.image = self.rot_center(self.hoja.subsurface(64,0,64,64).copy(),self.random)
                pantalla.blit(self.image, self.rect)
            if self.tipo == 2:
                self.image = self.rot_center(self.hoja.subsurface(128,0,64,64).copy(),self.random)
                pantalla.blit(self.image, self.rect)

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def update (self, tiempo):
        return


class GestorBasura():

    def __init__(self, cantidad, fSpawn, spawnCount, mascaraCol, basuras, tamanoV):

        self.cantidad = cantidad
        self.fSpawn = fSpawn
        self.spawnCount = spawnCount
        self.contador = 0.0
        random.seed()

        total = int(cantidad/2)
        for i in range(total):
                for basura in basuras:
                    if not basura.activo:
                        basura.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
                        (posX, posY) = basura.posicion
                        if mascaraCol.overlap_area(basura.mask, (int(posX), int(posY-basura.image.get_height()))) == 0:
                            basura.activo = True
                            break


    def update(self, tiempo, mascaraCol, basuras, tamanoV):

        self.contador += tiempo/60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            total = random.randint(self.spawnCount[0], self.spawnCount[1])
            
            for i in range(total):
                for basura in basuras:
                    if not basura.activo:
                        basura.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
                        (posX, posY) = basura.posicion
                        if mascaraCol.overlap_area(basura.mask, (int(posX), int(posY-basura.image.get_height()))) == 0:
                            basura.activo = True
                            break

                

def iniBasuras(tipo0, tipo1, tipo2):

    total = tipo0 + tipo1 + tipo2
    basuras = []
    for i in range(tipo0):
        basuras.append(Basura(0))
    for i in range(tipo1):
        basuras.append(Basura(1))
    for i in range(tipo2):
        basuras.append(Basura(2))
    
    return total, basuras 





