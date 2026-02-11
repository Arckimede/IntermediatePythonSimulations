# 🚀 2D Rocket Flight Simulator

A physics-based rocket trajectory simulator built with Python, NumPy and Matplotlib.
This project numerically simulates a 2D rocket launch including gravity, aerodynamic drag, thrust and fuel consumption. It supports both Euler and RK4 integration methods to compare numerical accuracy.
The goal of this project was to better understand classical mechanics, numerical integration methods and physics-based simulation.

## 📦 Technologies

Python
NumPy
Matplotlib

## 🧠 What This Simulates

This program simulates a rocket moving in 2D under the influence of:

Gravity
Aerodynamic drag
Engine thrust
Changing mass due to fuel burn

The rocket:

Starts at ground level, burns fuel at a constant rate, produces thrust at a given angle, slows down due to air resistance and falls back to the ground after fuel runs out.
The simulation stops when the rocket hits the ground.

## 🦄 Features

Here’s what the simulator can do:

### 🚀 Realistic Force Modeling

Includes:

Gravity (constant downward force)

Quadratic air drag (depends on speed²)

Thrust vector based on angle

Dynamic mass (fuel decreases over time)

All forces are combined using Newton’s Second Law:

F = m a

### 🔁 Multiple Integration Methods

You can choose between:

Euler Method: simple, fast and less accurate

Runge-Kutta 4 (RK4): more accurate, better stability, standard in scientific computing

The project compares both methods visually.

### 📈 Trajectory Visualization

Plots:

2D rocket trajectory

Euler vs RK4 comparison

(Optional) altitude vs time

(Optional) speed vs time

This makes it easy to see numerical differences between methods.

## 👨‍🔬 The Physics Model

The rocket state is:

[x, y, vx, vy]

Position and velocity are updated over time.

Forces included:

Gravity: 
Fg = (0, -mg)

Drag: 
Fd = ½ ρ Cd A v² (opposite velocity)

Thrust:
Ft = (T cosθ, T sinθ)

Net force:
F = Fg + Fd + Ft

Acceleration:
a = F / m

Fuel mass decreases over time:
m = m_dry + m_fuel

When fuel reaches zero, thrust stops.

## ⚙ Numerical Integration

Two methods are implemented:

1. Euler Method

x_next = x + v dt
v_next = v + a dt

Simple but accumulates error over time.

2. RK4 Method

Uses four slope evaluations per step to approximate the next state and is much more accurate for nonlinear systems like drag-based motion.

## 📊 What I Learned

### 🧮 Numerical Integration
Understanding the difference between Euler and RK4 in real physical systems.

### 🌍 Force-Based Simulation
How to build a modular physics engine with separate force components.

### ⚖ Dynamic Systems
Simulating systems where mass changes over time.

### 📈 Scientific Visualization
Plotting trajectories and comparing numerical methods visually.

## 📹 Video
https://github.com/user-attachments/assets/5f8324b2-8daa-4aae-b8dd-c6d43b9e2578
