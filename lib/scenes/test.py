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
        self.sofa2 = Sofa2()
        self.mesagato = Mesagato()
        self.silla = Silla()
        self.silla2 = Silla2()
        self.silla3 = Silla3()
        self.silla4 = Silla4()
        self.mesita = Mesita()
        self.soporte = Soporte()
        self.mesa3 = Mesa3()
        self.jugador = Jugador()
        self.jugador.establecerPosicion((150,150))

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
        self.sofa2.dibujar(pantalla)
        self.mesagato.dibujar(pantalla)
        self.silla.dibujar(pantalla)
        self.silla2.dibujar(pantalla)
        self.silla3.dibujar(pantalla)
        self.silla4.dibujar(pantalla)
        self.mesita.dibujar(pantalla)
        self.soporte.dibujar(pantalla)
        self.mesa3.dibujar(pantalla)
        
        self.grupoSprites.draw(pantalla)

        pygame.display.update()
    
    def salirPrograma(self):
        self.director.salirPrograma()

class Sofa:
    
    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('sofa/sofab.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (270,120))
        self.rect = self.sprite.get_rect()
        self.posicionX = 650
        self.posicionY = 450

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self,pantalla):
        pantalla.blit(self.sprite,self.rect)


class Sofa2:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('sofa/sofad.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (120, 270))
        self.rect = self.sprite.get_rect()
        self.posicionX = 750
        self.posicionY = 200

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)


class Mesagato:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('mesagato/mesagato.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (132, 260))
        self.rect = self.sprite.get_rect()
        self.posicionX = 250
        self.posicionY = 200

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)

class Silla:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('silla/silla.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (68, 68))
        self.rect = self.sprite.get_rect()
        self.posicionX = 100
        self.posicionY = 200

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)

class Silla2:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('silla/silla.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (68, 68))
        self.rect = self.sprite.get_rect()
        self.posicionX = 100
        self.posicionY = 350

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)

class Silla3:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('silla/sillag.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (68, 68))
        self.rect = self.sprite.get_rect()
        self.posicionX = 325
        self.posicionY = 200

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)

class Silla4:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('silla/sillag.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (68, 68))
        self.rect = self.sprite.get_rect()
        self.posicionX = 325
        self.posicionY = 350

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)

class Mesita:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('mesa cafe/mesita.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (100, 100))
        self.rect = self.sprite.get_rect()
        self.posicionX = 700
        self.posicionY = 75

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)

class Soporte:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('soporte/soporte.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (258, 98))
        self.rect = self.sprite.get_rect()
        self.posicionX = 550
        self.posicionY = 0

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)

class Mesa3:

    def __init__(self):
        self.sprite = GestorRecursos.CargarImagen('mesa cafe/mesa.png', -1)
        self.sprite = pygame.transform.scale(self.sprite, (132, 132))
        self.rect = self.sprite.get_rect()
        self.posicionX = 550
        self.posicionY = 250

        self.rect.right = self.posicionX
        self.rect.top = self.posicionY

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)