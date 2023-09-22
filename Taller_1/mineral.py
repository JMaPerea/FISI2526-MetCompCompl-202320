# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:32:28 2023

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
from IPython.display import display



class mineral:
    def __init__(self, nombre,dureza,lustre,rompimiento_por_fractura,color,composicion
                 ,sistemacr, gravedadesp,):
        self.nombre=nombre
        
        self.dureza=dureza
        
        self.lustre=lustre
        
        self.rompimiento_por_fractura=rompimiento_por_fractura
    
        self.color=color
    
        self.composicion=composicion
        
        self.sistemacr=sistemacr
        
        self.gravedadsp=gravedadesp
        
    
    def silicato(self):
        if 'Si' and 'O' in self.composicion:
            return True
        else:
            return False
    def densidad_si(self):
        den=self.gravedadsp*997
        return den
    def color_si(self):
        figure, axes = plt.subplots()
        Drawing_colored_circle = plt.Circle(( 0.8 , 0.8 ) , color=self.color)
         
        axes.set_aspect( 1 )
        axes.add_artist( Drawing_colored_circle )
        plt.title( 'Color' )
        plt.show()
        return print(self.color)
    def var_par(self):
        d=self.dureza
        r=self.rompimiento_por_fractura
        c=self.sistemacr
        if c == True:
            c='Se rompe por fractura'
        else:
            c='No se rompe por fractura'
        return f'dureza: {d} Tipo de rompimiento: {r} sistema de organización: {c}'


    
    