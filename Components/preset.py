import pygame
import pygame_gui
from pygame.locals import *
from Components.object import Object
from System.physics_engine import PhysicsEngine
import math

def gravity_assist(dt, object, object2, WIN, pointList):
  f = PhysicsEngine.get_newtonian_force(object, object2)
  dir = Object.get_xy_dist(object, object2)
  dir_angle = math.atan2(dir.x,dir.y)
  object2.set_acceleration(PhysicsEngine.force_mass_to_ac(dt, f, dir_angle,object2.mass))

  pointList.append((object2.pos.x,WIN.winY - object2.pos.y-object2.sizeY))

  object.update()
  object2.update()
  vel = pygame_gui.elements.UITextBox("{}".format(math.sqrt(object2.velocity.x**2 + object2.velocity.y**2)), pygame.Rect(165, 5, 70, 45),WIN.manager ,visible=1)