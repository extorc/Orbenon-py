import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

winX = 800
winY = 600

screen = pygame.display.set_mode((800,600))
running = True

clock = pygame.time.Clock()
dt = clock.tick(60)

pygame.display.set_caption("Orbenon")

def drawAt(x, y):
  pygame.draw.rect(screen,(0,0,0),(x,winY-y-10,10,10))
  
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((200,200,200))
  drawAt(0,0)
  pygame.display.update()