import numpy as np
from collisions import resolve_circle_collision, resolve_wall_collision

class World:
    def __init__(self, width, height, gravity=(0, 500)):
        self.width = width
        self.height = height
        self.gravity = np.array(gravity)

        self.bodies = []
        self.constraints = []

    def add_body(self, body):
        self.bodies.append(body)

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def step(self, dt):
        # Apply gravity
        for body in self.bodies:
            if body.mass != 0:
                body.apply_force(self.gravity * body.mass)

        # Integrate
        for body in self.bodies:
            body.integrate(dt)

        # Solve constraints
        for constraint in self.constraints:
            constraint.solve()

        # Resolve collisions
        for i in range(len(self.bodies)):
            for j in range(i+1, len(self.bodies)):
                resolve_circle_collision(self.bodies[i], self.bodies[j])

        # Wall collisions
        for body in self.bodies:
            resolve_wall_collision(body, self.width, self.height)
