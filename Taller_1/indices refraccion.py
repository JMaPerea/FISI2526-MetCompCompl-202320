# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.constants as cnst

lista_elementos = pd.read_csv('./indices_refraccion.csv')
lista_rutas_yml = lista_elementos['Categoría']+'/'+lista_elementos['Material']+'.yml'
lista_de_nombres = lista_elementos['Material']

def lect(ruta: str):
    
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

def ind_ref_longo(nombre,valores: list):
    x=[]
    y=[]
    c=cnst.c
    for i in valores:
        x.append(i[0])
        refr=c/i[1]
        y.append(refr)
    plt.plot(x,y, color='red')
    plt.title(nombre)
    plt.xlabel("Longitud de onda")
    plt.ylabel("Indice de refracción")
    plt.grid()
    
    return 
print(ind_ref_longo("NOA1348.yml",lect("Adhesivos Ópticos/NOA1348.yml")))


for f,g in zip(lista_rutas_yml,lista_de_nombres):
    #print(lect(f))
    ind_ref_longo(g, lect(f))
    plt.show()
   
   
   
#print(lect("Adhesivos Ópticos/NOA1348.yml"))

    
    