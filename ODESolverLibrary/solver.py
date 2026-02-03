import numpy as np
from integrators import Euler, RK4, SymplecticVerlet
from errorControl import estimate_error


class ODESolver:

    def __init__(self, f, method="rk4", dt=0.01, adaptive=False, tol=1e-6):
        self.f = f
        self.dt = dt
        self.adaptive = adaptive
        self.tol = tol

        if method == "euler":
            self.integrator = Euler()
        elif method == "rk4":
            self.integrator = RK4()
        elif method == "verlet":
            self.integrator = SymplecticVerlet()
        else:
            raise ValueError("Unknown method")

    def solve(self, y0, t0, tf):
        t_values = [t0]
        y_values = [np.array(y0)]

        t = t0
        y = np.array(y0)

        dt = self.dt

        while t < tf:

            if self.adaptive:
                y_new, error = estimate_error(self.integrator, self.f, t, y, dt)

                if error > self.tol:
                    dt *= 0.5
                    continue
                elif error < self.tol / 10:
                    dt *= 1.2

                y = y_new
            else:
                y = self.integrator.step(self.f, t, y, dt)

            t += dt
            t_values.append(t)
            y_values.append(y.copy())

        return np.array(t_values), np.array(y_values)
