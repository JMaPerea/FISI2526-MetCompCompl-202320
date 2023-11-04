# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:06:29 2023

@author: ADMIN
"""

import numpy as np


A = np.array([[3,1,-1],
     [1,-2,1],
     [4,-1,1]])
b = np.array([2,0,3])

def gaussian_elimination(A: np.array,b: np.array):
    
    nlin=len(A)
    ncol=len(A[0])
    
    for i in range(nlin):
        for j in range(ncol):
            val=A[j][i]
            #print(val)
            
            if i==j:
                
                
                if i+1<nlin:
                    valb1=b[j+1]
                    if val==0 and A[j+1][i]!=0:
                        A[j]=A[j+1]
                        val=A[j][i]
                        b[j]=b[j+1]    
                        valb=[j+1]
                    sig1=A[j+1][i]
                    #print(sig1)
                    coeff1=sig1/val
                    #print(coeff1)
                    newline1=A[j+1]-A[j]*coeff1
                    #print(newline1)
                    A[j+1]=newline1
                    
                    newvalb1=valb1-b[j]*coeff1
                    b[j+1]=newvalb1
                    
            
                if i+2<nlin:
                    sig2=A[j+2][i]
                    #print(sig2)
                    coeff2=sig2/val
                    #print(coeff2)
                    newline2=A[j+2]-A[j]*coeff2
                    #print(newline2)
                    A[j+2]=newline2
                    valb2=b[j+2]
                    newvalb2=valb2-b[j]*coeff2
                    b[j+2]=newvalb2
    B=b                
    b=b[np.newaxis]
    
    
    M=np.append(A,b.T, axis=1)
        
        
              
    return A,B,M
print("La matriz triangular ascociada al problema A es:\n",gaussian_elimination(A, b)[2])
tri=gaussian_elimination(A, b)
x=np.linalg.solve(tri[0],tri[1])

print(f"Las tres fuerzas son: \n F1={x[0]}, F2={x[1]}, F3={x[2]}")

C=np.array([[1,1,1],[0,-8,10],[4,-8,0]])
d=np.array([0,0,6])

print("La matriz triangular ascociada al problema B es:\n", gaussian_elimination(C, d)[2])
tri2=gaussian_elimination(C, d)
x=np.linalg.solve(tri2[0],tri2[1])
print(f"Las tres corrientes son: \n Ia={x[0]}, Ib={x[1]}, Ic={x[2]}")