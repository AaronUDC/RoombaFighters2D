
import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from math import *


class Torreta(Enemigos):

    def __init__(self, archivoImagen, archivoCoordenadas):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.activo = False
        Enemigos.__init__(self, archivoImagen,archivoCoordenadas, [3,3,3], 10,10);

    def mover_cpu(self, jugador):

        (centroJX,centroJY) = jugador.rect.center
        (centroGX,centroGY) = self.rect.center
        radian = math.atan2(centroGX - centroJX, centroGY - centroJY)
        angulo = degrees(radian)
        Enemigos.mover_cpu(self,angulo,0)


    def update(self, tiempo, mascaraEstaticos, grupoJugadores,tipo,pantalla):
       """ if self.angulo == DERECHA:
            Enemigos.mover_cpu(self, self.angulo)
        else:
            Enemigos.mover_cpu(self, self.angulo)"""
       Enemigos.update(self,tiempo,tipo,pantalla)