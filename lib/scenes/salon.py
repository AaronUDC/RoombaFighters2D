from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import Jugador
from lib.sprites.actores.enemigo.gato import Gato
from lib.sprites.actores.enemigo.bala import Bala
from lib.sprites.sprite import MiSprite
from lib.gestorRecursos import GestorRecursos
from lib.sprites.props.basura import *
from lib.sprites.recolectables.powerups.speedUp import *

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


        self.mascaraImg = GestorRecursos.CargarImagen('salon/mask.png', -1)
        self.mascaraImg.set_colorkey(self.mascaraImg.get_at((340, 430)), RLEACCEL)


        self.mascaraCol = pygame.mask.from_surface(self.mascaraImg)

        self.jugador = Jugador()
        self.jugador.establecerPosicion((150,150))

        self.bala = Bala()
        self.bala.establecerPosicion((450, 350))

        self.gato = Gato()
        self.gato.establecerPosicion((400, 400))

        self.grupoJugadores = pygame.sprite.Group(self.jugador)
        self.grupoEnemigos = pygame.sprite.Group(self.bala)
        self.grupoEnemigos.add(self.gato)

        self.numBasuras, self.basuras = iniBasuras(8, 4, 2)
        self.fSpawn = 60
        self.gestorbasura = GestorBasura(self.numBasuras, self.fSpawn, (1, 3), self.mascaraCol, self.basuras, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.grupoBasuras = pygame.sprite.Group(self.basuras)

        self.thunder = Thunder(0)
        self.simultaneouslyThunders = 1
        self.thunderGestor = ThunderGestor(self.simultaneouslyThunders, 60, self.mascaraCol, self.thunder, (ANCHO_PANTALLA,ALTO_PANTALLA))

        pygame.display.update()

    def update(self,tiempo):

        self.gestorbasura.update(tiempo,self.mascaraCol, self.basuras, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.thunderGestor.update(tiempo, self.mascaraCol, self.thunder, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.grupoJugadores.update(tiempo,self.mascaraCol, self.grupoBasuras, self.thunderGestor)

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

        self.thunder.dibujar(pantalla) #???

        self.grupoJugadores.draw(pantalla)
        self.grupoEnemigos.draw(pantalla)

        
        pantalla.blit(self.obstaculos,self.obstaculos.get_rect())
        pygame.display.update()


    def salirPrograma(self):
        self.director.salirPrograma()
