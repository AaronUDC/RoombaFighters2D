# -*- encoding: utf-8 -*-

import pyglet
from pygame.locals import *
from lib.escena import *
from lib.sprites.sprite import *


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
