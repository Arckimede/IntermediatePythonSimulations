import numpy as np

def estimate_error(integrator, f, t, y, dt):
    # One full step
    y_big = integrator.step(f, t, y, dt)

    # Two half steps
    y_half = integrator.step(f, t, y, dt/2)
    y_small = integrator.step(f, t + dt/2, y_half, dt/2)

    error = np.linalg.norm(y_big - y_small)

    return y_small, error