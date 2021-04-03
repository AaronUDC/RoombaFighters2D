import pygame
# import pyganim
from pygame.locals import *
from lib.escena import *
from lib.gestorRecursos import *
from lib.ui.ui import *
from lib.ui.pantallaGUI import PantallaGUI

class BotonRestartFase(Boton):
    def __init__(self, pantalla, posicion):
        Boton.__init__(self, pantalla, 'gui/botonGUI.png', posicion)

    def accion(self):
        self.pantalla.menu.restartFase()

class BotonVolverMenu(Boton):
    def __init__(self, pantalla, posicion):
        Boton.__init__(self, pantalla, 'gui/botonGUI.png', posicion)

    def accion(self):
        self.pantalla.menu.volverAlMenu()

class BotonSalir(Boton):
    def __init__(self, pantalla, posicion):
        Boton.__init__(self, pantalla, 'gui/botonGUI.png', posicion)

    def accion(self):
        self.pantalla.menu.salirPrograma()

class TextoRestartFase(TextoGUI):
    def __init__(self, pantalla, posicion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 16);
        TextoGUI.__init__(self, pantalla, fuente, (0, 0, 0), "Volver a intentarlo",  posicion)

    def accion(self):
        self.pantalla.menu.restartFase()

class TextoVolverMenu(TextoGUI):
    def __init__(self, pantalla, posicion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 16);
        TextoGUI.__init__(self, pantalla, fuente, (0, 0, 0), "Volver al menú",  posicion)

    def accion(self):
        self.pantalla.menu.volverAlMenu()

class TextoSalir(TextoGUI):
    def __init__(self, pantalla, posicion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 16);
        TextoGUI.__init__(self, pantalla, fuente, (0, 0, 0), "Salir del juego",  posicion)

    def accion(self):
        self.pantalla.menu.salirPrograma()

class TextoPuntuacionTitulo(TextoGUI):

    def __init__(self, pantalla, posicion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 30);
        TextoGUI.__init__(self, pantalla, fuente, (0, 0, 0), "Tu puntuación",  posicion)

    def accion(self):
        return

class TextoPuntuacion(TextoGUI):

    def __init__(self, pantalla, posicion, puntuacion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 25);
        TextoGUI.__init__(self, pantalla, fuente, (0, 0, 0), str(puntuacion),  posicion)

    def accion(self):
        return

class TextoGameOver(TextoGUI):

    def __init__(self, pantalla, posicion):
        # La fuente la debería cargar el estor de recursos
        fuente = pygame.font.Font('fuenteMenu.ttf', 50);
        TextoGUI.__init__(self, pantalla, fuente, (200, 0, 0), 'GAME OVER',  posicion)

    def accion(self):
        return



class PantallaGameOverSalon(PantallaGUI):
    
    def __init__(self, menu):
        PantallaGUI.__init__(self, menu, 'gui/fondoSalon.png')
        
        # Creamos los botones y los metemos en la lista
        botonRejugar = BotonVolverMenu(self, (ANCHO_PANTALLA/2,ALTO_PANTALLA/2))
        botonMenu = BotonVolverMenu(self,(ANCHO_PANTALLA/2,ALTO_PANTALLA/2+ 50))
        botonSalir = BotonSalir(self,(ANCHO_PANTALLA/2,ALTO_PANTALLA/2+ 100))

        self.elementosGUI.append(botonRejugar)
        self.elementosGUI.append(botonMenu)
        self.elementosGUI.append(botonSalir)

        # Creamos el texto y lo metemos en la lista
        textoRejugar = TextoRestartFase(self, (ANCHO_PANTALLA/2+ 10,ALTO_PANTALLA/2-10))
        textoMenu = TextoVolverMenu(self, (ANCHO_PANTALLA/2+ 10 ,ALTO_PANTALLA/2 + 40))
        textoSalir = TextoSalir(self, (ANCHO_PANTALLA/2+ 10 ,ALTO_PANTALLA/2 + 90))

        self.elementosGUI.append(textoRejugar)
        self.elementosGUI.append(textoMenu)
        self.elementosGUI.append(textoSalir)

        tituloPuntuacion = TextoPuntuacionTitulo(self, (100, 400))
        puntuacion = TextoPuntuacion(self, (100, 430), menu.director.jugador.puntuacion)
        self.elementosGUI.append(tituloPuntuacion)
        self.elementosGUI.append(puntuacion)

        textoGameOver = TextoGameOver(self,(ANCHO_PANTALLA/3, 100))
        self.elementosGUI.append(textoGameOver)

        
    
    def update(self,*args):
        x, y = pygame.mouse.get_pos()
        for boton in self.elementosGUI:
            if isinstance(boton, Boton):
                boton.update((x,y))
    
    def dibujar(self,pantalla):
        PantallaGUI.dibujar(self,pantalla)


class PantallaGameOverCocina(PantallaGUI):

    def __init__(self, menu):
        PantallaGUI.__init__(self, menu, 'gui/fondoCocina.png')

        # Creamos los botones y los metemos en la lista
        botonRejugar = BotonVolverMenu(self, (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2))
        botonMenu = BotonVolverMenu(self, (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2 + 50))
        botonSalir = BotonSalir(self, (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2 + 100))

        self.elementosGUI.append(botonRejugar)
        self.elementosGUI.append(botonMenu)
        self.elementosGUI.append(botonSalir)

        # Creamos el texto y lo metemos en la lista
        textoRejugar = TextoRestartFase(self, (ANCHO_PANTALLA / 2 + 10, ALTO_PANTALLA / 2 - 10))
        textoMenu = TextoVolverMenu(self, (ANCHO_PANTALLA / 2 + 10, ALTO_PANTALLA / 2 + 40))
        textoSalir = TextoSalir(self, (ANCHO_PANTALLA / 2 + 10, ALTO_PANTALLA / 2 + 90))

        self.elementosGUI.append(textoRejugar)
        self.elementosGUI.append(textoMenu)
        self.elementosGUI.append(textoSalir)

        tituloPuntuacion = TextoPuntuacionTitulo(self, (100, 400))
        puntuacion = TextoPuntuacion(self, (100, 430), menu.director.jugador.puntuacion)
        self.elementosGUI.append(tituloPuntuacion)
        self.elementosGUI.append(puntuacion)

        textoGameOver = TextoGameOver(self, (ANCHO_PANTALLA / 3, 100))
        self.elementosGUI.append(textoGameOver)

    def update(self, *args):
        x, y = pygame.mouse.get_pos()
        for boton in self.elementosGUI:
            if isinstance(boton, Boton):
                boton.update((x, y))

    def dibujar(self, pantalla):
        PantallaGUI.dibujar(self, pantalla)


class PantallaGameOverSotano(PantallaGUI):

    def __init__(self, menu):
        PantallaGUI.__init__(self, menu, 'gui/fondoSotano.png')

        # Creamos los botones y los metemos en la lista
        botonRejugar = BotonVolverMenu(self, (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2))
        botonMenu = BotonVolverMenu(self, (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2 + 50))
        botonSalir = BotonSalir(self, (ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2 + 100))

        self.elementosGUI.append(botonRejugar)
        self.elementosGUI.append(botonMenu)
        self.elementosGUI.append(botonSalir)

        # Creamos el texto y lo metemos en la lista
        textoRejugar = TextoRestartFase(self, (ANCHO_PANTALLA / 2 + 10, ALTO_PANTALLA / 2 - 10))
        textoMenu = TextoVolverMenu(self, (ANCHO_PANTALLA / 2 + 10, ALTO_PANTALLA / 2 + 40))
        textoSalir = TextoSalir(self, (ANCHO_PANTALLA / 2 + 10, ALTO_PANTALLA / 2 + 90))

        self.elementosGUI.append(textoRejugar)
        self.elementosGUI.append(textoMenu)
        self.elementosGUI.append(textoSalir)

        tituloPuntuacion = TextoPuntuacionTitulo(self, (100, 400))
        puntuacion = TextoPuntuacion(self, (100, 430), menu.director.jugador.puntuacion)
        self.elementosGUI.append(tituloPuntuacion)
        self.elementosGUI.append(puntuacion)

        textoGameOver = TextoGameOver(self, (ANCHO_PANTALLA / 3, 100))
        self.elementosGUI.append(textoGameOver)

    def update(self, *args):
        x, y = pygame.mouse.get_pos()
        for boton in self.elementosGUI:
            if isinstance(boton, Boton):
                boton.update((x, y))

    def dibujar(self, pantalla):
        PantallaGUI.dibujar(self, pantalla)

class GameOver(EscenaPygame):

    def __init__(self, director,fondo):
        # Llamamos al constructor de la clase padre
        EscenaPygame.__init__(self, director);
        # Creamos la lista de pantallas
        self.listaPantallas = []
        # Creamos las pantallas que vamos a tener
        #   y las metemos en la lista
        if fondo == "salon":
            self.listaPantallas.append(PantallaGameOverSalon(self))
        elif fondo == "sotano":
            self.listaPantallas.append(PantallaGameOverSotano(self))
        elif fondo == "cocina":
            self.listaPantallas.append(PantallaGameOverCocina(self))
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

    def mostrarPantallaInicial(self):
        self.pantallaActual = 0

    def dibujar(self, pantalla):
        self.listaPantallas[self.pantallaActual].dibujar(pantalla)

    def volverAlMenu(self):
        self.director.resetJugador()
        self.director.volverAlMenu()

    def restartFase(self):
        self.director.resetPuntuacionAAnterior()
        self.director.resetVidaJugador()
        self.director.salirEscena()

    def salirPrograma(self):
        self.director.salirPrograma()
