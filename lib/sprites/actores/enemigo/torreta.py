
import pygame, sys, os
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.actores.actores import *
from lib.sprites.actores.enemigos import *
from lib.sprites.actores.enemigo.bala import Bala
from math import *


class Torreta(Enemigos):

    def __init__(self, archivoImagen, archivoCoordenadas,numImagenes, bala, areaDeteccion):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.activo = False
        self.bala = bala
        self.areaDeteccion = areaDeteccion
        Enemigos.__init__(self, archivoImagen,archivoCoordenadas, numImagenes, 10,10);
        self.jugadorFuera = False

    def mover_cpu(self, jugador):

        (centroJX,centroJY) = jugador.rect.center
        (centroGX,centroGY) = self.rect.center
        radian = math.atan2(centroGX - centroJX, centroGY - centroJY)
        angulo = degrees(radian)
        Enemigos.mover_cpu(self,angulo,0)


    def update(self, tiempo, grupoJugadores):
        
        if self.bala.estaEspera():
            for jugador in grupoJugadores:
                if self.areaDeteccion.colliderect(jugador.rect):
                    if not self.jugadorFuera:
                        self.bala.disparar(jugador)
                    self.jugadorFuera = True
                    break
                else:
                    self.jugadorFuera = False

        Enemigos.update(self,tiempo)



class Gato(Torreta):

    def __init__(self,bala,areaDeteccion):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.tipo = 0
        Torreta.__init__(self, 'personajes/enemigos/gato/gato.png','personajes/enemigos/gato/coordGato.txt', [1,0,0],bala,areaDeteccion);

class Bebe(Torreta):

    def __init__(self,bala,areaDeteccion):
        # Invocamos al constructor de la clase padre con la configuracion de este personaje concreto
        self.tipo = 1
        Torreta.__init__(self, 'personajes/enemigos/bebe/BebeCabeza-Sheet.png','personajes/enemigos/bebe/coordBebe.txt',[16,0,0],bala,areaDeteccion);
        self.numFrames = 15
        self.duracionFrame = 0.07
        self.contadorFrame = 0
        self.disparando = False

    def update(self, tiempo, grupoJugadores):
        
        if self.disparando:
            if self.contadorFrame > self.duracionFrame:
                self.contadorFrame = 0
                if self.numImagenPostura >= self.numFrames:
                    self.numImagenPostura = 0
                    self.disparando = False
                else:
                    self.numImagenPostura += 1
            else:
                self.contadorFrame += (tiempo/1000)
        
        if self.bala.estaEspera() and not self.disparando:
            for jugador in grupoJugadores:
                if self.areaDeteccion.colliderect(jugador.rect):
                    self.disparando = True
                    break
            
        Torreta.update(self,tiempo,grupoJugadores)