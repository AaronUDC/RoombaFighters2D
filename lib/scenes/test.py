# -*- encoding: utf-8 -*-

import pyglet
from lib.escena import *
from pygame.locals import *
from lib.sprites.jugador import Jugador
from lib.gestorRecursos import GestorRecursos

BLANCO = (255,255,255)

class Test(EscenaPygame):

    def __init__(self, director):

        EscenaPygame.__init__(self, director);
        # Tupla que representa el color blanco
        self.sofa = Sofa()
        self.jugador = Jugador()
        self.jugador.establecerPosicion((200,500))

        self.grupoSprites = pygame.sprite.Group(self.jugador)

        pygame.display.update()
        
    def update(self, tiempo):
        #update de eventos
        self.grupoSprites.update(tiempo)

    def eventos(self, listaEventos):
        for event in listaEventos:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                self.salirPrograma()

        teclasPulsadas = pygame.key.get_pressed()
        self.jugador.mover(teclasPulsadas, K_UP, K_DOWN, K_LEFT, K_RIGHT)

    def dibujar(self,pantalla):
        pantalla.fill(BLANCO)
        self.sofa.dibujar(pantalla)
        
        self.grupoSprites.draw(pantalla)

        pygame.display.update()
    
    def salirPrograma(self):
        self.director.salirPrograma()

class Sofa:
    
    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('sofa/sofa.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (270,120))
        self.rect = self.sprite.get_rect()
        self.posicionX = 500
        self.posicionY = 10

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self,pantalla):
        pantalla.blit(self.sprite,self.rect)