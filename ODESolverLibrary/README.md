# 📐 Reusable ODE Solver Library

This project is a modular ordinary differential equation (ODE) solver framework built in Python. Instead of implementing numerical integration separately inside each simulation, this library provides reusable infrastructure for solving dynamical systems in a clean and extensible way. Furthermore, the solver is designed to work with any system of first-order differential equations and supports multiple numerical integration methods that can be swapped dynamically.

The projects features:

1. Generic ODE solver class

2. Plug-in integrators (Euler, RK4, Symplectic Verlet)

3. Configurable time step

4. Optional adaptive step-size with error estimation (step-doubling)

5. Clean separation between physics models and numerical methods
