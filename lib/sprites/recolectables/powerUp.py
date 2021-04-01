import pygame, sys, os, math, random
from pygame.locals import *
from lib.gestorRecursos import *
from lib.sprites.recolectables.recolectables import Recolectable
from lib.sprites.actores.jugador import Jugador


class PowerUp(Recolectable):

    def __init__(self, tipo, tiempoPowerUp):
        Recolectable.__init__(self,  "recolectables/powerups/powerUps.png", "recolectables/powerups/coordPowerUps.txt", [2,0,0], tipo)
        self.mask = pygame.mask.from_surface(self.image)
        self.tiempoPowerUp = tiempoPowerUp

    def update(tiempo, jugadores, powerUp):
        #Llamamos al metodo de ganar un powerUp del jugador
        Recolectable.update(self,tiempo,jugadores, 0.3,Jugador.obtenerPowerUp, powerUp, self.tiempoPowerUp)

class SpeedUp(PowerUp):

    def __init__(self):
        PowerUp.__init__(self, 0, 10)

    def update(tiempo, jugadores): 
        #Le pasamos el powerUp concreto
        PowerUp.update(self, tiempo, jugadores, None)

class ShieldUp(PowerUp):

    def __init__(self):
        PowerUp.__init__(self, 1, 20)

    def update(tiempo,jugadores):
        #Le pasamos el powerUp concreto
        PowerUp.update(self, tiempo, jugadores, None)






