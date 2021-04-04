# -*- encoding: utf-8 -*-

# Modulos
import pygame
import sys
from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import *

FPS = 60

class Director():
    
    def __init__(self):
        #pila de escenas
        self.pila = []
        # Flag que nos indica cuando quieren salir de la escena de pygame
        self.salir_escena_pygame = False
        self.jugador = None
        self.puntuacionAnterior = 0

    def buclePygame(self, escena):

         # Cogemos el reloj de pygame
        reloj = pygame.time.Clock()

        # Ponemos el flag de salir de la escena a False
        self.salir_escena_pygame = False

        # Eliminamos todos los eventos producidos antes de entrar en el bucle
        pygame.event.clear()
        
        # El bucle del juego, las acciones que se realicen se harán en cada escena
        while not self.salir_escena_pygame:

            # Sincronizar el juego a 60 fps
            tiempo_pasado = reloj.tick(FPS)
            
            # Pasamos los eventos a la escena
            escena.eventos(pygame.event.get())

            # Actualiza la escena
            escena.update(tiempo_pasado)

            # Se dibuja en pantalla
            escena.dibujar(escena.pantalla)
            
            pygame.display.flip()

    def ejecutar(self):

        # Inicializamos la libreria de pygame (si no esta inicializada ya)
        pygame.init()
        # Creamos la pantalla de pygame (si no esta creada ya)
        self.screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        # Estas dos lineas realmente no son necesarias, se ponen aqui por seguridad,
        
        self.jugador = Jugador()
        self.puntuacionAnterior = self.jugador.puntuacion
        #self.bala = Bala()
        #self.gato = Gato()
        # Mientras haya escenas en la pila, ejecutaremos la de arriba
        while (len(self.pila)>0):

            # Se coge la escena a ejecutar como la que este en la cima de la pila
            escena = self.pila[len(self.pila)-1]

            # Si la escena es de pyame
            if isinstance(escena, EscenaPygame):

                # Ejecutamos el bucle
                self.buclePygame(escena)

            else:
                raise Exception('No se que tipo de escena es')

        # Finalizamos la libreria de pygame y cerramos las ventanas
        pygame.quit()


    def pararEscena(self):
        if (len(self.pila)>0):
            escena = self.pila[len(self.pila)-1]
            # Si la escena es de pygame
            if isinstance(escena, EscenaPygame):
                # Indicamos en el flag que se quiere salir de la escena
                self.salir_escena_pygame = True
            else:
                raise Exception('No se que tipo de escena es')

    def salirEscena(self):
        self.pararEscena()
        # Eliminamos la escena actual de la pila (si la hay)
        if (len(self.pila)>0):
            self.pila.pop()

    def salirPrograma(self):
        self.pararEscena()
        # Vaciamos la lista de escenas pendientes
        self.pila = []

    def cambiarEscena(self, escena):
        self.pararEscena()
        # Eliminamos la escena actual de la pila (si la hay)
        if (len(self.pila)>0):
            self.pila.pop()
        # Ponemos la escena pasada en la cima de la pila
        self.pila.append(escena)

    def apilarEscena(self, escena):
        self.pararEscena()
        # Ponemos la escena pasada en la cima de la pila
        #  (por encima de la actual)
        self.pila.append(escena)

    def volverAlMenu(self):
        self.pararEscena()
        #El menu es la primera escena,
        # volvemos atras hasta tener una escena en la pila 
        while(len(self.pila) > 1):
            self.pila.pop()
    
    def guardarPuntuacionAnterior(self):
        self.puntuacionAnterior = self.jugador.puntuacion
    
    def resetPuntuacionAAnterior(self):
        self.jugador.puntuacion = self.puntuacionAnterior
    
    def resetJugador(self):
        self.jugador = Jugador()
    
    def resetVidaJugador(self):
        self.jugador.establecerPosicion(self.jugador.origen)
        self.jugador.vida = self.jugador.maxVida
        """self.jugador.powerupActual = 0
        self.jugador.modificadorVel = 1
        self.jugador.modificadorGiro = 1
        self.jugador.escudo = False"""
        self.jugador._resetPowerUp()
        self.jugador.actualizarPostura()

