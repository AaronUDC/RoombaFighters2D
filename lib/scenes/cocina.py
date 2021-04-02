from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import Jugador
from lib.sprites.actores.enemigo.enemigoSeguidor import Loro
from lib.sprites.sprite import MiSprite
from lib.gestorRecursos import GestorRecursos
from lib.gestorRecolectables import GestorRecolectables
from lib.gestorRecolectables import GestorBasuraR
from lib.gestorRecolectables import GestorThunder
from lib.gestorRecolectables import GestorShield
from lib.gestorRecolectables import GestorWrenches
from lib.sprites.actores.enemigo.torreta import Bebe
from lib.sprites.actores.enemigo.bala import Vomito
from lib.sprites.recolectables.basura import *
from lib.sprites.recolectables.powerups.speedUp import *
from lib.sprites.recolectables.powerups.lifeUp import *
from lib.sprites.recolectables.powerups.shieldUp import *
from lib.ui.puntos import *
from lib.scenes.sotano import *
from lib.ui.temporizador import * 

BLANCO = (255,255,255)

class Cocina(EscenaPygame):

    def __init__(self,director):

        EscenaPygame.__init__(self,director)

        #Fondo de la escena
        self.suelo = GestorRecursos.CargarImagen('escenas/cocina/suelo.png',-1)
        self.suelo = pygame.transform.scale(self.suelo,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.suelo = self.suelo.convert_alpha()
        self.suelo.set_alpha(None)

        #Obstáculos
        self.obstaculos = GestorRecursos.CargarImagen('escenas/cocina/obstaculos.png', -1)
        self.obstaculos = pygame.transform.scale(self.obstaculos,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.obstaculos.set_colorkey(self.obstaculos.get_at((340, 430)), RLEACCEL)

        #Jaula
        self.jaula = GestorRecursos.CargarImagen('escenas/cocina/jaula.png', -1)
        self.jaulaRect = self.jaula.get_rect()
        self.jaulaRect.left = 518
        self.jaulaRect.top = 520

        #Silla
        self.silla = GestorRecursos.CargarImagen('escenas/cocina/Sillita.png', -1)
        self.sillaRect = self.jaula.get_rect()
        self.sillaRect.left = 700
        self.sillaRect.top = 290

        #Máscara
        self.mascaraImg = GestorRecursos.CargarImagen('escenas/cocina/mask.png', -1)
        self.mascaraImg.set_colorkey(self.mascaraImg.get_at((340, 430)), RLEACCEL)
        self.mascaraCol = pygame.mask.from_surface(self.mascaraImg)

        #Jugador
        self.jugador = director.jugador
        self.jugador.establecerPosicion((188,138))

        self.grupoJugadores = pygame.sprite.Group(self.jugador)

        #Enemigos

        #lo que lanza el bebe
        self.bala = Vomito((700, 350))
        self.bala.establecerPosicion((700, 350))
        #cambiar posicion del bebe
        self.bebe = Bebe(self.bala,Rect(544,128,224,384))
        self.bebe.establecerPosicion((700, 350))

        self.grupoEnemigos = pygame.sprite.Group(self.bebe)

        #Loro
        posicionJaula = (530,590)
        self.loro = Loro(self.jugador,posicionJaula, 5, 17, 20)
        self.loro.establecerPosicion(posicionJaula)

        self.grupoEnemigosVoladores = pygame.sprite.Group(self.loro)

        #Recolectables
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
        self.marcadorTiempo = Temporizador(None, (500,30), 60)
        pygame.display.update()

    def update(self,tiempo):

        self.loro.update(tiempo,self.grupoJugadores)
        
        self.gestorbasura.update(tiempo,self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.basuras)
        self.thunderGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA),self.thunder)
        self.wrenchGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA, ALTO_PANTALLA), self.wrench)
        self.shieldGestor.update(tiempo, self.mascaraCol, (ANCHO_PANTALLA,ALTO_PANTALLA), self.shield)
        self.grupoBasuras.update(tiempo,self.grupoJugadores)
        self.grupoThunders.update(tiempo, self.grupoJugadores)
        self.grupoShields.update(tiempo, self.grupoJugadores)
        self.grupoWrenches.update(tiempo, self.grupoJugadores)
        self.grupoJugadores.update(tiempo,self.mascaraCol, self.grupoBasuras, self.thunder,self.wrench,self.shield)
        self.bala.update(tiempo, self.grupoJugadores)
        self.bebe.update(tiempo, self.grupoJugadores)
        
        
        self.marcadorPuntuacion.update(tiempo, self.jugador)
        self.marcadorTiempo.update(tiempo)

        

    def eventos(self,listaEventos):
        for event in listaEventos:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                self.salirPrograma()
        
        teclasPulsadas = pygame.key.get_pressed()
        self.loro.mover_cpu()
        
        self.jugador.mover(teclasPulsadas, K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.bebe.mover_cpu(self.jugador)
        self.bala.mover_cpu(self.jugador)


    def dibujar(self,pantalla):

        pantalla.blit(self.suelo,self.suelo.get_rect())
        
        for basura in self.basuras:
            basura.dibujar(pantalla)

        self.thunder[0].dibujar(pantalla)
        self.wrench[0].dibujar(pantalla)
        self.shield[0].dibujar(pantalla)
        
        
        pantalla.blit(self.silla,self.sillaRect)

        self.grupoJugadores.draw(pantalla)

        self.bala.draw(pantalla)
        self.grupoEnemigos.draw(pantalla)

        pantalla.blit(self.obstaculos,self.obstaculos.get_rect())

        pantalla.blit(self.obstaculos,self.obstaculos.get_rect())
        
        self.loro.dibujar(pantalla)
        
        pantalla.blit(self.jaula,self.jaulaRect)
        self.marcadorPuntuacion.dibujar(pantalla)
        self.marcadorTiempo.dibujar(pantalla)
        pygame.display.update()


    def salirPrograma(self):
        self.director.salirPrograma()
