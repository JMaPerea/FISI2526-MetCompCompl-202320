# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:15:25 2023

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
from mineral import mineral

data= pd.read_csv('minerales.csv')
minerales=[]

for i in range(len(data)):
    nom=data.iloc[i]['nombre']
    dur=data.iloc[i]['dureza']
    lustre=data.iloc[i]['lustre']
    rompfr=data.iloc[i]['rompimiento_por_fractura']
    clr=data.iloc[i]['color']
    comp=data.iloc[i]['composicion']
    gravsp=data.iloc[i]['specific_gravity']
    sistemacr=data.iloc[i]['sistema cristalino']
    minerales.append(mineral(nom,dur,lustre,rompfr,clr,comp,sistemacr,gravsp))

sum_densidad=0
silicatos=0
# pru=minerales[14]

# print(pru.var_par())
for i in minerales:
    f=i.silicato()
    if f ==True:
        silicatos=silicatos+1
    sum_densidad=sum_densidad+i.densidad_si()
    

#print(sum_densidad/len(minerales))