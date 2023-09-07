# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def lect(ruta):
    f=open(ruta)
    txt=f.read() 
    f.close()
    lstu=txt.split('data: |\n')[1].split('\nSPECS')[0].split('  - type')[0].strip().split('\n        ')
    lstf=[]
    for k in lstu:
        texto = k.split(' ')
        texto[0] = float(texto[0])
        texto[1] = float(texto[1])
        lstf.append(tuple(texto))

    
    return lstf

lista_elementos = pd.read_csv('./indices_refraccion.csv')
lista_rutas_yml = lista_elementos['Categoría']+'/'+lista_elementos['Material']+'.yml'
print(lista_rutas_yml)
for f in lista_rutas_yml.values:
    lect(f)
#print(lect("Adhesivos Ópticos/Iezzi.yml"))
    
    