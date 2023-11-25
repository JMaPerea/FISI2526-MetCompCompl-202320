# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 23:00:31 2023

@author: POWER
"""

import numpy as np


prob_exposicion = 0.6
prob_exito_inoculado = 0.8
prob_exito_no_inoculado = 0.9

N = int(1e6) 


ambas_enfermas = 0
solo_primera_enferma = 0
solo_segunda_enferma = 0

for i in range(N):

    expuesta_inoculado = np.random.rand() < prob_exposicion
    expuesta_no_inoculado = np.random.rand() < prob_exposicion


    enferma_inoculado = expuesta_inoculado and (np.random.rand() > prob_exito_inoculado)
    enferma_no_inoculado = expuesta_no_inoculado and (np.random.rand() > prob_exito_no_inoculado)


    if enferma_inoculado and enferma_no_inoculado:
        ambas_enfermas += 1
    elif enferma_inoculado:
        solo_primera_enferma += 1
    elif enferma_no_inoculado:
        solo_segunda_enferma += 1


probabilidad_al_menos_una_enferma = (ambas_enfermas + solo_primera_enferma + solo_segunda_enferma) / N

print("Probabilidad:", probabilidad_al_menos_una_enferma)
