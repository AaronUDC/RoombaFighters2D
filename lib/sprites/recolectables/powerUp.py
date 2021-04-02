import pygame, sys, os, math, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import Recolectable
from lib.sprites.actores.jugador import Jugador

SPEED_UP = 0
SHIELD_UP = 1

class PowerUp(Recolectable):

    def __init__(self, tipo, tiempoPowerUp):
        Recolectable.__init__(self,  "recolectables/powerups/powerUps.png", "recolectables/powerups/coordPowerUps.txt", [2,0,0], tipo)
        self.tiempoPowerUp = tiempoPowerUp

    def update(self,tiempo, jugadores, powerUp,sonido):
        #Llamamos al metodo de ganar un powerUp del jugador
        Recolectable.update(self,tiempo,jugadores, 0.3,Jugador.obtenerPowerUp, powerUp, self.tiempoPowerUp,sonido)

class SpeedUp(PowerUp):

    def __init__(self):
        PowerUp.__init__(self, SPEED_UP, 10)

    def update(self,tiempo, jugadores):
        #Le pasamos el powerUp concreto
        sonido =  GestorRecursos.CargarSonido("powerups/thunderEffect.mp3")
        PowerUp.update(self, tiempo, jugadores, 1,sonido)

class ShieldUp(PowerUp):

    def __init__(self):
        PowerUp.__init__(self, SHIELD_UP, 20)

    def update(self,tiempo,jugadores):
        #Le pasamos el powerUp concreto
        sonido =  GestorRecursos.CargarSonido("powerups/shieldEffect.mp3")
        PowerUp.update(self, tiempo, jugadores, 2,sonido)






