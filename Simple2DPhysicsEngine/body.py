import numpy as np

class Body:
    def __init__(self, position, radius, mass, restitution=0.9):
        self.position = np.array(position, dtype=float)
        self.velocity = np.zeros(2)
        self.force = np.zeros(2)

        self.radius = radius
        self.mass = mass
        self.inv_mass = 0.0 if mass == 0 else 1.0 / mass
        self.restitution = restitution

    def apply_force(self, force):
        self.force += force

    def integrate(self, dt):
        if self.mass == 0:
            return

        acceleration = self.force * self.inv_mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
        self.force[:] = 0