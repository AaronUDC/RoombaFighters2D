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
from lib.sprites.recolectables.lifeUp import *
from lib.sprites.recolectables.powerUp import *
from lib.sprites.recolectables.basura import *
from lib.ui.gameHUD import * 
from lib.scenes.sotano import *
from lib.scenes.gameOver import GameOver

BLANCO = (255,255,255)

class Salon(EscenaPygame):

    def __init__(self,director):

        EscenaPygame.__init__(self,director)
        
        director.guardarPuntuacionAnterior()

        #Fondo de la escena
        musica = GestorRecursos.CargarMusica("main_themes/salon_theme.mp3")
        pygame.mixer.music.play(-1)
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
        self.jugador.origen = (600,570)

        posicionGato = (360,310)
        self.bala = Pelo(posicionGato)

        self.gato = Gato(self.bala,Rect(160,160,384,288))
        (posX,posY) = posicionGato
        self.gato.establecerPosicion((posX-self.gato.rect.width/2,posY+self.gato.rect.height/2))

        self.grupoJugadores = pygame.sprite.Group(self.jugador)
        self.grupoTorretas= pygame.sprite.Group(self.gato)

        #Recolectables
        self.numBasuras, self.basuras = GestorRecolectables.iniBasuras(15, 10, 5)
        self.gestorbasura = GestorBasuraR(self.numBasuras, 5, (6, 10), self.basuras, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoBasuras = pygame.sprite.Group(self.basuras)

        #PowerUps
        self.simultaneouslyThunders = 1
        self.thunder = [SpeedUp()]
        self.thunderGestor = GestorThunder(self.simultaneouslyThunders, 25, (1, 3), self.thunder, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoThunders = pygame.sprite.Group(self.thunder)

        self.simultaneouslyWrenches = 1
        self.wrench = [Wrench()]
        self.wrenchGestor = GestorWrenches(self.simultaneouslyThunders, 20, (1, 3), self.wrench, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoWrenches = pygame.sprite.Group(self.wrench)

        self.simultaneouslyShields = 1
        self.shield = [ShieldUp()]
        self.shieldGestor = GestorShield(self.simultaneouslyShields, 25, (1, 3), self.shield, (ANCHO_PANTALLA, ALTO_PANTALLA), self.mascaraCol)
        self.grupoShields = pygame.sprite.Group(self.shield)


        self.marcadorPuntuacion = Puntos((0,0,0),None,(50,30))
        self.marcadorTiempo = Temporizador((0,0,0),None, (500,30), 60)
        pygame.display.update()

    def update(self,tiempo):
        self.bala.update(tiempo,self.grupoJugadores)
        self.grupoTorretas.update(tiempo,self.grupoJugadores)

        self.gestorbasura.update(tiempo,self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.basuras)
        self.thunderGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.thunder)
        self.wrenchGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.wrench)
        self.shieldGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.shield)

        self.grupoBasuras.update(tiempo,self.grupoJugadores)
        self.grupoThunders.update(tiempo, self.grupoJugadores)
        self.grupoShields.update(tiempo, self.grupoJugadores)
        self.grupoWrenches.update(tiempo, self.grupoJugadores)

        self.grupoJugadores.update(tiempo,self.mascaraCol)

        self.marcadorPuntuacion.update(tiempo, self.jugador)
        self.marcadorTiempo.update(tiempo)

        if self.marcadorTiempo.tiempoLimite < 0:
            pantalla = Sotano(self.director)
            self.director.cambiarEscena(pantalla)
            

        if self.jugador.vida <= 0:
            pantalla = GameOver(self.director,"salon")
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
