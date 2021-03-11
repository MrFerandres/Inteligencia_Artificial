"""
Fernando Andres Chavez Gavaldon
Juego del 15
"""

import numpy as np
import random

#Imprime el estado inicial del juego (resuelto)
def inicio(estado):
    for i in range(15):
        estado[i]=i+1
    estado[15] = 0
    return estado

#imprime el estado actual de la partida
def PTablero(tablero):
    print("\n\n-------------------")
    for i in [0, 4, 8, 12]:
        print("||%2d||%2d||%2d||%2d||" % (tablero[i], tablero[i + 1], tablero[i + 2], tablero[i + 3]))
        print("-------------------")

#hace la accion de mover la ficha vacia (0) a la pocision que se desea
def juego(tablero,accion="SA"):
    ubicacion=np.where(tablero==0)[0]
    #print(ubicacion)
    if accion=="SA":
        PTablero(tablero)

    elif accion == "u" and ubicacion !=0 and ubicacion !=1 and ubicacion !=2 and ubicacion != 3:
        #print("ariba si se pudo")
        aux=tablero[ubicacion-4]
        tablero[ubicacion-4]=0
        tablero[ubicacion]=aux

        PTablero(tablero)

    elif accion == "d" and ubicacion != 15 and ubicacion != 14 and ubicacion != 13 and ubicacion != 12:
        #print("abajo si se pudo")
        aux=tablero[ubicacion+4]
        tablero[ubicacion+4]=0
        tablero[ubicacion]=aux

        PTablero(tablero)

    elif accion == "l" and ubicacion !=0 and ubicacion != 4 and ubicacion != 8 and ubicacion != 12:
        #print("izquierda si se pudo")
        aux=tablero[ubicacion-1]
        tablero[ubicacion-1]=0
        tablero[ubicacion]=aux

        PTablero(tablero)

    elif accion == "r" and ubicacion !=3 and ubicacion !=7 and ubicacion !=11 and ubicacion !=15:
        #print("derecha si se pudo")
        aux=tablero[ubicacion+1]
        tablero[ubicacion+1]=0
        tablero[ubicacion]=aux

        PTablero(tablero)

    else:
        print("No se pudo ninguna accion, porfavor repita la accion")

    return tablero

def aleatoriedad(argumento):
    switcher = {
        1: "u",
        2: "d",
        3: "l",
        4: "r"
    }
    return switcher.get(argumento, "nothing")

#inicia el main

tablero = np.zeros(16)
tablero = inicio(tablero)
tablero = juego(tablero)

#Descomponemos el tablero
for j in range(1000):
    aleatorio = random.randint(1,4)
    aleatorio = aleatoriedad(aleatorio)
    tablero = juego(tablero,aleatorio)


while True:
    accion = input("u=Up \nd=Down \nl=Left \nr=Right \nexit=salir\n")
    if accion == "exit": break
    tablero = juego(tablero,accion)

