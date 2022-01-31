import pygame
import pygame_gui
from pygame.locals import *
from window import Window
from object import Object
from vec2 import Vec2
from physics_engine import PhysicsEngine
import math

WIN = Window(800, 600, "Orbenon")
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

object = Object(10,10,400,200, 10000000000000)
object2 = Object(10,10,500,100, 1)

object2.set_velocity_y(0.2)
object2.set_velocity_x(0.2)
pointList = [(500,600-100-10),(500,600-100-10)]

manager = pygame_gui.UIManager((800, 600))
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5,5), (70, 45)),text='Start',manager=manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80,5), (80, 45)),text='Pause',manager=manager)

physics_running = False

while WIN.running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      WIN.running = False
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == start_button:
        print('Started Physics Simulation')
        physics_running = True
      elif event.ui_element == pause_button:
        print('Paused Physics Simulation')
        physics_running = False
    manager.process_events(event)

  dt_factor = WIN.clock.tick(30)
  dt = dt_factor/1000
  manager.update(dt)

  if physics_running:
    f = PhysicsEngine.get_newtonian_force(object, object2)
    dir = Vec2(object.pos.x-object2.pos.x,object.pos.y-object2.pos.y)
    dir_angle = math.atan2(dir.x,dir.y)
    object2.set_acceleration_x(dt * f * math.sin(dir_angle)/object2.mass)
    object2.set_acceleration_y(dt * f * math.cos(dir_angle)/object2.mass)

    pointList.append((object2.pos.x,600 - object2.pos.y-10))

    object.update()
    object2.update()

  WIN.update(background, manager, pointList, object, object2)