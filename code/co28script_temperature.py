# -*- coding: utf-8 -*-
"""
CO28: Ferromagnetism

Study of temperature dependence of magnetisation using the Ising model

Arnav Prasad
Wadham College, Oxford

Created on Thu Nov 29 15:07:09 2018
"""

import numpy as np
import matplotlib.pyplot as plt

from sweep import sweep

N = 10 #Elements in the sides of the square lattice 

JkTrange = np.linspace(0,1,10) #Values of J/kT
BkT = 0.0 #Value of B/kT

#Prepare lattice (NxN array) with randomly distributed values of plus/minus 1

S_init = np.random.rand(N,N) #create NxN array with random numbers in [0,1]

S = np.copy(S_init)

#loop through S and adjust numbers to be either 1 or -1
for i in range(N):
    for j in range(N):
        S[i,j] = (round(S[i,j]))
        if S[i,j] == 0:
            S[i,j] = -1
  
maxM = N*N #To normalise M such that |M|=1 corresponds to all spins pointing in the same direction  
    
iterations = 1000 #No. of sweeps we want to conduct for each value of J/kT

#To start after a few sweeps are done so that we are close to the equilibrium state 
#(and to avoid the effect of the initial state)
eqstate = int(iterations/3) 

finalM = []

for JkT in JkTrange:
    
    M = [] #Empty list to store magnetisation (normalised)
    absM = [] #Empty list to store absolute value of magnetisation (normalised)
    avgabsM = [] #Empty list to store average absolute value of magnetisation

    #Do multiple sweeps and store the information related to magnetisation in a list    
    for i in range(iterations):
        S = sweep(S, JkT, BkT)
    
        M.append(np.sum(S)/maxM) #Store value of M after i sweeps
        absM.append(abs(np.sum(S)/maxM)) #Store value of |M| after i sweeps
        
        #For points after our chosen "equilibrium state"
        if i >= eqstate:
            avgabsM.append(sum(absM)/len(absM))
        
    finalM.append(avgabsM[-1])
            
#Plot average |M| vs J/kT
plt.figure(1)
plt.scatter(JkTrange, finalM)
plt.grid(True)
plt.suptitle('Temperature dependence of |M|')
plt.ylabel('Average |M| (normalised)')
plt.xlabel('J/kT')
plt.title('B/kT = ' + str(BkT))