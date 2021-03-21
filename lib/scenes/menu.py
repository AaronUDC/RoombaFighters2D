# -*- encoding: utf-8 -*-

import pygame
# import pyganim
from pygame.locals import *
from lib.escena import *
from lib.scenes.salon import Salon
from lib.scenes.test import Test
from lib.gestorRecursos import *

# Elementos UI, luego lo pondré en clases separadas
class ElementoGUI:
    def __init__(self, pantalla, rectangulo):
        self.pantalla = pantalla
        self.rect = rectangulo

    def establecerPosicion(self, posicion):
        (posicionx, posiciony) = posicion
        self.rect.left = posicionx
        self.rect.bottom = posiciony

    def posicionEnElemento(self, posicion):
        (posicionx, posiciony) = posicion
        if (posicionx>=self.rect.left) and (posicionx<=self.rect.right) and (posiciony>=self.rect.top) and (posiciony<=self.rect.bottom):
            return True
        else:
            return False

    def dibujar(self):
        raise NotImplemented("Tiene que implementar el metodo dibujar.")
    def accion(self):
        raise NotImplemented("Tiene que implementar el metodo accion.")

class Boton(ElementoGUI):
    def __init__(self, pantalla, nombreImagen, posicion):
        # Se carga la imagen del boton
        self.hoja = GestorRecursos.CargarImagen(nombreImagen,-1)
        #self.imagen = pygame.transform.scale(self.imagen, (, 20))
        self.estadoMarcado = False
        
        self.imagenDesmarcado = self.hoja.subsurface(Rect(0,0,self.hoja.get_width(),self.hoja.get_height()/2))
        self.imagenMarcado = self.hoja.subsurface(Rect(0,self.hoja.get_height()/2,self.hoja.get_width(),self.hoja.get_height()/2))

        # Se llama al método de la clase padre con el rectángulo que ocupa el botón
        ElementoGUI.__init__(self, pantalla, self.imagenDesmarcado.get_rect())
        # Se coloca el rectangulo en su posicion
        self.establecerPosicion(posicion)
    def dibujar(self, pantalla):
        if self.estadoMarcado:
            pantalla.blit(self.imagenMarcado, self.rect)
        else: 
            pantalla.blit(self.imagenDesmarcado, self.rect)

    def update(self, posRaton):
        if self.rect.collidepoint(posRaton):
            self.estadoMarcado = True
        else:
            self.estadoMarcado = False
        

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

class TextoGUI(ElementoGUI):
    def __init__(self, pantalla, fuente, color, texto, posicion):
        # Se crea la imagen del texto
        self.imagen = fuente.render(texto, True, color)
        # Se llama al método de la clase padre con el rectángulo que ocupa el texto
        ElementoGUI.__init__(self, pantalla, self.imagen.get_rect())
        # Se coloca el rectangulo en su posicion
        self.establecerPosicion(posicion)
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)

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

class PantallaGUI:
    def __init__(self, menu, nombreImagen):
        self.menu = menu
        # Se carga la imagen de fondo
        self.imagen = GestorRecursos.CargarImagen(nombreImagen)
        self.imagen = pygame.transform.scale(self.imagen, (ANCHO_PANTALLA, ALTO_PANTALLA))

        self.logo = GestorRecursos.CargarImagen("gui/logo.png",-1)
        self.rectLogo = self.logo.get_rect()
        self.rectLogo.left = ANCHO_PANTALLA/2 - self.logo.get_width()/2
        self.rectLogo.bottom = 150
        # Se tiene una lista de elementos GUI
        self.elementosGUI = []
        # Se tiene una lista de animaciones
        self.animaciones = []

    def update(self,*args):
        return

    def eventos(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == MOUSEBUTTONDOWN:
                self.elementoClic = None
                for elemento in self.elementosGUI:
                    if elemento.posicionEnElemento(evento.pos):
                        self.elementoClic = elemento
            if evento.type == MOUSEBUTTONUP:
                for elemento in self.elementosGUI:
                    if elemento.posicionEnElemento(evento.pos):
                        if (elemento == self.elementoClic):
                            elemento.accion()

    def dibujar(self, pantalla):
        # Dibujamos primero la imagen de fondo
        pantalla.blit(self.imagen, self.imagen.get_rect())

        pantalla.blit(self.logo,self.rectLogo)
        # Después las animaciones
        for animacion in self.animaciones:
            animacion.dibujar(pantalla)
        # Después los botones
        for elemento in self.elementosGUI:
            elemento.dibujar(pantalla)

class PantallaInicialGUI(PantallaGUI):
    def __init__(self, menu):
        PantallaGUI.__init__(self, menu, 'gui/fondoSalon.png')
        
        # Creamos los botones y los metemos en la lista
        botonJugarFase1 = BotonJugarFase(self, Salon, (ANCHO_PANTALLA/2,ALTO_PANTALLA/2))
        botonSalir = BotonSalir(self,(ANCHO_PANTALLA/2,ALTO_PANTALLA/2+ 100))

        self.elementosGUI.append(botonJugarFase1)
        self.elementosGUI.append(botonSalir)

        # Creamos el texto y lo metemos en la lista
        textoJugar = TextoJugarFase(self, 'Jugar en el salón', Salon, (ANCHO_PANTALLA/2+ 10,ALTO_PANTALLA/2-10))
        textoSalir = TextoSalir(self, (ANCHO_PANTALLA/2+ 10 ,ALTO_PANTALLA/2 + 90))
        self.elementosGUI.append(textoJugar)
        self.elementosGUI.append(textoSalir)

    def update(self,*args):
        x, y = pygame.mouse.get_pos()
        for boton in self.elementosGUI:
            if isinstance(boton, Boton):
                boton.update((x,y))


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
