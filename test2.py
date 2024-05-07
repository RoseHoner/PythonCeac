""" 
crea un juego que a partir de una matriz de 8x8
y desde el centro se vayan añadiendo figuras (x)(y) aleatoriamente
de tal modo que solo se puedan generar a partir de la primera
en cualquier dirección. el juego termina cuando hay 3 figuras iguales 
situadas consecutivamente.
"""
import random as rd
tablero=[["_" for i in range(8)] for j in range(8)]
figuras=["X","Y"]
vectores=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
posI=[4,4]

def posicionInicial(posI):
    eleccion=rd.choice(figuras)
    for i in range (len(tablero)):
        tablero[posI[0]][posI[1]]=eleccion
        print(tablero[i])
def jugar():
    juego=True
    while juego:
        movimiento=rd.choice(vectores)  
        eleccion=rd.choice(figuras)   
        posI[0]+=movimiento[0]
        posI[1]+=movimiento[1]
        tablero[posI[0]][posI[1]]=eleccion
        if posI[0]<1 or posI[1]<1 or posI[0]>6 or posI[1]>6:
            posI[0]-=movimiento[0]
            posI[1]-=movimiento[1]
            if tablero [posI[0]][posI[1]]!="_":
                posI[0]+=movimiento[0]
                posI[1]+=movimiento[1]
                                         
        for i in range (len(tablero)):
            tablero[posI[0]][posI[1]]=eleccion
            print(tablero[i])
        print()    
posicionInicial(posI)
jugar()
    