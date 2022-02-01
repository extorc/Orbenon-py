import pygame
from pygame.locals import *
import pygame_gui

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
    self.manager = pygame_gui.UIManager((800, 600))

  def drawAt(self, color, object):
    pygame.draw.rect(self.screen,color,(object.pos.x,self.winY-object.pos.y-object.sizeY, object.sizeX, object.sizeY))
    
  def update(self, background, manager, pointList, object, object2):
    self.screen.blit(background,(0,0))
    self.screen.fill((200,200,200))
    pygame.draw.lines(self.screen, (255,0,0), False, pointList)
    self.drawAt((0,0,0),object)
    self.drawAt((0,0,0),object2)
    manager.draw_ui(self.screen)
    pygame.display.update()