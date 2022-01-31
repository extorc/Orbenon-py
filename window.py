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
    pygame.draw.rect(self.screen,color,(object.pos.x,self.winY-object.pos.y-object.sizeY, object.sizeX, object.sizeY))
  def update(self, pointList, object, object2):
    self.screen.fill((200,200,200))
    pygame.draw.lines(self.screen, (255,0,0), False, pointList)
    self.drawAt((0,0,0),object)
    self.drawAt((0,0,0),object2)
    pygame.display.update()