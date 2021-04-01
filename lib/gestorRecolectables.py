import pygame, sys, os, math, random
from pygame.locals import *
from lib.sprites.recolectables.recolectables import *

class GestorRecolectables():

    def __init__(self, cantidad, fSpawn, spawnCount, listaRecolectables):

        self.cantidad = cantidad
        self.fSpawn = fSpawn
        self.spawnCount = spawnCount
        self.contador = 0.0

        self.listaRecolectables = listaRecolectables
        random.seed()

    def update(self, tiempo, mascaraCol, rectPantalla):

        self.contador += (tiempo/1000)
        if self.contador > self.fSpawn:
            self.contador = 0.0
            total = random.randint(self.spawnCount[0], self.spawnCount[1])
            self.spawnRecolectables(total, mascaraCol, rectPantalla)
    
    def spawnRecolectables(self, total, mascaraCol, rectPantalla):
        
        #Implementar esto
        '''for i in range(total):
                for basura in basuras:
                    if not basura.activo:
                        basura.establecerPosicion((random.randint(0, tamanoV[0]), random.randint(0, tamanoV[1])))
                        (posX, posY) = basura.posicion
                        if mascaraCol.overlap_area(basura.mask, (int(posX), int(posY-basura.image.get_height()))) == 0:
                            basura.activo = True
                            break'''
        return

class GestorBasura(GestorRecolectables):

    def __init__(self, cantidad, fSpawn, spawnCount, listaBasuras, rectPantalla):
        GestorRecolectables.__init__(self, cantidad, fSpawn, spawnCount, listaBasuras)
        #Spawn inicial
        ##Poner valores mas altos para el spawn inicial
        total = random.randint( , )
        self.spawnRecolectables(total, mascaraCol, rectPantalla)

def iniBasuras( tipo0, tipo1, tipo2):

    total = tipo0 + tipo1 + tipo2
    basuras = []
    for i in range(tipo0):
        basuras.append(Basura(0))
    for i in range(tipo1):
        basuras.append(Basura(1))
    for i in range(tipo2):
        basuras.append(Basura(2))
    
    return total, basuras 

