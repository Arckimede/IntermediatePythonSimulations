import numpy as np


class Integrator:
    def step(self, f, t, y, dt):
        raise NotImplementedError


class Euler(Integrator):
    def step(self, f, t, y, dt):
        return y + dt * f(t, y)


class RK4(Integrator):
    def step(self, f, t, y, dt):
        k1 = f(t, y)
        k2 = f(t + dt/2, y + dt*k1/2)
        k3 = f(t + dt/2, y + dt*k2/2)
        k4 = f(t + dt, y + dt*k3)
        return y + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)


class SymplecticVerlet(Integrator):
    """
    Assumes state = [x, v]
    where f returns [v, a]
    """

    def step(self, f, t, y, dt):
        n = len(y) // 2
        x = y[:n]
        v = y[n:]

        a = f(t, y)[n:]

        v_half = v + 0.5 * dt * a
        x_new = x + dt * v_half

        y_temp = np.concatenate([x_new, v_half])
        a_new = f(t + dt, y_temp)[n:]

        v_new = v_half + 0.5 * dt * a_new

        return np.concatenate([x_new, v_new])