# 🌊 2D Wave Equation Simulator

An interactive physics simulation of wave propagation in 2D, built with Python and NumPy.

This project numerically solves the 2D wave equation using finite difference methods and visualizes the results in real time. It also tracks total system energy to verify numerical stability.

The goal of this project was to better understand partial differential equations (PDEs), numerical stability, and scientific computing.

## 📦 Technologies

Python

NumPy

Matplotlib

## 🧠 What This Simulates

This program solves the 2D wave equation:

u_tt = c² (u_xx + u_yy)

Basically:

A wave starts as a Gaussian pulse.

It spreads outward over time.

Boundaries are fixed (Dirichlet boundary conditions).

The system’s total energy is calculated at every frame.

The simulation respects the CFL stability condition, ensuring the numerical solution remains stable.

## 🦄 Features

Here’s what the simulator can do:

### 🌊 Real-Time Wave Propagation

Simulates wave motion on a 2D grid.

Uses second-order central difference discretization.

Updates in real time with animation.

### 📊 Energy Monitoring

Computes kinetic + potential energy at each timestep.

Displays total energy to verify conservation.

Helps analyze numerical stability.

### 🖱 Interactive Pulse Injection

Click anywhere on the grid to add a new wave pulse.

Allows experimentation with wave interference.

### ⚙ Stable Time Integration

Implements CFL-safe timestep:

dt = dx / (c * √2) * 0.9

Prevents numerical blow-up.

### 👨‍🔬 The Numerical Method

This simulation uses:

Second-order central differences in space

Explicit time stepping

Finite difference Laplacian

Fixed boundary conditions (u = 0 at edges)

The update rule:

u_next = 2u - u_prev + c² dt² ∇²u

Energy is computed using:

Velocity approximation: (u - u_prev)/dt

Spatial gradients for potential energy

This allows monitoring whether the numerical method preserves energy as expected.

## 📈 What I Learned

### 🔢 Numerical Stability

Understanding and applying the CFL condition to prevent simulation instability.

### 🧮 Discretizing PDEs

How continuous equations are converted into grid-based approximations.

### ⚡ Energy Validation

Using energy conservation as a correctness check for physical simulations.

### 🎥 Scientific Visualization

How to animate and visualize time-evolving physical systems.
