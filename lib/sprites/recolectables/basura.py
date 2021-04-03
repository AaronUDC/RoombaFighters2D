# -*- coding: utf-8 -*-

import pygame, sys, os, math, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import *
from lib.sprites.actores.jugador import Jugador


class Basura(Recolectable):

    
    def __init__(self, tipo):

        Recolectable.__init__(self, 'recolectables/basura/Basura-Sheet.png','recolectables/basura/coordBasura.txt', [3,0,0], tipo)

        self.puntuacion = 0

        #self.coordenadasHoja = GestorRecursos.CargarArchivoCoordenadas('basura/coordBasura.txt')
        if tipo == 0:
            self.puntuacion = 10 
        elif tipo == 1:
            self.puntuacion = 50 
        elif tipo == 2:
            self.puntuacion = 100
        else: 
            raise ValueError("Tipo de basura no soportado")

    def update (self, tiempo, jugadores):
        sonido = GestorRecursos.CargarSonido("others/basura.mp3")
        Recolectable.update(self,tiempo,jugadores,0.3,Jugador.ganarPuntos,self.puntuacion,sonido)





