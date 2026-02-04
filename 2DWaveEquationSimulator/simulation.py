import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
Nx, Ny = 150, 150
dx = 0.01
c = 1.0

dt = dx / (c * np.sqrt(2)) * 0.9  # CFL-safe
steps_per_frame = 2

# Fields
u = np.zeros((Nx, Ny))
u_prev = np.zeros((Nx, Ny))
u_next = np.zeros((Nx, Ny))

# Initial Gaussian pulse
x = np.linspace(0, Nx*dx, Nx)
y = np.linspace(0, Ny*dx, Ny)
X, Y = np.meshgrid(x, y)

cx, cy = Nx*dx/2, Ny*dx/2
sigma = 0.08
u = np.exp(-((X-cx)**2 + (Y-cy)**2) / (2*sigma**2))
u_prev = u.copy()

# Energy tracking
energy_history = []

def compute_energy(u, u_prev):
    # velocity approximation
    ut = (u - u_prev) / dt
    
    kinetic = 0.5 * ut**2
    
    # gradients
    ux = (u[2:,1:-1] - u[:-2,1:-1]) / (2*dx)
    uy = (u[1:-1,2:] - u[1:-1,:-2]) / (2*dx)
    
    potential = 0.5 * c**2 * (ux**2 + uy**2)
    
    total_energy = (
        np.sum(kinetic[1:-1,1:-1]) +
        np.sum(potential)
    ) * dx**2
    
    return total_energy

# Plot setup
fig, (ax_wave, ax_energy) = plt.subplots(1, 2, figsize=(10,4))

im = ax_wave.imshow(u, cmap='viridis', vmin=-1, vmax=1)
ax_wave.set_title("2D Wave")

energy_line, = ax_energy.plot([], [])
ax_energy.set_title("Total Energy")
ax_energy.set_xlim(0, 300)
ax_energy.set_ylim(0, 5)

# Mouse interaction
def add_pulse(event):
    global u
    
    if event.inaxes != ax_wave:
        return
    
    ix = int(event.xdata)
    iy = int(event.ydata)
    
    r = 6
    for i in range(-r, r):
        for j in range(-r, r):
            if 0 <= ix+i < Nx and 0 <= iy+j < Ny:
                u[ix+i, iy+j] += 0.5 * np.exp(-(i**2+j**2)/10)

fig.canvas.mpl_connect("button_press_event", add_pulse)

# Update loop
def update(frame):
    global u, u_prev, u_next
    
    for _ in range(steps_per_frame):
        laplacian = (
            u[2:,1:-1] + u[:-2,1:-1] +
            u[1:-1,2:] + u[1:-1,:-2] -
            4*u[1:-1,1:-1]
        ) / dx**2
        
        u_next[1:-1,1:-1] = (
            2*u[1:-1,1:-1] - u_prev[1:-1,1:-1]
            + c**2 * dt**2 * laplacian
        )
        
        # Fixed boundary
        u_next[0,:] = 0
        u_next[-1,:] = 0
        u_next[:,0] = 0
        u_next[:,-1] = 0
        
        u_prev, u = u, u_next.copy()
    
    # Update energy
    E = compute_energy(u, u_prev)
    energy_history.append(E)
    
    im.set_array(u)
    energy_line.set_data(range(len(energy_history)), energy_history)
    
    return [im, energy_line]

ani = FuncAnimation(fig, update, frames=300, interval=30)
plt.tight_layout()
plt.show()