# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.enemigos import *
from math import *

class EnemigoSeguidor(Enemigos):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadCarrera, velGiro):
        Enemigos.__init__(self, archivoImagen ,archivoCoordenadas, numImagenes, velocidadCarrera, velGiro);


    def mover_cpu(self, movimientoAngular,movimientoLineal):
        Enemigos.mover_cpu(movimientoAngular,movimientoLineal)
    
    def update(self, tiempo, jugador):
        
        (centroJX,centroJY) = jugador.rect.center
        (centroGX,centroGY) = self.rect.center
        radian = math.atan2(centroGX - centroJX, centroGY - centroJY)
        angulo = degrees(radian)
        if angulo > self.velGiro:
            angulo = self.velGiro
        Enemigos.mover_cpu(self,angulo,velocidadCarrera)

class Fantasma(EnemigoSeguidor):

   def __init__(self):
        Actor.__init__(self, 'personajes/enemigos/fantasma/Fantasma.png' ,'', 1, 10, 20); 

