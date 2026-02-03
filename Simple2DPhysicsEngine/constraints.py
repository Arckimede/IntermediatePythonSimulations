import numpy as np

class DistanceConstraint:
    def __init__(self, b1, b2, length):
        self.b1 = b1
        self.b2 = b2
        self.length = length

    def solve(self):
        delta = self.b2.position - self.b1.position
        dist = np.linalg.norm(delta)

        if dist == 0:
            return

        diff = (dist - self.length) / dist
        correction = delta * 0.5 * diff

        if self.b1.mass != 0:
            self.b1.position += correction
        if self.b2.mass != 0:
            self.b2.position -= correction
