import matplotlib.pyplot as plt
import numpy as np


def plot_trajectory(positions: np.ndarray):
    """
    Plots rocket trajectory in 2D.
    positions: array of shape (N, 2)
    """

    x = positions[:, 0]
    y = positions[:, 1]

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Altitude (m)")
    plt.title("Rocket Trajectory")
    plt.grid(True)
    plt.axis("equal")  # keeps scaling realistic
    plt.show()


def plot_altitude_vs_time(times: np.ndarray, positions: np.ndarray):
    """
    Plots altitude over time.
    """

    y = positions[:, 1]

    plt.figure()
    plt.plot(times, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Altitude vs Time")
    plt.grid(True)
    plt.show()


def plot_speed_vs_time(times: np.ndarray, velocities: np.ndarray):
    """
    Plots speed magnitude over time.
    """

    speed = np.linalg.norm(velocities, axis=1)

    plt.figure()
    plt.plot(times, speed)
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (m/s)")
    plt.title("Speed vs Time")
    plt.grid(True)
    plt.show()
