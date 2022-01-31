import math
from vec2 import Vec2

class Object:
  def __init__(self, sizeX, sizeY, posX, posY, mass):
    self.sizeX = sizeX
    self.sizeY = sizeY
    self.pos = Vec2(posX, posY)
    self.velocity = Vec2(0,0)
    self.acceleration = Vec2(0,0)
    self.mass = mass
    
  def set_velocity_y(self, y):
    self.velocity.y = y
  def set_velocity_x(self, x):
    self.velocity.x = x
  def set_velocity(self, x, y):
    self.velocity = Vec2(x, y)
  def set_acceleration_y(self, y):
    self.acceleration.y = y
  def set_acceleration_x(self, x):
    self.acceleration.x = x
  def set_acceleration(self, x, y):
    self.acceleration = Vec2(x, y)
  def update(self):
    self.velocity.y+=self.acceleration.y
    self.velocity.x+=self.acceleration.x
    self.pos.y+=self.velocity.y
    self.pos.x+=self.velocity.x

  @staticmethod
  def get_distance(object, object2):
    return math.sqrt((object2.pos.x-object.pos.x)**2 + (object2.pos.y-object.pos.y)**2)