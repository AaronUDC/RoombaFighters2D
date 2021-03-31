# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from math import *


class Enemigos(Actor):

    def __init__(self, archivoImagen, archivoCoordenadas, numImagenes, velocidadCarrera, velGiro):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        Actor.__init__(self, archivoImagen ,archivoCoordenadas, numImagenes, velocidadCarrera, velGiro);

        self.hoja = GestorRecursos.CargarImagen(archivoImagen,-1)
        self.image = self.hoja.convert_alpha()
        self.rect = self.image.get_rect()
        self.current_frame = 0
        self.frames = 16
        self.frame_width = 64
        self.frame_height = 64
        self.contador = 0
        self.actualizarPostura()

    def mover_cpu(self, movimientoAngular,movimientoLineal):
        
        self.angulo = movimientoAngular
        adelanteX = math.cos(math.radians(self.angulo))
        adelanteY = math.sin(math.radians(self.angulo))
        self.adelante = (adelanteY, adelanteX)
        
        self.movimientoLineal = movimientoLineal

    def actualizarPostura(self):
        self.numImagenPostura = self.current_frame

    def update(self, tiempo,tipo,pantalla):
        Actor.update(self, tiempo)

        if tipo == 1:
            #(posActX, posActY) = self.posicion
            #MiSprite.establecerPosicion(self, (posActX,posActY))
            if self.current_frame >= self.frames - 1:
                self.current_frame = 0
            else:
                if self.contador == 6:
                    self.current_frame += 1
                    self.contador = 0
                else:
                    self.contador += 1
            #new_area = pygame.Rect((self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height))
            if (self.current_frame*64) % 64 == 0:
                self.image = self.rot_center(self.hoja.subsurface(self.current_frame*64, 0, 64, 64), self.angulo)
            #pantalla.blit(self.image, (700, 350))
        else:
            self.current_frame = 0
            self.actualizarPostura()

        return
