# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:53:00 2023

@author: POWER
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import math
x=sym.Symbol('x',real=True)

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

    

    poly = sym.lambdify(x,GetLaguerreRecursive(n+1, x))   

    Weights = Roots / ((n+1)**2*(poly(Roots)**2))
    
    
    return Weights

def estimar_integral(ck,xk,func,n):
    sol=0
    
    for i in range(n):
        val=ck[i]*func(xk[i])
        sol=sol+val
        
    return sol




#Si excluimos todas las constantes de la integral asumiendo valores para M,R,T
Pvu=lambda u: u*np.exp(-u)
k=5
ck=GetWeightsGLag(k)
xk=GetAllRootsGLag(k)

Valor=estimar_integral(ck, xk, Pvu,k)
print('Punto 1')
print(f'Valor estimado de la integral: {Valor}')


#asumiendo hirogeno monoatomico
T=np.linspace(100,1000,num=10)
M=1.00784
R=8.3145
v=np.linspace(0,100,100)


for i in T:
    Pv= lambda v: 4*np.pi*(M/(2*np.pi*R*i))**(3/2)*v**2*(np.exp(-(M*v**2)/(2*R*i)))
    plt.plot(v,Pv(v))
    plt.plot(v,Pv(v), label=f'Temp = {i} K')
plt.xlabel('Velocidad (m/s)')
plt.ylabel('(p(v))')
plt.title('Maxwell-Boltzmann Hidrogeno')
plt.legend()
plt.grid(True)
plt.show()
    

print('Punto 3')
vvalue=[]
for i in T:
    Pv= lambda u: np.sqrt((2*R*i*u)/(M))*4*np.pi*(M/(2*np.pi*R*i))**(3/2)*((2*R*i*u)/(M))*np.exp(-u)
    sol=estimar_integral(ck, xk, Pv, k)
    vvalue.append(sol)
    print(f'El valor de la velocidad promedio en {i}K es: {sol}')

plt.plot(T,vvalue)
plt.title('Valores Calculados (Hidrogeno)')
plt.xscale('log')
plt.xlabel('Temp (K)')
plt.ylabel('v avg')
plt.grid(True)
plt.show()


vavg= lambda T: np.sqrt((8*R*T)/(np.pi*M))
plt.plot(T,vavg(T))
plt.xscale('log')
plt.title('Valores Teorícos (Hidrogeno)')
plt.xlabel('Temp (K)')
plt.ylabel('v avg')
plt.grid(True)
plt.show()   
    

    



