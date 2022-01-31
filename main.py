import pygame
from pygame.locals import *
from window import Window
from object import Object
from vec2 import Vec2
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
  f = G * (object.mass * object2.mass)/Object.get_distance(object, object2)**2
  dir = Vec2(object.posX-object2.posX,object.posY-object2.posY)
  dir_angle = math.atan2(dir.x,dir.y)
  print("slope" + str(dir_angle) + "Pos : " + str(object2.posX) + " " + str(object2.posY))
  dir.print()
  object2.acceleration_x = dt * f * math.sin(dir_angle)/object2.mass
  object2.acceleration_y = dt * f * math.cos(dir_angle)/object2.mass
  
  object.update()
  object2.update()

  WIN.screen.fill((200,200,200))
  WIN.drawAt((0,0,0),object)
  WIN.drawAt((0,0,0),object2)
  pygame.display.update()