from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import Jugador
from lib.sprites.actores.enemigo.torreta import Gato
from lib.sprites.actores.enemigo.bala import Pelo
from lib.sprites.sprite import MiSprite
from lib.gestorRecursos import GestorRecursos
from lib.gestorRecolectables import GestorRecolectables
from lib.gestorRecolectables import GestorBasuraR
from lib.gestorRecolectables import GestorThunder
from lib.gestorRecolectables import GestorShield
from lib.gestorRecolectables import GestorWrenches
from lib.sprites.recolectables.powerups.speedUp import *
from lib.sprites.recolectables.powerups.lifeUp import *
from lib.sprites.recolectables.powerups.shieldUp import *
from lib.ui.puntos import *
from lib.ui.temporizador import * 
from lib.scenes.cocina import *

BLANCO = (255,255,255)

class Salon(EscenaPygame):

    def __init__(self,director):

        EscenaPygame.__init__(self,director)


        #Fondo de la escena
        self.suelo = GestorRecursos.CargarImagen('escenas/salon/suelo.png',-1)
        self.suelo = pygame.transform.scale(self.suelo,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.suelo = self.suelo.convert_alpha()
        self.suelo.set_alpha(None)

        #Obstáculos
        self.obstaculos = GestorRecursos.CargarImagen('escenas/salon/obstaculos.png', -1)
        self.obstaculos = pygame.transform.scale(self.obstaculos,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.obstaculos.set_colorkey(self.obstaculos.get_at((340, 430)), RLEACCEL)

        #Máscara
        self.mascaraImg = GestorRecursos.CargarImagen('escenas/salon/mask.png', -1)
        self.mascaraImg.set_colorkey(self.mascaraImg.get_at((340, 430)), RLEACCEL)
        self.mascaraCol = pygame.mask.from_surface(self.mascaraImg)

        #Jugador
        self.jugador = director.jugador
        self.jugador.establecerPosicion((600,570))

        posicionGato = (360,310)
        self.bala = Pelo(posicionGato)

        self.gato = Gato(self.bala,Rect(160,160,384,288))
        (posX,posY) = posicionGato
        self.gato.establecerPosicion((posX-self.gato.rect.width/2,posY+self.gato.rect.height/2))

        self.grupoJugadores = pygame.sprite.Group(self.jugador)
        self.grupoTorretas= pygame.sprite.Group(self.gato)

        #Basura
        self.numBasuras, self.basuras = GestorRecolectables.iniBasuras(10, 10, 10)
        self.fSpawn = 60
        self.gestorbasura = GestorBasuraR(self.numBasuras, self.fSpawn, (1, 3), self.basuras, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoBasuras = pygame.sprite.Group(self.basuras)

        #PowerUps
        self.simultaneouslyThunders = 1
        self.thunder = [Thunder()]
        self.thunderGestor = GestorThunder(self.simultaneouslyThunders, self.fSpawn, (1, 3), self.thunder, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoThunders = pygame.sprite.Group(self.thunder)

        self.simultaneouslyWrenches = 1
        self.wrench = [Wrench()]
        self.wrenchGestor = GestorWrenches(self.simultaneouslyThunders, self.fSpawn, (1, 3), self.wrench, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoWrenches = pygame.sprite.Group(self.wrench)

        self.simultaneouslyShields = 1
        self.shield = [Shield()]
        self.shieldGestor = GestorShield(self.simultaneouslyShields, self.fSpawn, (1, 3), self.shield, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoShields = pygame.sprite.Group(self.shield)

        self.marcadorPuntuacion = Puntos(None,(50,30))
        self.marcadorTiempo = Temporizador(None, (500,30), 50)
        pygame.display.update()

    def update(self,tiempo):

        self.gestorbasura.update(tiempo,self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.basuras)
        self.thunderGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.thunder)

        self.grupoBasuras.update(tiempo,self.grupoJugadores)
        self.grupoThunders.update(tiempo, self.grupoJugadores)
        self.grupoShields.update(tiempo, self.grupoJugadores)
        self.grupoWrenches.update(tiempo, self.grupoJugadores)

        self.bala.update(tiempo,self.grupoJugadores)
        self.grupoTorretas.update(tiempo,self.grupoJugadores)

        self.wrenchGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.wrench)
        self.shieldGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.shield)

        self.grupoJugadores.update(tiempo,self.mascaraCol, self.grupoBasuras,self.thunder,self.wrench,self.shield)

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

        self.thunder[0].dibujar(pantalla)
        self.wrench[0].dibujar(pantalla)
        self.shield[0].dibujar(pantalla)

        self.grupoJugadores.draw(pantalla)

        
        pantalla.blit(self.obstaculos,self.obstaculos.get_rect())
        self.grupoJugadores.draw(pantalla)
        self.bala.draw(pantalla)
        self.grupoTorretas.draw(pantalla)

        
        self.marcadorPuntuacion.dibujar(pantalla)
        self.marcadorTiempo.dibujar(pantalla)
        pygame.display.update()

    def cambiarScena(self, scenes):
        if self.marcadorPuntuacion == 10:
            if self.marcadorTiempo == 50:
                self.apilarEscena(Cocina)


    def salirPrograma(self):
        self.director.salirPrograma()
