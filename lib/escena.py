# -*- encoding: utf-8 -*-

import pygame, sys
from pygame.locals import *

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# -------------------------------------------------
# Clase Escena con lo metodos abstractos

class Escena:

    def __init__(self, director):
        self.director = director

    def update(self, *args):
        pygame.display.update()
        #raise NotImplemented("Tiene que implementar el metodo update.")

    def eventos(self, *args):
        pygame.display.update()
        #raise NotImplemented("Tiene que implementar el metodo eventos.")

    def dibujar(self):
        raise NotImplemented("Tiene que implementar el metodo dibujar.")

class EscenaPygame(Escena):

    def __init__(self, director):
        Escena.__init__(self, director)
        # Inicializamos la libreria de pygame (si no esta inicializada ya)
        pygame.init()
        # Tupla que representa el color blanco
        BLANCO = (255,255,255)
        # Creamos la pantalla (si no esta creada ya)
        screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pygame.display.set_caption("Sofa")
        icon = pygame.image.load('sofa2.png')
        pygame.display.set_icon(icon)
        sofaImg = pygame.image.load('sofa.png')
        sofaX = 300
        sofaY = 0

        def sofa():
            screen.blit(sofaImg, (sofaX, sofaY))

        mesaImg = pygame.image.load('mesa.png')
        mesaX = 0
        mesaY = 200

        def mesa():
            screen.blit(mesaImg, (mesaX, mesaY))
        tipoLetra = pygame.font.SysFont('arial', 96)
        screen.blit(tipoLetra.render('TEST', True, BLANCO), (50, ALTO_PANTALLA/4, 200, 100))
        screen.blit(tipoLetra.render('Pulse calquer tecla', True, BLANCO), (20, ALTO_PANTALLA/2, 200, 100))
        pygame.display.update()

        running = True
        while running:

          screen.fill((141, 73, 37))

          for event in pygame.event.get():
                if event.type == KEYDOWN:
                  running = False
          
        sofa()
        mesa()
        pygame.display.update()

    def eventos(self, *args):
        screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        # Tupla que representa el color blanco
        BLANCO = (255,255,255)
        running = True
        while running:

          for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                  running = False

        pygame.draw.circle(screen, BLANCO, (50,50),4,0)
        pygame.display.update()

    def dibujar(self):
        screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

        sofaImg = pygame.image.load('sofa.png')
        sofaX = 0
        sofaY = 0

        def sofa():
            screen.blit(sofaImg, (sofaX, sofaY))

        while running:

          for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                  running = False

        sofa()
        pygame.display.update()

class EscenaPyglet(Escena):

    def __init__(self, director):
        Escena.__init__(self, director)
