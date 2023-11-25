# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:04:53 2023

@author: POWER
"""

import sympy as sym
import numpy as np

N = int(1e6)
evento_se_cumplio = 0

for i in range(N):
    cartas = np.arange(1, 53)
    np.random.shuffle(cartas)
    cartas_tomo = cartas[:5]

    primeras_2=cartas_tomo[:2]
    
    num_espadas_primera=np.sum(primeras_2[:2]%13 ==1)
    #print(num_espadas_primera)
    

    if num_espadas_primera == 2:
        num_espadas_siguientes = np.sum(cartas_tomo[2:] % 13 == 1)
        #print(cartas_tomo[:3])

        if num_espadas_siguientes == 0:
            evento_se_cumplio += 1


probabilidad = evento_se_cumplio / N
print("1a Probabilidad:", probabilidad)



evento_se_cumplio = 0

for i in range(N):
    cartas = np.arange(1, 53)
    np.random.shuffle(cartas)
    cartas_tomo = cartas[:5]

    primeras_3=cartas_tomo[:3]
    
    num_espadas_primera=np.sum(primeras_3[:3]%13 ==1)
    #print(num_espadas_primera)
    

    if num_espadas_primera == 2:
        num_espadas_siguientes = np.sum(cartas_tomo[3:] % 13 == 1)
        #print(cartas_tomo[2:])

        if num_espadas_siguientes == 0:
            evento_se_cumplio += 1


probabilidad = evento_se_cumplio / N
print("1b Probabilidad:", probabilidad)

evento_se_cumplio = 0

for i in range(N):
    cartas = np.arange(1, 53)
    np.random.shuffle(cartas)
    cartas_tomo = cartas[:5]

    primeras_4=cartas_tomo[:4]
    
    num_espadas_primera=np.sum(primeras_4[:4]%13 ==1)
    #print(num_espadas_primera)
    

    if num_espadas_primera == 2:
        num_espadas_siguientes = np.sum(cartas_tomo[4:] % 13 == 1)


        if num_espadas_siguientes == 0:
            evento_se_cumplio += 1

probabilidad = evento_se_cumplio / N

print("1c Probabilidad:", probabilidad)








