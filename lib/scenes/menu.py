# -*- encoding: utf-8 -*-

import pygame
# import pyganim
from pygame.locals import *
from lib.escena import *
from lib.scenes.salon import Salon
from lib.gestorRecursos import *
from lib.ui.ui import *
from lib.ui.pantallaGUI import * 
from lib.scenes.cocina import Cocina
from lib.scenes.sotano import Sotano

class BotonJugarFase(Boton):
    def __init__(self, pantalla, fase, posicion):
        Boton.__init__(self, pantalla, 'gui/botonGUI.png', posicion)
        self.fase = fase
    def accion(self):
        self.pantalla.menu.ejecutarJuego(self.fase)

class BotonSalir(Boton):
    def __init__(self, pantalla, posicion):
        Boton.__init__(self, pantalla, 'gui/botonGUI.png', posicion)
    def accion(self):
        self.pantalla.menu.salirPrograma()

# -------------------------------------------------
# Clase TextoGUI y los distintos textos
class TextoJugarFase(TextoGUI):
    def __init__(self, pantalla, texto, fase, posicion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 16);
        TextoGUI.__init__(self, pantalla, fuente, (0, 0, 0), texto,  posicion)
        self.fase = fase
    def accion(self):
        self.pantalla.menu.ejecutarJuego(self.fase)

class TextoSalir(TextoGUI):
    def __init__(self, pantalla, posicion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 16);
        TextoGUI.__init__(self, pantalla, fuente, (0, 0, 0), 'Salir', posicion)
    def accion(self):
        self.pantalla.menu.salirPrograma()

# -------------------------------------------------
# Clase PantallaGUI y las distintas pantallas


class PantallaInicialGUI(PantallaGUI):
    def __init__(self, menu):
        PantallaGUI.__init__(self, menu, 'gui/fondoSalon.png')
        musica = GestorRecursos.CargarMusica("main_themes/main_theme.mp3")
        pygame.mixer.music.play(-1)
        self.logo = GestorRecursos.CargarImagen("gui/Logo.png",-1)
        self.rectLogo = self.logo.get_rect()
        self.rectLogo.left = ANCHO_PANTALLA/2 - self.logo.get_width()/2
        self.rectLogo.bottom = 200

        # Creamos los botones y los metemos en la lista
        botonJugarFase1 = BotonJugarFase(self, Salon, (ANCHO_PANTALLA/2,ALTO_PANTALLA/2))
        botonSalir = BotonSalir(self,(ANCHO_PANTALLA/2,ALTO_PANTALLA/2+ 50))

        self.elementosGUI.append(botonJugarFase1)
        self.elementosGUI.append(botonSalir)

        # Creamos el texto y lo metemos en la lista
        textoJugar = TextoJugarFase(self, 'Limpiar la casa', Salon, (ANCHO_PANTALLA/2+ 10,ALTO_PANTALLA/2-10))
        textoSalir = TextoSalir(self, (ANCHO_PANTALLA/2+ 10 ,ALTO_PANTALLA/2 + 40))
        self.elementosGUI.append(textoJugar)
        self.elementosGUI.append(textoSalir)

    def update(self,*args):
        x, y = pygame.mouse.get_pos()
        for boton in self.elementosGUI:
            if isinstance(boton, Boton):
                boton.update((x,y))

    def dibujar(self,pantalla):
        PantallaGUI.dibujar(self,pantalla)
        
        pantalla.blit(self.logo,self.rectLogo)


# -------------------------------------------------
# Clase MenuPygame, la escena en sí, en Pygame

class Menu(EscenaPygame):

    def __init__(self, director):
        # Llamamos al constructor de la clase padre
        EscenaPygame.__init__(self, director);
        # Creamos la lista de pantallas
        self.listaPantallas = []
        # Creamos las pantallas que vamos a tener
        #   y las metemos en la lista
        self.listaPantallas.append(PantallaInicialGUI(self))
        # En que pantalla estamos actualmente
        self.mostrarPantallaInicial()

    def update(self, *args):
        self.listaPantallas[self.pantallaActual].update(*args)
        return

    def eventos(self, lista_eventos):
        # Se mira si se quiere salir de esta escena
        for evento in lista_eventos:
            # Si se quiere salir, se le indica al director
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    self.salirPrograma()
            elif evento.type == pygame.QUIT:
                self.director.salirPrograma()

        # Se pasa la lista de eventos a la pantalla actual
        self.listaPantallas[self.pantallaActual].eventos(lista_eventos)

    def dibujar(self, pantalla):
        self.listaPantallas[self.pantallaActual].dibujar(pantalla)

    #--------------------------------------
    # Metodos propios del menu

    def salirPrograma(self):
        self.director.salirPrograma()

    def ejecutarJuego(self, nivel):
        # Creamos la escena con la animacion antes de jugar
        pantalla = nivel(self.director)
        self.director.apilarEscena(pantalla)

    def mostrarPantallaInicial(self):
        self.pantallaActual = 0

    #def mostrarPantallaConfiguracion(self):
    #   self.pantallaActual = ...
