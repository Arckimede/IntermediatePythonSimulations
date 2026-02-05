# 🛰️ Orbital Perturbation Simulator (J2 Model)

A physics-based simulation of satellite motion around Earth, comparing an ideal two-body orbit with a more realistic J2-perturbed model.

Built with Python, NumPy, SciPy and Matplotlib, this project demonstrates how small physical effects (Earth’s oblateness) influence long-term orbital motion.

## 📦 Technologies

Python

NumPy

SciPy

Matplotlib (2D + 3D plotting)

Classical orbital mechanics

## 🧠 What This Simulates

This project compares two models of satellite motion:

### 1️⃣ Ideal Two-Body Model

Assumes:

Earth is perfectly spherical

Only gravity acts on the satellite

Orbit follows Newton’s inverse-square law

### 2️⃣ J2 Perturbation Model

Adds:

Earth’s oblateness (equatorial bulge)

J2 gravitational harmonic term

More realistic acceleration model

The simulation shows how even small perturbations cause measurable orbital deviation over time.

##🌍 Physical Background 

In the ideal case, acceleration is:

a = -μ r / r³

Where:

μ is Earth’s gravitational parameter

r is the position vector

The J2 model adds a correction term:

a_J2 ∝ J2 * (R_earth² / r⁵)

This accounts for Earth's slightly flattened shape.

The result is:

Orbital precession

Gradual deviation from the ideal path

## 🦄 Features

###🛰️ Dual Orbit Simulation

Solves both models using solve_ivp

Integrates full 3D motion

Same initial conditions for fair comparison

### 🌎 3D Orbit Visualization

Displays both orbits in 3D space

Includes Earth rendered as a sphere

Clear visual comparison of divergence

### 📈 Deviation Analysis

Computes position difference over time

Shows how perturbation accumulates

Quantifies physical impact of J2

### ⚙ Numerical Integration

Uses SciPy’s adaptive ODE solver

Handles nonlinear coupled differential equations

Maintains stable integration over hours

## 📊 What the Results Show

Over 4 hours:

The ideal orbit remains perfectly Keplerian.

The J2-perturbed orbit slowly deviates.

Position error grows over time.

This demonstrates how small physical corrections matter in real satellite dynamics.

## 📈 What I Learned

### 🧮 Orbital Mechanics

How gravitational harmonics affect satellite motion.

### 🔢 Modeling Physical Systems

How to translate physics equations into ODE systems.

### 🧠 Perturbation Theory in Practice

Understanding how small corrections create measurable long-term effects.

### ⚙ Numerical Integration

Working with adaptive ODE solvers and 6D state vectors.

### 🌍 Visualization of Physical Systems

Rendering 3D trajectories and interpreting simulation data.

## 💭 Possible Improvements

Simulate longer durations (days instead of hours)

Show orbital element changes (RAAN precession)

Add atmospheric drag model

Compare different inclinations

Validate against known analytical J2 precession rate

Add animation of satellite motion

Turn into reusable orbital mechanics module
