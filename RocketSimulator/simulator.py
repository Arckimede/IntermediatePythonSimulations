import numpy as np
from physics import net_force


class RocketSimulator:
    def __init__(self,
                 m_dry,
                 m_fuel,
                 burn_rate,
                 thrust,
                 Cd,
                 A,
                 dt=0.01,
                 method="euler"):

        self.m_dry = m_dry
        self.m_fuel = m_fuel
        self.burn_rate = burn_rate
        self.thrust = thrust
        self.Cd = Cd
        self.A = A
        self.dt = dt
        self.method = method

        # state = [x, y, vx, vy]
        self.state = np.array([0.0, 0.0, 0.0, 0.0])
        self.time = 0.0

    @property
    def mass(self):
        return self.m_dry + self.m_fuel

    def derivatives(self, state, angle):
        """
        Returns time derivative of state.
        """

        x, y, vx, vy = state
        velocity = np.array([vx, vy])

        # thrust only if fuel exists
        current_thrust = self.thrust if self.m_fuel > 0 else 0.0

        F = net_force(
            mass=self.mass,
            velocity=velocity,
            thrust=current_thrust,
            angle=angle,
            Cd=self.Cd,
            A=self.A
        )

        acceleration = F / self.mass

        return np.array([vx, vy, acceleration[0], acceleration[1]])

    # Euler Integrator
    def _euler_step(self, angle):
        dstate = self.derivatives(self.state, angle)
        self.state += dstate * self.dt

    # RK4 Integrator
    def _rk4_step(self, angle):
        dt = self.dt

        k1 = self.derivatives(self.state, angle)
        k2 = self.derivatives(self.state + 0.5 * dt * k1, angle)
        k3 = self.derivatives(self.state + 0.5 * dt * k2, angle)
        k4 = self.derivatives(self.state + dt * k3, angle)

        self.state += (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    def step(self, angle):

        # burn fuel
        if self.m_fuel > 0:
            fuel_used = self.burn_rate * self.dt
            self.m_fuel = max(0.0, self.m_fuel - fuel_used)

        # choose method
        if self.method == "rk4":
            self._rk4_step(angle)
        else:
            self._euler_step(angle)

        self.time += self.dt

    def simulate(self, t_max, angle_function):

        states = []
        times = []

        while self.time < t_max and self.state[1] >= 0:

            angle = angle_function(self.time)

            self.step(angle)

            states.append(self.state.copy())
            times.append(self.time)

        return np.array(times), np.array(states)
