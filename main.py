import pygame
import pygame_gui
from pygame.locals import *
from System.window import Window
from Components.object import Object
from System.ui_manager import UIManager
from Components.preset import gravity_assist

WIN = Window(800, 600, "Orbenon")
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

object = Object(10,10,500,400, 30000000000000)
object2 = Object(10,10,170,0, 1)

object2.set_velocity_y(1)
object2.set_velocity_x(1)
object.set_velocity_x(0.22)
pointList = [(object2.pos.x,WIN.winY-object2.pos.y-10),(object2.pos.x,WIN.winY-object2.pos.y-10)]

start_button = UIManager.add_button(5, 5, 70, 45, 'Start', WIN.manager)
pause_button = UIManager.add_button(80,5, 80, 45, 'Pause', WIN.manager)

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
    WIN.manager.process_events(event)

  dt_factor = WIN.clock.tick(30)
  dt = dt_factor/1000
  WIN.manager.update(dt)

  if physics_running:
    gravity_assist(dt, object, object2, WIN, pointList)
  WIN.update(background, WIN.manager, pointList, object, object2)