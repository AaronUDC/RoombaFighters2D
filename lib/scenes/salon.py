from lib.escena import *
from pygame.locals import *
from lib.sprites.actores.jugador import Jugador
from lib.sprites.actores.enemigo.gato import Gato
from lib.sprites.actores.enemigo.bala import Bala
from lib.sprites.sprite import MiSprite
from lib.gestorRecursos import GestorRecursos

BLANCO = (255,255,255)

class Salon(EscenaPygame):

    def __init__(self,director):

        EscenaPygame.__init__(self,director);

        #Fondo de la escena
        self.suelo = GestorRecursos.CargarImagen('suelo.png',-1)
        self.suelo = pygame.transform.scale(self.suelo,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.suelo = self.suelo.convert_alpha()
        self.suelo.set_alpha(None)

        #Paredes
        self.paredes = Paredes()


        self.sofa = Sofa((224,480))
        #Agrupamos los elementos que no se mueven (paredes y muebles) para comprobar colisiones
        self.grupoElementosEstaticos = pygame.sprite.Group(self.paredes.paredTop,self.paredes.paredBot,self.paredes.paredLeft,self.paredes.paredRight)
        self.grupoElementosEstaticos.add(self.sofa)

        self.mascaraImg = GestorRecursos.CargarImagen('mask.png', -1)
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

        pygame.display.update()

    def update(self,tiempo):

<<<<<<< HEAD
        self.grupoJugadores.update(tiempo,self.mascaraCol)
=======
        self.grupoJugadores.update(tiempo,self.grupoElementosEstaticos)
        self.grupoEnemigos.update(tiempo, self.grupoElementosEstaticos)
>>>>>>> origin/Tarea_Borja

    def eventos(self,listaEventos):
        for event in listaEventos:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                self.salirPrograma()
        
        teclasPulsadas = pygame.key.get_pressed()
        self.jugador.mover(teclasPulsadas, K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.gato.mover_cpu(self.jugador)
        self.bala.disparar(self.jugador)


    def dibujar(self,pantalla):

        pantalla.blit(self.suelo,self.suelo.get_rect())
        

        
        self.grupoJugadores.draw(pantalla)
        self.grupoEnemigos.draw(pantalla)

        self.paredes.dibujar(pantalla)
        pantalla.blit(self.sofa.sprite,self.sofa.rect)
        pygame.display.update()

    def salirPrograma(self):
        self.director.salirPrograma()

class Paredes:
    
    class Pared(MiSprite):

        def __init__(self, ruta, flip, pos):

            MiSprite.__init__(self)
            self.sprite = GestorRecursos.CargarImagen(ruta,-1)
            self.sprite = self.sprite.convert_alpha()
            self.sprite.set_alpha(None)
            self.sprite = pygame.transform.flip(self.sprite, flip[0], flip[1])
            self.rect = self.sprite.get_rect()
            self.rect.right = pos[0]
            self.rect.top = pos[1]

    def __init__(self):
        
        self.paredTop = Paredes.Pared('pared_H.png',(False,True),(ANCHO_PANTALLA,0))
        self.paredBot = Paredes.Pared('pared_H.png',(False,False),(ANCHO_PANTALLA,ALTO_PANTALLA-32))
        self.paredLeft = Paredes.Pared('pared_V.png',(False,False),(32,32))
        self.paredRight = Paredes.Pared('pared_V.png',(True,False),(ANCHO_PANTALLA,32))
    
    
    def dibujar(self,pantalla):
        pantalla.blit(self.paredTop.sprite,self.paredTop.rect)
        pantalla.blit(self.paredBot.sprite,self.paredBot.rect)
        pantalla.blit(self.paredLeft.sprite,self.paredLeft.rect)
        pantalla.blit(self.paredRight.sprite,self.paredRight.rect)


class Sofa(MiSprite):

    def __init__(self, pos):
        
        MiSprite.__init__(self)
        self.sprite = GestorRecursos.CargarImagen('sofa/sofa.png',-1)
        self.rect = self.sprite.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]