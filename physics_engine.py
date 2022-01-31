from object import Object

class PhysicsEngine:
  G = 6.6e-11
  @staticmethod
  def get_newtonian_force(object, object2):
    return PhysicsEngine.G * (object.mass * object2.mass)/Object.get_distance(object, object2)**2