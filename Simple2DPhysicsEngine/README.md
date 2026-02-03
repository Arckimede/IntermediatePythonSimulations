⚙️ Simple 2D Physics Engine 

This project implements a modular 2D rigid body physics engine built from scratch in Python. It focuses on engine architecture, physics infrastructure and clean separation between computation and rendering.
The engine simulates circular rigid bodies under gravity, resolves collisions using impulse-based methods and supports basic positional constraints.

🧱 Project Features

-Rigid body dynamics (circle bodies)

-Gravity and force accumulation

-Semi-implicit Euler integration

-Circle–circle collision detection

-Impulse-based collision response

-Wall collision handling

-Distance constraint (rod behavior)

-Separation of physics engine and rendering layer

🗂 Project Structure

The physics modules are completely independent of Pygame. Rendering is handled separately in main.py. This separation mirrors real-world engine architecture where simulation logic and visualization are decoupled.

🧠 Physics Model

The engine uses:

-Newtonian mechanics (F = ma)

-Impulse-based collision resolution

-Basic positional correction to prevent overlap

-Constraint projection for maintaining fixed distances

-The distance constraint allows simulation of rigid rods or pendulum-like systems.
