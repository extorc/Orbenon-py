import pygame
from pygame.locals import *
from window import Window

WIN = Window()
  
while WIN.running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      WIN.running = False

  WIN.screen.fill((200,200,200))
  WIN.drawAt((0,0,0),0,0)
  pygame.display.update()