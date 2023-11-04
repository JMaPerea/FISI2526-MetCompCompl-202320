#Multiplicación de matrices de cualquier tamaño
import numpy as np

#Da un array con el tamaño de la matriz (mxn)

def size(matriz):
    m=len(matriz)
    n=0
    for i in matriz:
        n=len(i)
    tamanio=np.array([m,n])     
    return tamanio 

#Multiplica matrices

def multiplicar (matriz_1,matriz_2):
    size_1=size(matriz_1)
    size_2=size(matriz_2)
    result=np.zeros((size_1[0],size_2[1]) )
    transpuesta_2=matriz_2.T
    lista=np.array([])
    #tamaño resultante
    filas_res=size_1[0]
    columnas_res=size_2[1]
    contador=0
    if size_1[1]==size_2[0]:
        for i in matriz_1:
            for j in transpuesta_2:
                operado=i*j
                cada_elemento=np.sum(operado)
                lista=np.append(lista,cada_elemento)
    #Añadir cada elemento de la lista a la matriz resultado
        for l in range (0,filas_res):
            for m in range(0,columnas_res):
                result[l][m]=lista[contador]
                contador+=1
        return result
    else:
        return ("No se puede multiplicar, el numero de columnas de la matriz 1 es",size_1[1],
              "y el numero de filas de la matriz 2 es", size_2[0])
    
matriz_1=np.array([[5,-4,-2],[5,-5,4],[2,5,-4],[-5,4,3],[3,-4,-3]])
matriz_2=np.array([[5],[-2],[-3]])
print(multiplicar(matriz_1, matriz_2)) 

matriz_3=np.array([[0,-1,-1,3],[5,-5,-2,2],[1,0,4,5]])
matriz_4=np.array([[0,-3],[-2,-1],[3,-3]])
print( multiplicar(matriz_3, matriz_4)) 

matriz_5=np.array([[2,-5,5,1],[5,2,-7,6],[-6,-1,7,-4],[5,4,1,-5]])
matriz_6=np.array([[0,4,-7,1,-6],[-1,-6,-5,1,1],[2,-1,-6,5,-5],[-3,-6,6,3,5]])

print( multiplicar(matriz_5, matriz_6)) 


# Punto 2:
matriz_7=np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz_8=np.array([[7,8,9],[4,5,6],[1,2,3]])
print("punto 2")
print("la matriz 1 es:")
print(matriz_7)
print("la matriz 2 es:")
print(matriz_8)
print("si multiplicamos la matriz 1 por la matriz 2 da como resultado:")
print( multiplicar(matriz_7, matriz_8)) 
print("si multiplicamos la matriz 2 por la matriz 1 da como resultado:")
print( multiplicar(matriz_8, matriz_7)) 

