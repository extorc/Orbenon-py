import pygame
from pygame.locals import *
from window import Window
from object import Object
import math

WIN = Window(800, 600, "Orbenon")
object = Object(10,10,100,300, 1000000000000000)
object2 = Object(10,10,200,200, 1)

G = 6.6e-11
while WIN.running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      WIN.running = False

  dt_factor = WIN.clock.tick(30)
  dt = dt_factor/1000
  fdir = (object.posX-object2.posX,object.posY-object2.posY)
  f = G * (object.mass * object2.mass)/Object.get_distance(object, object2)**2
  object2.acceleration_x = dt * f * math.sin(math.atan((object.posY-object2.posY)/(object.posX-object2.posX)))/object2.mass
  object2.acceleration_y = dt * f * math.cos(math.atan((object.posY-object2.posY)/(object.posX-object2.posX)))/object2.mass
  
  object.update()
  object2.update()

  WIN.screen.fill((200,200,200))
  WIN.drawAt((0,0,0),object)
  WIN.drawAt((0,0,0),object2)
  print(object2.velocity_x)
  print(object2.velocity_y)
  pygame.display.update()