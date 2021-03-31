from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import Jugador
from lib.sprites.sprite import MiSprite
from lib.gestorRecursos import GestorRecursos
from lib.sprites.actores.enemigo.bebe import Bebe
from lib.sprites.actores.enemigo.vomito import Vomito
from lib.sprites.recolectables.basura import *
from lib.sprites.recolectables.powerups.speedUp import *
from lib.ui.puntos import *
from lib.scenes.sotano import *
from lib.ui.temporizador import * 

BLANCO = (255,255,255)

class Cocina(EscenaPygame):

    def __init__(self,director):

        EscenaPygame.__init__(self,director)

        #Fondo de la escena
        self.suelo = GestorRecursos.CargarImagen('cocina/suelo.png',-1)
        self.suelo = pygame.transform.scale(self.suelo,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.suelo = self.suelo.convert_alpha()
        self.suelo.set_alpha(None)

        #Obstáculos
        self.obstaculos = GestorRecursos.CargarImagen('cocina/obstaculos.png', -1)
        self.obstaculos = pygame.transform.scale(self.obstaculos,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.obstaculos.set_colorkey(self.obstaculos.get_at((340, 430)), RLEACCEL)

        #Silla
        self.silla = GestorRecursos.CargarImagen('cocina/Sillita.png', -1)
        self.silla = pygame.transform.scale(self.silla, (ANCHO_PANTALLA, ALTO_PANTALLA))
        self.silla.set_colorkey(self.silla.get_at((0, 0)), RLEACCEL)

        #Máscara
        self.mascaraImg = GestorRecursos.CargarImagen('cocina/mask.png', -1)
        self.mascaraImg.set_colorkey(self.mascaraImg.get_at((340, 430)), RLEACCEL)
        self.mascaraCol = pygame.mask.from_surface(self.mascaraImg)

        #Jugador
        self.jugador = director.jugador
        self.jugador.establecerPosicion((600,500))

    #lo que lanza el bebe
        self.bala = Vomito(725, 325)
        self.bala.establecerPosicion((700, 350))
    #cambiar posicion del bebe
        self.bebe = Bebe()
        self.bebe.establecerPosicion((700, 350))
        #self.bebe.rot_center(self.bebe.image, 90)

        self.grupoJugadores = pygame.sprite.Group(self.jugador)
        self.grupoEnemigos = pygame.sprite.Group(self.bebe)


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

    def update(self,tiempo):

        self.gestorbasura.update(tiempo,self.mascaraCol, self.basuras, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.thunderGestor.update(tiempo, self.mascaraCol, self.thunder, (ANCHO_PANTALLA,ALTO_PANTALLA))
        self.grupoJugadores.update(tiempo,self.mascaraCol, self.grupoBasuras, self.grupoThunders)
        self.bala.update(tiempo, self.mascaraCol, self.grupoJugadores,1)
        self.grupoEnemigos.update(tiempo, self.mascaraCol, self.grupoJugadores,1,self.pantalla)
        
        self.marcadorPuntuacion.update(tiempo, self.jugador)
        self.marcadorTiempo.update(tiempo)

        if self.marcadorTiempo.tiempoLimite < 0:
            pantalla = Sotano(self.director)
            self.director.apilarEscena(pantalla)
        

    def eventos(self,listaEventos):
        for event in listaEventos:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                self.salirPrograma()
        
        teclasPulsadas = pygame.key.get_pressed()
        self.jugador.mover(teclasPulsadas, K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.bebe.mover_cpu(self.jugador)
        self.bala.mover_cpu(self.jugador)


    def dibujar(self,pantalla):

        pantalla.blit(self.suelo,self.suelo.get_rect())
        
        for basura in self.basuras:
            basura.dibujar(pantalla)

        self.thunder.dibujar(pantalla)
        sillaImg = GestorRecursos.CargarImagen('cocina/Sillita.png', -1)
        def sillita():
            pantalla.blit(sillaImg, (700, 290))
        sillita ()
        self.grupoJugadores.draw(pantalla)
        self.bala.draw(pantalla)
        self.grupoEnemigos.draw(pantalla)

        pantalla.blit(self.obstaculos,self.obstaculos.get_rect())

        self.marcadorPuntuacion.dibujar(pantalla)
        self.marcadorTiempo.dibujar(pantalla)
        pygame.display.update()


    def salirPrograma(self):
        self.director.salirPrograma()
