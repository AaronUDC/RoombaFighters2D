import pygame, sys, os, math, random
from pygame.locals import *
from lib.sprites.recolectables.recolectables import *
from lib.sprites.recolectables.basura import *

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
    
    def spawnRecolectables(self, total, mascaraCol, rectPantalla,listaRecolectables):
        
        #Implementar esto
        for i in range(total):
                for recolectable in listaRecolectables:
                    if not recolectable.activo:
                        recolectable.establecerPosicion((random.randint(0, rectPantalla[0]), random.randint(0, rectPantalla[1])))
                        (posX, posY) = recolectable.posicion
                        if mascaraCol.overlap_area(recolectable.mask, (int(posX), int(posY-recolectable.image.get_height()))) == 0:
                            recolectable.activo = True
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

class GestorBasuraR(GestorRecolectables):

    def __init__(self, cantidad, fSpawn, spawnCount, listaBasuras, rectPantalla,mascaraCol):
        GestorRecolectables.__init__(self, cantidad, fSpawn, spawnCount, listaBasuras)
        #Spawn inicial
        ##Poner valores mas altos para el spawn inicial
        total = random.randint(10, 20)
        self.spawnRecolectables(total, mascaraCol, rectPantalla,listaBasuras)

    def update(self,tiempo,mascaraCol, rectPantalla, listaBasuras):
        self.contador += tiempo / 60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            total = random.randint(self.spawnCount[0], self.spawnCount[1])
            self.spawnRecolectables(total, mascaraCol, rectPantalla, listaBasuras)

class GestorThunder(GestorRecolectables):

    def __init__(self, cantidad, fSpawn, spawnCount, listaBasuras, rectPantalla,mascaraCol):
        GestorRecolectables.__init__(self, cantidad, fSpawn, spawnCount, listaBasuras)
        #Spawn inicial
        ##Poner valores mas altos para el spawn inicial
        total = random.randint(10, 20)
        self.spawnRecolectables(1, mascaraCol, rectPantalla,listaBasuras)

    def update(self,tiempo,mascaraCol, rectPantalla, listaBasuras):
        self.contador += tiempo / 60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            total = random.randint(self.spawnCount[0], self.spawnCount[1])
            self.spawnRecolectables(total, mascaraCol, rectPantalla, listaBasuras)

class GestorShield(GestorRecolectables):

    def __init__(self, cantidad, fSpawn, spawnCount, listaBasuras, rectPantalla,mascaraCol):
        GestorRecolectables.__init__(self, cantidad, fSpawn, spawnCount, listaBasuras)
        #Spawn inicial
        ##Poner valores mas altos para el spawn inicial
        total = random.randint(0, 2)
        self.spawnRecolectables(1, mascaraCol, rectPantalla,listaBasuras)

    def update(self,tiempo,mascaraCol, rectPantalla, listaBasuras):
        self.contador += tiempo / 60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            total = random.randint(self.spawnCount[0], self.spawnCount[1])
            self.spawnRecolectables(total, mascaraCol, rectPantalla, listaBasuras)

class GestorWrenches(GestorRecolectables):

    def __init__(self, cantidad, fSpawn, spawnCount, listaBasuras, rectPantalla,mascaraCol):
        GestorRecolectables.__init__(self, cantidad, fSpawn, spawnCount, listaBasuras)
        #Spawn inicial
        ##Poner valores mas altos para el spawn inicial
        total = random.randint(0, 2)
        self.spawnRecolectables(1, mascaraCol, rectPantalla,listaBasuras)

    def update(self,tiempo,mascaraCol, rectPantalla, listaBasuras):
        self.contador += tiempo / 60
        if self.contador > self.fSpawn:
            self.contador = 0.0
            total = random.randint(self.spawnCount[0], self.spawnCount[1])
            self.spawnRecolectables(total, mascaraCol, rectPantalla, listaBasuras)

