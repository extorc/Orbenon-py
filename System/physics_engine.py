import math
from Components.object import Object
from Components.vec2 import Vec2

class PhysicsEngine:
  G = 6.6e-11
  @staticmethod
  def get_newtonian_force(object, object2):
    return PhysicsEngine.G * (object.mass * object2.mass)/Object.get_distance(object, object2)**2
  @staticmethod
  def force_mass_to_ac(dt, f, a, m):
    return Vec2(dt * (f * math.sin(a))/m, dt * (f * math.cos(a))/m)