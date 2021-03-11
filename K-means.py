"""
Fernando Andres Chavez Gavaldon
Codigo para hacer K-means
"""

#biblotecas
import numpy as np
import random as rn
import math as mt
from matplotlib import pyplot as plt

#adquisicion de valores
numeros = int(input("Ingresa el numero de valores a agrupar con k-mean: \n"))
dim = 2
print('Ingrese la cantidad de categorias (mayor a 2 y menor a {} )'.format(numeros-1))
cat = int(input())

#creacion de vectores para su uso
datos = np.zeros(dim*numeros) #todos los datos randoms

banderas = []  #las banderas de en que categoria esta


for i in range(len(datos)): #creacion de los valores randoms
    datos[i] = rn.uniform(-10,10)
    #datos[i] = rn.randint(-10,10)

for i in range(numeros):            #asociacion de las banderas y garantiza que en siempre tenga 1 en todas
    banderas.append(i % cat)

#print(datos[0:int(len(datos)/2)],"\n",datos[int(len(datos)/2):int(len(datos))],"\n\n",datos, prom)
print(datos, "\n\n", banderas, "\n")


while True:
    prom = np.zeros(cat * dim)  # los promedios de los valores de las distancias que estan en ese lugar
    cantidad = np.zeros(cat * dim)  # ayuda para sacar el promedio

    bandcamb = banderas.copy()
    for i in range(len(datos)): #calcula los promedios
        for j in range(cat):
            if i < numeros:
                if banderas[i] == j:
                    prom[j] = prom[j]+datos[i]
                    cantidad[j] += 1
                    #print(i,j,"\n")
            else:
                if banderas[i-numeros] == j:
                    prom[j+cat] = prom[j+cat] + datos[i]
                    cantidad[j+cat] += 1
                    #print(i,j,"\n")
    #print("\n",cantidad)

    for i in range(len(prom)):
        if cantidad[i]!= 0:
            prom[i] = prom[i]/cantidad[i]
        else:
            prom[i] = 0

    #print(prom)

    for i in range(int(len(datos)/2)): #verifica si es la distancia mas corta y si la es cambia su bandera
        comparacion = pow(datos[i] - prom[0], 2) + pow(datos[i+numeros] - prom[cat], 2)
        comparacion = mt.sqrt(comparacion)
        #print(comparacion)

        for j in range(cat):
            comparacion2 = pow(datos[i]-prom[j], 2)+pow(datos[i+numeros] - prom[j+cat],2)
            comparacion2 = mt.sqrt(comparacion2)
            #print(i,"------",j,"------",i+numeros,"------",j+cat)
            #print("sqrt-",datos[i],"-",prom[j],"^2 + ",datos[i+numeros],"-",prom[j+cat],"^2 - = ", comparacion2,"<?",comparacion, "     tamos en",j )
            if j == 0:
                banderas[i] = 0
            if comparacion2 < comparacion:
                #print("Entro en el if  ",j,"\n")
                comparacion = comparacion2
                banderas[i] = j

    #print(banderas,"\n",bandcamb)
    if banderas == bandcamb:
        break

plt.figure(1)


for i in range(numeros):
    if banderas[i] == 0:
        plt.plot(datos[i], datos[i + numeros], 'bo')
    elif banderas[i] == 1:
        plt.plot(datos[i], datos[i + numeros], 'go')
    elif banderas[i] == 2:
        plt.plot(datos[i], datos[i + numeros], 'ro')
    elif banderas[i] == 3:
        plt.plot(datos[i], datos[i + numeros], 'ko')
    elif banderas[i] == 4:
        plt.plot(datos[i], datos[i + numeros], 'mo')
    elif banderas[i] == 5:
        plt.plot(datos[i], datos[i + numeros], 'yo')
    elif banderas[i] == 6:
        plt.plot(datos[i], datos[i + numeros], 'co')
    elif banderas[i] == 7:
        plt.plot(datos[i], datos[i + numeros], 'wo')

for i in range(int(len(prom)/2)):
    print('punto {}: {} , {}  '.format(i, prom[i], prom[i+cat]))
    plt.plot(prom[i], prom[i+cat], 'x')

plt.show()



