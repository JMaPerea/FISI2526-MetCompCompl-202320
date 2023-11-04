# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:26:04 2023

@author: ADMIN
"""

import sympy as sym
import numpy as np

c1, c2, c3 =sym.symbols('c1 c2 c3')
m1, m2, m3 =sym.symbols('m1 m2 m3')
k11, k12, k13 =sym.symbols('k11 k12 k13')
k21, k22, k23 =sym.symbols('k21 k22 k23')
k31, k32, k33 =sym.symbols('k31 k32 k33')
#s=(m1,m2,m3,k11,k12,k13,k21,k22,k23,k31,k32,k33)

#print(k13)
M=sym.Matrix([[k11/m1,k12/m1,k13/m1],[k21/m2,k22/m2,k23/m2],[k31/m3,k32/m3,k33/m3]])
v=sym.Matrix([c1,c2,c3])

#vect=M.eigenvects()

iterac=5

valor=[]
for i in range(iterac):
    
    if i==0:
        vant=v
        c=M**i*v
    else:
        vant=c
    
        c=M**i*c
    value=c[0]/vant[0]
    valor.append(value)
#print(valor)
sym.init_printing(use_latex=True)        

