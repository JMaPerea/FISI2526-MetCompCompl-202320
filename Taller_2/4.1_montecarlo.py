#Monte Carlo
import matplotlib.pyplot as plt
import numpy as np
#N = 1000000
limite_inferior = 0
limite_superior = np.pi
def funcion_a_integrar(x):
    return np.exp(-x)*np.sin(x)
Integral_teorica=0.5*(1+np.exp(-np.pi))
"""EJERCICIO 4.1"""

def Error_vs_N(): 
    Error_segun_n=np.array(0)
    for i in range(1,10000):
        Numeros_random=np.random.uniform(limite_inferior,limite_superior,i)
        f_i=funcion_a_integrar(Numeros_random)
        integ= (limite_superior-limite_inferior)* sum(f_i) /i
        error_porcentual=np.abs(1-integ/Integral_teorica)*100
        Error_segun_n=np.append(Error_segun_n, error_porcentual)
        print("I va por",i)
    return Error_segun_n

"""Graficar"""
#y son los distintos errores encontrados para cada N
y=Error_vs_N()[1:]
# x son los distintos N
x=np.arange(1,10000)
#Cota superior
def cota(x):
    return 1/np.sqrt(x)
ci=cota(x) #Array con los valores de 1/raiz de n para todo n es decir "y"
#cada n seria x
"""    
plt.plot(x,y,linewidth=2,color='b')
plt.plot(x,ci,"-",linewidth=2,color='g')
plt.xlabel('Valores de N')
plt.ylabel('Error  porcentual')
plt.title('')
plt.show()"""

plt.plot(x,y,linewidth=2,color='b')
plt.plot(x,ci,"-",linewidth=2,color='k')

# Ajustar el orden de dibujo
plt.gca().set_zorder(plt.gca().get_zorder() + 1)
plt.plot(x, ci,linewidth=3, color='red',label=' cota (1/N^(1/2)')
# Etiquetas y leyenda
plt.xlabel('Valores de N')
plt.ylabel('Error  porcentual')
plt.title('')
plt.legend()
plt.show()

#Solo error porcntual
plt.plot(x,y,linewidth=2,color='b')
# Etiquetas y leyenda
plt.xlabel('Valores de N')
plt.ylabel('Error  porcentual')
plt.title('Error porcentual vs N')
plt.show()

#Solo cota

plt.plot(x,ci,"-",linewidth=2,color='red',label=' cota (1/N^(1/2)')
plt.xlabel('Valores de N')
plt.ylabel('Error  porcentual')
plt.title('')
plt.legend()
plt.show()

"""
Calculando integrales de orden superior

¿Cómo se relaciona con el método de MonteCarlo?
En este experimento se aproxima una solucion a problemas matemáticos complejos 
mediante la generación de números aleatorios.que es precisamente el objetivo del
metodo de monte carlo, para nuestro ejercicio 4.1 queremos aproximar una integral
y para el experimento del video quieren aproximar pi.

¿Cómo recrear el experimento utilizando Python?
Se puede recrear como se muestra en el ejemplo, generando números aleatorios que
estén en cierto rango, (un cuadrado de lado 2r). Cuando un numero esté dentro del
circulo entonces sumamos 1. a partir de esto podemos usar la formula para aproximar
una integral, esta es:
b-a*la suma/ N. siendo N el número de datos aleatorios.(los dardos del video)

"""
