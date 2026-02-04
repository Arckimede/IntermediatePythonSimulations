# 🛰️ Satellite Perturbation Model (J2 Effect)

This project extends a classical two-body orbit simulation by introducing **J2 perturbation**, accounting for Earth's oblateness. Instead of modeling Earth as a perfect sphere, I include its equatorial bulge, which causes measurable orbital drift: a real aerospace engineering effect.

---

## What This Project Demonstrates

1. Two-body orbital mechanics  
2. J2 perturbation modeling  
3. Numerical ODE integration using SciPy  
4. 3D orbit visualization  
5. Deviation analysis over time  

---

## Output

The simulation generates:

1. 3D comparison of:
   - Ideal orbit
   - J2 perturbed orbit

2. Position deviation vs time plot

---

## 🛠 Requirements

pip install numpy matplotlib scipy
