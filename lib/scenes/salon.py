from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import Jugador
from lib.sprites.actores.enemigo.gato import Gato
from lib.sprites.actores.enemigo.pelo import Pelo
from lib.sprites.actores.enemigo.bala import Bala
from lib.sprites.sprite import MiSprite
from lib.gestorRecursos import GestorRecursos
from lib.sprites.recolectables.basura import *
from lib.sprites.recolectables.powerups.speedUp import *
from lib.ui.puntos import *
from lib.ui.temporizador import * 
from lib.scenes.cocina import *

BLANCO = (255,255,255)

class Salon(EscenaPygame):

    def __init__(self,director):

        EscenaPygame.__init__(self,director)


        #Fondo de la escena
        self.suelo = GestorRecursos.CargarImagen('salon/suelo.png',-1)
        self.suelo = pygame.transform.scale(self.suelo,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.suelo = self.suelo.convert_alpha()
        self.suelo.set_alpha(None)

        #Obstáculos
        self.obstaculos = GestorRecursos.CargarImagen('salon/obstaculos.png', -1)
        self.obstaculos = pygame.transform.scale(self.obstaculos,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.obstaculos.set_colorkey(self.obstaculos.get_at((340, 430)), RLEACCEL)

        #Máscara
        self.mascaraImg = GestorRecursos.CargarImagen('salon/mask.png', -1)
        self.mascaraImg.set_colorkey(self.mascaraImg.get_at((340, 430)), RLEACCEL)
        self.mascaraCol = pygame.mask.from_surface(self.mascaraImg)

        #Jugador
        self.jugador = director.jugador
        self.jugador.establecerPosicion((600,570))

        self.bala = Pelo(360,310)
        self.bala.establecerPosicion((360, 310))

        self.gato = Gato()
        self.gato.establecerPosicion((300, 370))

        self.grupoJugadores = pygame.sprite.Group(self.jugador)
        self.grupoEnemigos = pygame.sprite.Group(self.bala)
        self.grupoEnemigos.add(self.gato)

        self.numBasuras, self.basuras = iniBasuras(8, 4, 2)
        self.fSpawn = 60
        self.gestorbasura = GestorBasura(self.numBasuras, self.fSpawn, (1, 3), self.mascaraCol, self.basuras, (ANCHO_PANTALLA, ALTO_PANTALLA))
        self.grupoBasuras = pygame.sprite.Group(self.basuras)

        self.simultaneouslyThunders = 1
        self.thunder = Thunder()
        self.thunderGestor = ThunderGestor(self.simultaneouslyThunders, 1, self.mascaraCol, self.thunder, (ANCHO_PANTALLA, ALTO_PANTALLA))
        self.grupoThunders = pygame.sprite.Group(self.thunder)

        self.marcadorPuntuacion = Puntos(None,(50,30))
        self.marcadorTiempo = Temporizador(None, (500,30), 5)
        pygame.display.update()

    def update(self,tiempo):

        self.gestorbasura.update(tiempo,self.mascaraCol, self.basuras, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.thunderGestor.update(tiempo, self.mascaraCol, self.thunder, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.grupoJugadores.update(tiempo,self.mascaraCol, self.grupoBasuras, self.grupoThunders,self.grupoEnemigos)
        self.grupoEnemigos.update(tiempo,self.mascaraCol)
        self.marcadorPuntuacion.update(tiempo, self.jugador)
        self.marcadorTiempo.update(tiempo)

        if self.marcadorTiempo.tiempoLimite < 0:
            pantalla = Cocina(self.director)
            self.director.apilarEscena(pantalla)
            


    def eventos(self,listaEventos):
        for event in listaEventos:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                self.salirPrograma()
        
        teclasPulsadas = pygame.key.get_pressed()
        self.jugador.mover(teclasPulsadas, K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.gato.mover_cpu(self.jugador)
        self.bala.mover_cpu(self.jugador)


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

    def cambiarScena(self, scenes):
        if self.marcadorPuntuacion == 10:
            if self.marcadorTiempo == 50:
                self.apilarEscena(Cocina)


    def salirPrograma(self):
        self.director.salirPrograma()
