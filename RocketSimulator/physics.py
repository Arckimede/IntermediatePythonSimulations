import numpy as np

# Constants
g = 9.81              # m/s^2
rho = 1.225           # air density (kg/m^3)


def gravity_force(mass: float) -> np.ndarray:
    # Returns gravity force vector (always downward).
    return np.array([0.0, -mass * g])


def drag_force(velocity: np.ndarray, Cd: float, A: float) -> np.ndarray:
    """
    Calculates 2D aerodynamic drag.
    Drag acts opposite to velocity vector.
    """
    speed = np.linalg.norm(velocity)

    if speed == 0:
        return np.array([0.0, 0.0])

    drag_magnitude = 0.5 * rho * Cd * A * speed**2

    drag_direction = -velocity / speed  # unit vector opposite velocity

    return drag_magnitude * drag_direction


def thrust_force(thrust: float, angle: float) -> np.ndarray:
    """
    Returns thrust force vector.
    
    thrust : magnitude (N)
    angle  : radians (0 = horizontal right, pi/2 = straight up)
    """
    fx = thrust * np.cos(angle)
    fy = thrust * np.sin(angle)

    return np.array([fx, fy])


def net_force(mass: float,
              velocity: np.ndarray,
              thrust: float,
              angle: float,
              Cd: float,
              A: float) -> np.ndarray:
    # Sum of all forces.

    Fg = gravity_force(mass)
    Fd = drag_force(velocity, Cd, A)
    Ft = thrust_force(thrust, angle)

    return Fg + Fd + Ft
