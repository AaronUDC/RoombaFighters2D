import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Sofa")
icon = pygame.image.load('sofa2.jpg')
pygame.display.set_icon(icon)

sofaImg = pygame.image.load('sofa2.jpg')
sofaX = 0
sofaY = 0

def sofa():
    screen.blit(sofaImg, (sofaX, sofaY))

running = True
while running:

  screen.fill((0, 0, 0))

  for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = False
          
  
  sofa()
  pygame.display.update()
