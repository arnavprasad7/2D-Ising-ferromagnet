# -*- coding: utf-8 -*-
"""
Energy Function
CO28: Ferromagnetism

Arnav Prasad
Wadham College, Oxford

Created on Thu Nov 29 16:35:35 2018
"""

def energy(Si, Sj, JkT):
    
    E = -JkT * (Si*Sj)
    
    return E