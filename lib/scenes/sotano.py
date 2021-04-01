from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import Jugador
from lib.sprites.actores.enemigo.enemigoSeguidor import Fantasma
from lib.sprites.sprite import MiSprite
from lib.gestorRecursos import GestorRecursos
from lib.sprites.recolectables.basura import *
from lib.sprites.recolectables.powerups.speedUp import *
from lib.ui.puntos import *
from lib.ui.temporizador import * 

BLANCO = (255,255,255)

class Sotano(EscenaPygame):

    def __init__(self,director):

        EscenaPygame.__init__(self,director)

        #Fondo de la escena
        self.suelo = GestorRecursos.CargarImagen('escenas/sotano/suelo.png',-1)
        self.suelo = pygame.transform.scale(self.suelo,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.suelo = self.suelo.convert_alpha()
        self.suelo.set_alpha(None)

        #Obstáculos
        self.obstaculos = GestorRecursos.CargarImagen('escenas/sotano/obstaculos.png', -1)
        self.obstaculos = pygame.transform.scale(self.obstaculos,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.obstaculos.set_colorkey(self.obstaculos.get_at((340, 430)), RLEACCEL)

        #Máscara
        self.mascaraImg = GestorRecursos.CargarImagen('escenas/sotano/mask.png', -1)
        self.mascaraImg.set_colorkey(self.mascaraImg.get_at((340, 430)), RLEACCEL)
        self.mascaraCol = pygame.mask.from_surface(self.mascaraImg)

        #Jugador
        self.jugador = director.jugador
        self.jugador.establecerPosicion((600,570))

        #fantasma
        self.fantasma = Fantasma(self.jugador)
        self.fantasma.establecerPosicion((300,400))

        self.grupoEnemigos = pygame.sprite.Group(self.fantasma)

        self.grupoJugadores = pygame.sprite.Group(self.jugador)
        

        self.numBasuras, self.basuras = iniBasuras(8, 4, 2)
        self.fSpawn = 60
        self.gestorbasura = GestorBasura(self.numBasuras, self.fSpawn, (1, 3), self.mascaraCol, self.basuras, (ANCHO_PANTALLA, ALTO_PANTALLA))
        self.grupoBasuras = pygame.sprite.Group(self.basuras)

        self.simultaneouslyThunders = 1
        self.thunder = Thunder()
        self.thunderGestor = ThunderGestor(self.simultaneouslyThunders, 1, self.mascaraCol, self.thunder, (ANCHO_PANTALLA, ALTO_PANTALLA))
        self.grupoThunders = pygame.sprite.Group(self.thunder)

        self.marcadorPuntuacion = Puntos(None,(50,30))  
        self.marcadorTiempo = Temporizador(None, (500,30), 60)
        pygame.display.update()

        pygame.display.update()

    def update(self,tiempo):

        self.fantasma.update(tiempo, self.grupoJugadores)

        self.gestorbasura.update(tiempo,self.mascaraCol, self.basuras, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.thunderGestor.update(tiempo, self.mascaraCol, self.thunder, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.grupoJugadores.update(tiempo,self.mascaraCol, self.grupoBasuras, self.grupoThunders)
        
        
        self.marcadorPuntuacion.update(tiempo, self.jugador)
        self.marcadorTiempo.update(tiempo)

    def eventos(self,listaEventos):
        for event in listaEventos:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                self.salirPrograma()
        
        teclasPulsadas = pygame.key.get_pressed()
        self.jugador.mover(teclasPulsadas, K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.fantasma.mover_cpu()


    def dibujar(self,pantalla):

        pantalla.blit(self.suelo,self.suelo.get_rect())
        
        for basura in self.basuras:
            basura.dibujar(pantalla)

        self.thunder.dibujar(pantalla)

        self.grupoJugadores.draw(pantalla)

        
        pantalla.blit(self.obstaculos,self.obstaculos.get_rect())


        self.grupoEnemigos.draw(pantalla)

        self.marcadorPuntuacion.dibujar(pantalla)
        self.marcadorTiempo.dibujar(pantalla)

        pygame.display.update()


    def salirPrograma(self):
        self.director.salirPrograma()
