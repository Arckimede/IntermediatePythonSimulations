import numpy as np
import matplotlib.pyplot as plt
from solver import ODESolver

mu = 1.0

def two_body(t, state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)

    ax = -mu * x / r**3
    ay = -mu * y / r**3

    return np.array([vx, vy, ax, ay])


y0 = [1.0, 0.0, 0.0, 1.0]

solver = ODESolver(two_body, method="rk4", dt=0.01, adaptive=True, tol=1e-5)
t, sol = solver.solve(y0, 0, 20)

plt.plot(sol[:, 0], sol[:, 1], color='#9C45E8')
plt.gca().set_aspect("equal")
plt.title("Orbit using Reusable ODE Library")
plt.show()
