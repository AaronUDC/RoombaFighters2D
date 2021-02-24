# -*- coding: utf-8 -*-

# Importar modulos
from lib.director import Director
from lib.scenes.menu import Menu


if __name__ == '__main__':

    # Creamos el director
    director = Director()

    # Creamos la escena con el menu
    escena = Menu(director)
    
    # Le decimos al director que apile esta escena
    director.apilarEscena(escena)
    
    # Y ejecutamos el juego
    director.ejecutar()
