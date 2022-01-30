import pygame
from pygame.locals import *
from object import Object

class Window:
  def __init__(self, x, y, title):
    pygame.init()
    pygame.font.init()
    self.winX = x
    self.winY = y

    self.screen = pygame.display.set_mode((self.winX, self.winY))
    self.running = True

    self.clock = pygame.time.Clock()
    pygame.display.set_caption(title)

  def drawAt(self, color, object):
    pygame.draw.rect(self.screen,color,(object.posX,self.winY-object.posY-object.sizeY, object.sizeX, object.sizeY))