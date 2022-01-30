import pygame
from pygame.locals import *
from window import Window
from object import Object

WIN = Window(800, 600, "Orbenon")
object = Object(10,10,0,300, 1)
object2 = Object(10,10,100,200, 1)


while WIN.running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      WIN.running = False

  object.update()
  object2.update()

  WIN.screen.fill((200,200,200))
  WIN.drawAt((0,0,0),object)
  WIN.drawAt((0,0,0),object2)
  
  pygame.display.update()
  dt = WIN.clock.tick(30)
  object.set_acceleration_y(-9.8 * (dt/1000))
  object2.set_acceleration_y(-9.8 * (dt/1000))
  print(dt)