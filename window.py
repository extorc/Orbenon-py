import pygame
from pygame.locals import *

class Window:
  def __init__(self, x, y, title):
    pygame.init()
    pygame.font.init()
    self.winX = x
    self.winY = y

    self.screen = pygame.display.set_mode((self.winX, self.winY))
    self.running = True

    self.clock = pygame.time.Clock()
    self.dt = self.clock.tick(60)
    pygame.display.set_caption(title)

  def drawAt(self, color, x, y):
    pygame.draw.rect(self.screen,color,(x,self.winY-y-10,10,10))