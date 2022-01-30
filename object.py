import pygame

class Object:
  def __init__(self, sizeX, sizeY, posX, posY):
    self.sizeX = sizeX
    self.sizeY = sizeY
    self.posX = posX
    self.posY = posY
    self.velocity_x = 0
    self.velocity_y = 0

  def set_velocity_y(self, y):
    self.velocity_y = y
  def set_velocity_x(self, x):
    self.velocity_x = x
  def set_velocity(self, x, y):
    self.velocity_y = y
    self.velocity_x = x
  def update(self):
    self.posY+=self.velocity_y
    self.posX+=self.velocity_x