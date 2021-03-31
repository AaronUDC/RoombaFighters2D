
import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from math import *


class Torreta(Enemigos):

    def __init__(self, archivoImagen, archivoCoordenadas,numImagenes):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.activo = False
        Enemigos.__init__(self, archivoImagen,archivoCoordenadas, numImagenes, 10,10);

    def mover_cpu(self, jugador):

        (centroJX,centroJY) = jugador.rect.center
        (centroGX,centroGY) = self.rect.center
        radian = math.atan2(centroGX - centroJX, centroGY - centroJY)
        angulo = degrees(radian)
        Enemigos.mover_cpu(self,angulo,0)


    def update(self, tiempo, mascaraEstaticos, grupoJugadores):

        self.current_frame = 0
        self.actualizarPostura()

        Enemigos.update(self,tiempo)

class Gato(Torreta):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.activo = False
        self.tipo = 0
        Torreta.__init__(self, 'personajes/enemigos/gato/gato.png','personajes/enemigos/gato//coordGato.txt', [1,0,0]);

class Bebe(Torreta):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.activo = False
        self.tipo = 1
        Torreta.__init__(self, 'personajes/enemigos/bebe/BebeCabeza-Sheet.png','personajes/enemigos/bebe/coordBebe.txt',[3,0,0]);

    def update(self, tiempo):
        '''#(posActX, posActY) = self.posicion
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
            self.image = self.rot_center(self.hoja.subsurface(self.current_frame*64, 0, 64, 64), self.angulo)'''
        Enemigos.update(self,tiempo)