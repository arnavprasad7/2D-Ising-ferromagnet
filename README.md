# 2D-Ising-ferromagnet
Simulating a two-dimensional ferromagnet using a Monte Carlo method—implemented via the Metropolis–Hastings algorithm—as described by the Ising model of ferromagnetism.

## About
This is a project I did in the second year of my Physics degree at Oxford. In this, we explore the concept of ferromagnetism—and its inherently probabalistic nature—through the *Ising model*. We initialize a square lattice (NxN array) as a set of electron spins. We then simulate the evolution of the system by "sweeping" through it: iteratively computing the energy cost of an electron's spin changing, evaluating the probability of the defined system configuration, and then using the Monte Carlo method via the Metropolis algorithm. 

We study the temperature dependence of the ferromagnet, its approach to equilibrium, and its phase transition at a *critical temperature*.

## Files
* *Ferromagnetism, Final Report.pdf*: A complete report of the project (created in LaTeX) that describes the underlying theory, the method, the results, and the analysis.
* *co28script_equilibrium.py*: Python program exploring the possible approach to equilibrium of the ferromagnet, depending on the different parameters (exchange energy, temperature, external magnetic field).
* *co28script_temperature.py*: Python program studying the phase transition of the ferromagnet—from ferromagnetism to paramagnetism—as a function of temeperature and external B-field.
