# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:28:37 2023

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import math

def newton_raphson(func, derivada, posibles, tolerance=1e-6, max_iterations=100):
    x = posibles
    
    for i in range(max_iterations):
        
        f_x = func(x)
        
        if abs(f_x) < tolerance:
            
            return x
        
        f_prime_x = derivada(x)
        
        if f_prime_x == 0:
            
            raise ValueError("Derivative is zero. Newton-Raphson cannot proceed.")
            
        x = x - f_x / f_prime_x
        
    raise Exception("Newton-Raphson did not converge")
    

t=sym.Symbol('t',real=True)

Time=np.linspace(0,0.2,num=100)

Bo=0.05

omega=3.5

f=7

r=0.25

R=1.75

Flux=np.pi*r**2*sym.cos(omega*t)*sym.cos(2*np.pi*f*t)

DFlux=sym.diff(Flux)

Ir=(-1/R)*DFlux

DIr=sym.diff(Ir)

Ir=sym.lambdify(t,Ir)

DIr=sym.lambdify(t,DIr)

Flux=sym.lambdify(t,Flux)

posibles=[0,0.06,0.16]

zeroes=[]
for i in posibles:
    z=newton_raphson(Ir, DIr, i)
    zeroes.append(z)


print(f'Los primeros 3 puntos de t en los cuales  I=0 son {zeroes}')
#plt.plot(Time,Flux(Time),color='black',)
plt.scatter(zeroes,np.zeros(3))
plt.plot(Time,Ir(Time),color="red")
plt.legend(['I=0','Corriente'])
plt.xlabel('Tiempo(s)')
plt.ylabel('Corriente')
plt.show()