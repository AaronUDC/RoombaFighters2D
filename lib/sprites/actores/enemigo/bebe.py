
import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from lib.sprites.actores.enemigo.torreta import *
from math import *


class Bebe(Torreta):

    def __init__(self):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.activo = False
        Torreta.__init__(self, 'personajes/enemigos/gato/gato.png','personajes/enemigos/gato//coordGato.txt');

    """def mover_cpu(self, jugador):

        (centroJX,centroJY) = jugador.rect.center
        (centroGX,centroGY) = self.rect.center
        radian = math.atan2(centroGX - centroJX, centroGY - centroJY)
        angulo = degrees(radian)
        Enemigos.mover_cpu(self,angulo,0)"""


    """def update(self, tiempo, mascaraEstaticos):
        if self.angulo == DERECHA:
            Enemigos.mover_cpu(self, self.angulo)
        else:
            Enemigos.mover_cpu(self, self.angulo)
       Enemigos.update(self,tiempo)"""