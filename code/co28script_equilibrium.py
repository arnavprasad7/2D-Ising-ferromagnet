# -*- coding: utf-8 -*-
"""
CO28: Ferromagnetism

Study of approach to equilibrium state of magnetisation using the Ising model

Arnav Prasad
Wadham College, Oxford

Created on Thu Nov 29 15:07:09 2018
"""

import numpy as np
import matplotlib.pyplot as plt

from sweep import sweep

N = 10 #Elements in the sides of the square lattice 

JkT = 0.7 #Value of J/kT
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
       
M = [] #Empty list to store magnetisation (normalised)
absM = [] #Empty list to store absolute value of magnetisation (normalised)
avgabsM = [] #Empty list to store average absolute value of magnetisation
    
iterations = 1000 #No. of sweeps we want to conduct

#To start after a few sweeps are done so that we are close to the equilibrium state 
#(and to avoid the effect of the initial state)
eqstate = int(iterations/3) 

#Set up empty lists for storing data after our chosen "equilibrium state" 
eqsweep = [] #sweep no. after "equilibrium"
eqM = [] #absolute magnetisation value after "equilibrium"

#Do multiple sweeps and store the information related to magnetisation in a list    
for i in range(iterations):
    S = sweep(S, JkT, BkT)
    
#    #For visualising lattice
#    if i%100 == 0:
#        plt.clf()
#        plt.title("i = " + str(i))
#        plt.imshow(S)
#        plt.pause(0.000001)

    M.append(np.sum(S)/maxM) #Store value of M after i sweeps
    absM.append(abs(np.sum(S)/maxM)) #Store value of |M| after i sweeps
    
    #For points after our chosen "equilibrium state"
    if i >= eqstate:
        
        eqsweep.append(i)
        eqM.append(abs(np.sum(S)/maxM))
        avgabsM.append(sum(absM)/len(absM))


#Plot(s) for studying approach to equilibrium

#Plot |M| vs no. of sweeps 
plt.figure(1)  
plt.plot(range(iterations), absM)
plt.grid(True)
plt.ylim(0,1)
plt.xlabel('No. of sweeps')
plt.ylabel('|M| (normalised)')
plt.suptitle('Absolute Magnetisation')
plt.title('J/kT = ' + str(JkT) + ', B/kT = ' + str(BkT))

##Plot cumulative sum of M vs no. of sweeps (after "equilibrium point")
#plt.figure(2)        
#plt.plot(eqsweep, np.cumsum(eqM))
#plt.suptitle('Cumulative Magnetisation (after "equilibrium point")')
#plt.xlabel('No. of sweeps')
#plt.ylabel('Cumulative Absolute Magnetisation')
#plt.grid(True)
#plt.title('J/kT = ' + str(JkT) + ', B/kT = ' + str(BkT))
#
##Plot average absolute magnetisation vs no. of sweeps
#plt.figure(3)  
#plt.plot(eqsweep, avgabsM)
#plt.grid(True)
#plt.ylim(0,1)
#plt.xlabel('No. of sweeps')
#plt.ylabel('Average |M| (normalised)')
#plt.suptitle('Absolute Average Magnetisation (after "equilibrium point")')
#plt.title('J/kT = ' + str(JkT) + ', B/kT = ' + str(BkT))