# -*- coding: utf-8 -*-
"""
Sweep Function
CO28: Ferromagnetism

Arnav Prasad
Wadham College, Oxford

Created on Thu Nov 29 15:54:25 2018
"""

import numpy as np

def energy(Si, Sj, JkT):
    """
    Calculates energy (divided by kT) at a point due to spin of a neighbouring particle
    
    """
    
    E = -JkT * (Si*Sj)
    
    return E

def sweep(S_init, JkT, BkT):
    """
    Performs a full sweep of the configuration, given the values of J/kT and B/kT
    
    Input: 
        -S_init: (NxN) array of the initial configuration
        -JkT, BkT: The values of J/kT and B/kT
        
    Output:
        -S_next: (NxN) array of the next configuration after a full sweep
    
    """
    N = np.shape(S_init)[0]
    
    S = np.copy(S_init)
    
    #iterate over N^2 elements (full sweep of the NxN lattice)
    for a in range(N*N):
        
        #Pick random row of the lattice
        i = np.random.randint(0,N)
        
        #Pick random column of the lattice
        j = np.random.randint(0,N)
        
        #We now have a random (i,j) component of the lattice
        #We can now calculate the change in the energy of the configuration if its spin flips, and accordingly change the
        #configuration of the lattice (do this N^2 times for a full sweep)
        
        S_flipped = np.copy(S) #create a copy of S #np.copy() is VERY important
        S_flipped[i,j] = -S_flipped[i,j] #copy of S but with the (i,j) component's spin flipped
        
        #Setting up the periodic boundary conditions
        
        #top row
        if i == 0:
            
            #top left corner
            if j == 0:
                
                #energy in current configuration
                Ecurrent = energy(S[i,j], S[i+1, j], JkT) + energy(S[i,j], S[i, j+1], JkT) + energy(S[i,j], S[N-1, j], JkT) + \
                           energy(S[i,j], S[i, N-1], JkT) + BkT * np.sum(S)
                
                #energy of configuration if spin flips
                Enext = energy(-S[i,j], S[i+1, j], JkT) + energy(-S[i,j], S[i, j+1], JkT) + energy(-S[i,j], S[N-1, j], JkT) + \
                           energy(-S[i,j], S[i, N-1], JkT) + BkT * np.sum(S_flipped)
            
            #top right corner
            elif j == N-1:
                
                #energy in current configuration
                Ecurrent = energy(S[i,j], S[i+1, j], JkT) + energy(S[i,j], S[i, j-1], JkT) + energy(S[i,j], S[N-1, j], JkT) + \
                           energy(S[i,j], S[i, 0], JkT) + BkT * np.sum(S)
                
                #energy of configuration if spin flips
                Enext = energy(-S[i,j], S[i+1, j], JkT) + energy(-S[i,j], S[i, j-1], JkT) + energy(-S[i,j], S[N-1, j], JkT) + \
                           energy(-S[i,j], S[i, 0], JkT) + BkT * np.sum(S_flipped)
            
            #rest of the top row
            else:
                
                #energy in current configuration
                Ecurrent = energy(S[i,j], S[i+1, j], JkT) + energy(S[i,j], S[i, j+1], JkT) + energy(S[i,j], S[N-1, j], JkT) + \
                           energy(S[i,j], S[i, j-1], JkT) + BkT * np.sum(S)
                
                #energy of configuration if spin flips
                Enext = energy(-S[i,j], S[i+1, j], JkT) + energy(-S[i,j], S[i, j+1], JkT) + energy(-S[i,j], S[N-1, j], JkT) + \
                           energy(-S[i,j], S[i, j-1], JkT) + BkT * np.sum(S_flipped)
                
        #bottom row
        elif i == N-1:
            
            #bottom left corner
            if j == 0:
                
                #energy in current configuration
                Ecurrent = energy(S[i,j], S[i-1, j], JkT) + energy(S[i,j], S[i, j+1], JkT) + energy(S[i,j], S[i, N-1], JkT) + \
                           energy(S[i,j], S[0, j], JkT) + BkT * np.sum(S)
                
                #energy of configuration if spin flips
                Enext = energy(-S[i,j], S[i-1, j], JkT) + energy(-S[i,j], S[i, j+1], JkT) + energy(-S[i,j], S[i, N-1], JkT) + \
                           energy(-S[i,j], S[0, j], JkT) + BkT * np.sum(S_flipped)
                           
            #bottom right corner
            elif j == N-1:
                
                #energy in current configuration
                Ecurrent = energy(S[i,j], S[i-1, j], JkT) + energy(S[i,j], S[i, j-1], JkT) + energy(S[i,j], S[0, j], JkT) + \
                           energy(S[i,j], S[i, 0], JkT) + BkT * np.sum(S)
                
                #energy of configuration if spin flips
                Enext = energy(-S[i,j], S[i-1, j], JkT) + energy(-S[i,j], S[i, j-1], JkT) + energy(-S[i,j], S[0, j], JkT) + \
                           energy(-S[i,j], S[i, 0], JkT) + BkT * np.sum(S_flipped)
                           
            #rest of the bottom row
            else:
                
                #energy in current configuration
                Ecurrent = energy(S[i,j], S[i-1, j], JkT) + energy(S[i,j], S[i, j-1], JkT) + energy(S[i,j], S[0, j], JkT) + \
                           energy(S[i,j], S[i, j+1], JkT) + BkT * np.sum(S)
                
                #energy of configuration if spin flips
                Enext = energy(-S[i,j], S[i-1, j], JkT) + energy(-S[i,j], S[i, j-1], JkT) + energy(-S[i,j], S[0, j], JkT) + \
                           energy(-S[i,j], S[i, j+1], JkT) + BkT * np.sum(S_flipped)
                   
        #leftmost column
        elif j == 0:
            
            #energy in current configuration
            Ecurrent = energy(S[i,j], S[i-1, j], JkT) + energy(S[i,j], S[i, N-1], JkT) + energy(S[i,j], S[i+1, j], JkT) + \
                       energy(S[i,j], S[i, j+1], JkT) + BkT * np.sum(S)
            
            #energy of configuration if spin flips
            Enext = energy(-S[i,j], S[i-1, j], JkT) + energy(-S[i,j], S[i, N-1], JkT) + energy(-S[i,j], S[i+1, j], JkT) + \
                       energy(-S[i,j], S[i, j+1], JkT) + BkT * np.sum(S_flipped)
        
        #rightmost column
        elif j == N-1:
            
            #energy in current configuration
            Ecurrent = energy(S[i,j], S[i-1, j], JkT) + energy(S[i,j], S[i, j-1], JkT) + energy(S[i,j], S[i+1, j], JkT) + \
                       energy(S[i,j], S[i, 0], JkT) + BkT * np.sum(S)
            
            #energy of configuration if spin flips
            Enext = energy(-S[i,j], S[i-1, j], JkT) + energy(-S[i,j], S[i, j-1], JkT) + energy(-S[i,j], S[i+1, j], JkT) + \
                       energy(-S[i,j], S[i, 0], JkT) + BkT * np.sum(S_flipped)
            
        else:
            
                #energy in current configuration
                Ecurrent = energy(S[i,j], S[i+1, j], JkT) + energy(S[i,j], S[i, j+1], JkT) + energy(S[i,j], S[i-1, j], JkT) + \
                           energy(S[i,j], S[i, j-1], JkT) + BkT * np.sum(S)
                
                #energy of configuration if spin flips
                Enext = energy(-S[i,j], S[i+1, j], JkT) + energy(-S[i,j], S[i, j+1], JkT) + energy(-S[i,j], S[i-1, j], JkT) + \
                           energy(-S[i,j], S[i, j-1], JkT) + BkT * np.sum(S_flipped)
                               
        #Ratio of weight factors
        r = np.exp(Ecurrent-Enext) #factor of 1/kT is included in Ecurrent and Enext
        
        #Change in energy is negative
        if r >= 1:
            S[i,j] = -S[i,j] #spin flips
            
        #Change in energy is positive    
        else:
            #spin flips with probability r, so we compare r to a random number in [0,1]
            if r >= np.random.rand():
                S[i,j] = -S[i,j] #spin flips
          
    S_next = np.copy(S)
    
    return S_next