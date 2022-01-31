import pygame
from pygame.locals import *
from window import Window
from object import Object
from vec2 import Vec2
from physics_engine import PhysicsEngine
import math

WIN = Window(800, 600, "Orbenon")
object = Object(10,10,400,200, 10000000000000)
object2 = Object(10,10,500,100, 1)

object2.set_velocity_y(0.2)
pointList = [(500,600-100-10)]

while WIN.running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      WIN.running = False

  dt_factor = WIN.clock.tick(30)
  dt = dt_factor/1000
  f = PhysicsEngine.get_newtonian_force(object, object2)
  dir = Vec2(object.posX-object2.posX,object.posY-object2.posY)
  dir_angle = math.atan2(dir.x,dir.y)
  object2.acceleration_x = dt * f * math.sin(dir_angle)/object2.mass
  object2.acceleration_y = dt * f * math.cos(dir_angle)/object2.mass

  pointList.append((object2.posX,600 - object2.posY-10))

  object.update()
  object2.update()
  WIN.update(pointList, object, object2)