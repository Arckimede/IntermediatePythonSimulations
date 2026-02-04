import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
mu = 398600.4418        # Earth's gravitational parameter (km^3/s^2)
R_earth = 6378.137      # Earth's radius (km)
J2 = 1.08263e-3         # Earth's J2 coefficient

# Initial Orbit Parameters
altitude = 700  # km above Earth
r0_mag = R_earth + altitude
v0_mag = np.sqrt(mu / r0_mag)

# Initial state vector [x, y, z, vx, vy, vz]
y0 = [r0_mag, 0, 0, 0, v0_mag, 0]

# Simulation time (seconds)
t_span = (0, 4 * 3600)  # 4 hours
t_eval = np.linspace(t_span[0], t_span[1], 4000)

# Two-Body (Ideal) Model
def two_body(t, y):
    x, y_pos, z, vx, vy, vz = y
    r = np.sqrt(x**2 + y_pos**2 + z**2)
    
    ax = -mu * x / r**3
    ay = -mu * y_pos / r**3
    az = -mu * z / r**3
    
    return [vx, vy, vz, ax, ay, az]

# J2 Perturbation Model
def j2_perturbed(t, y):
    x, y_pos, z, vx, vy, vz = y
    r = np.sqrt(x**2 + y_pos**2 + z**2)
    
    factor = (3/2) * J2 * mu * R_earth**2 / r**5
    
    zx_ratio = z / r
    
    ax = -mu * x / r**3 + factor * x * (5*zx_ratio**2 - 1)
    ay = -mu * y_pos / r**3 + factor * y_pos * (5*zx_ratio**2 - 1)
    az = -mu * z / r**3 + factor * z * (5*zx_ratio**2 - 3)
    
    return [vx, vy, vz, ax, ay, az]

# Solve ODEs
sol_ideal = solve_ivp(two_body, t_span, y0, t_eval=t_eval)
sol_j2 = solve_ivp(j2_perturbed, t_span, y0, t_eval=t_eval)

# Extract positions
r_ideal = sol_ideal.y[:3]
r_j2 = sol_j2.y[:3]

# Compute Deviation
deviation = np.linalg.norm(r_j2 - r_ideal, axis=0)

# Plot 3D Orbit Comparison
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(r_ideal[0], r_ideal[1], r_ideal[2], label="Ideal Orbit")
ax.plot(r_j2[0], r_j2[1], r_j2[2], label="J2 Perturbed Orbit")

# Earth sphere
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:20j]
x = R_earth * np.cos(u)*np.sin(v)
y = R_earth * np.sin(u)*np.sin(v)
z = R_earth * np.cos(v)
ax.plot_surface(x, y, z, color='blue', alpha=0.3)

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title("Orbit Comparison: Ideal vs J2 Perturbation")
ax.legend()

plt.show()

# Plot Deviation Over Time
plt.figure(figsize=(8,5))
plt.plot(t_eval / 3600, deviation)
plt.xlabel("Time (hours)")
plt.ylabel("Position Deviation (km)")
plt.title("Deviation Between Ideal and J2 Orbit")
plt.grid(True)
plt.show()