import numpy as np
from simulator import RocketSimulator
from visualization import plot_trajectory


def constant_angle(t):
    return np.pi / 2


# Euler Simulation
sim_euler = RocketSimulator(
    m_dry=5.0,
    m_fuel=10.0,
    burn_rate=1.0,
    thrust=300.0,
    Cd=0.5,
    A=0.1,
    dt=0.05,
    method="euler"
)

t_e, states_e = sim_euler.simulate(20, constant_angle)


# RK4 Simulation
sim_rk4 = RocketSimulator(
    m_dry=5.0,
    m_fuel=10.0,
    burn_rate=1.0,
    thrust=300.0,
    Cd=0.5,
    A=0.1,
    dt=0.05,
    method="rk4"
)

t_r, states_r = sim_rk4.simulate(20, constant_angle)


# Plot both
import matplotlib.pyplot as plt

plt.figure()
plt.plot(states_e[:,0], states_e[:,1], label="Euler")
plt.plot(states_r[:,0], states_r[:,1], label="RK4")
plt.legend()
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Euler vs RK4")
plt.grid(True)
plt.show()