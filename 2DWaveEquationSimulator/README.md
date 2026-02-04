# 2D Wave Equation Simulator (Finite Differences)

A Python simulation of a vibrating membrane (like a drum surface) using a finite difference solution of the 2D wave equation.
This project demonstrates numerical PDE discretization, stability constraints (CFL condition) and grid-based simulation using fully vectorized NumPy operations.

---

## Mathematical Model

We solve the 2D wave equation:

∂²u/∂t² = c² ∇²u

Where:
- `u(x, y, t)` = membrane displacement
- `c` = wave propagation speed
- `∇²` = 2D Laplacian operator

### Spatial Discretization

The Laplacian is approximated using second-order finite differences:

∇²uᵢⱼ ≈  (uᵢ₊₁ⱼ + uᵢ₋₁ⱼ + uᵢⱼ₊₁ + uᵢⱼ₋₁ − 4uᵢⱼ) / dx²

### Time Stepping (Explicit Scheme)

uⁿ⁺¹ = 2uⁿ − uⁿ⁻¹ + c² dt² ∇²uⁿ

---

## Stability Condition (CFL)

For numerical stability in 2D:

c * dt / dx ≤ 1 / √2

The simulation enforces this condition automatically.

If violated:
- The solution becomes unstable
- Energy grows exponentially
- The simulation "blows up"

---

## Features

- 2D finite difference discretization
- Explicit second-order time integration
- CFL-stable time stepping
- Fixed (Dirichlet) boundary conditions
- Optional free (Neumann) boundary conditions
- Gaussian pulse initial condition
- Interactive mouse excitation (click to hit the membrane)
- Real-time animation (Matplotlib)
- Total energy computation and visualization
- Fully vectorized NumPy implementation

---

## Interactive Controls

- Click anywhere on the membrane to inject a localized Gaussian pulse.
- Watch wave propagation and reflections.
- Observe energy conservation in the live energy plot.

---

## Energy Monitoring

The simulator computes total energy:

E = ∫ [ ½ (u_t)² + ½ c² |∇u|² ] dx dy

You can use the energy plot to:

- Verify numerical stability
- Detect CFL violations
- Observe energy injection from mouse interaction
- Study boundary reflections

---

## Installation

git clone https://github.com/Arckimede/IntermediatePythonSimulations/

## Install dependencies:

pip install numpy matplotlib
