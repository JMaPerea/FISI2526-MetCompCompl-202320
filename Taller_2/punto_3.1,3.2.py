# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:11:25 2023

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import math

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLaguerreRecursive(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*(n-1)+1-x)*GetLaguerreRecursive(n-1, x)-(n-1)*GetLaguerreRecursive(n-2, x))/n
   
    return sym.expand(poly,x)

def GetDLaguerre(n,x):
    Pn = GetLaguerreRecursive(n,x)
    return sym.diff(Pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn

def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGLag(n):

    xn = np.linspace(0,n+((n-1)*np.sqrt(n)),100)
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerreRecursive(i,x))
        DLaguerre.append(GetDLaguerre(i,x))
    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)

    

    DLaguerre = []
    
    for i in range(n+1):
        DLaguerre.append(GetDLaguerre(i,x))
    
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights

def GetHermiteRecursive(n,x):

    if n==0:
        poly = 1
    elif n==1:
        poly = 2*x
    else:
        poly = 2*x*GetHermiteRecursive(n-1, x)-((2*n-2)*GetHermiteRecursive(n-2, x))
   
    return sym.expand(poly,x)

def GetDHermite(n,x):
    Pn = GetHermiteRecursive(n,x)
    return sym.diff(Pn,x,1)


def GetAllRootsGHerm(n):

    xn = np.linspace(-np.sqrt(4*n+1),np.sqrt(4*n+1),100)
    
    Hermite = []
    DHermite = []
    
    for i in range(n+1):
        Hermite.append(GetHermiteRecursive(i,x))
        DHermite.append(GetDHermite(i,x))
    
    poly = sym.lambdify([x],Hermite[n],'numpy')
    Dpoly = sym.lambdify([x],DHermite[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGHerm(n):

    Roots = GetAllRootsGHerm(n)

    

    DHermite = []
    
    for i in range(n+1):
        DHermite.append(GetDHermite(i,x))
    
    Dpoly = sym.lambdify([x],DHermite[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights


print("raices Laguerre  ",GetAllRootsGLag(3))
print("pesos Laguerre  ",GetWeightsGLag(3))
print("polinomio laguerre",GetLaguerreRecursive(3, x))


print("raices Hermite ",GetAllRootsGHerm(3))
print("pesos Hermite  ", GetWeightsGHerm(3))
print("polinomio Hermite",GetHermiteRecursive(3, x))