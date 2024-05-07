import random as rd

"""
Juego del pacman sin menu, ni obstaculos unicamente el tablero de 8x8 y 5 fantasmas 
con posicion aleatoria.    
"""

#creamos el tablero de 8x8

tablero = [["_" for i in range(8)] for j in range(8)]

#definimos los vectores de movimiento de PACMAN

vectores = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]

#definimos las posiciones aleatorias de los 5 fantasmas

for i in range(5):
    x = rd.randint(0,7)
    y = rd.randint(0,7)
    if tablero[x][y] == "F":
        continue
    tablero[x][y] = "F"
        
#definimos a pacman en una posicion aleatoria

pacmanX = rd.randint(0,7)
pacmanY = rd.randint(0,7)
tablero[pacmanX][pacmanY] = "P"

#hacemos que pacman se mueva en las direcciones de los vectores hasta chocar con un fantasma

   
   
#mostramos el tablero

for i in range(0,len(tablero)):
    for j in range(0,len(tablero)):
        print(tablero[i][j],end=" ")
    print() 

        
            
            
