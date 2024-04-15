"""
Crear un tablero de 10x10 con una pieza que empiece en el centro y que se mueva hasta salirse por los huecos del tablero.
Las paredes se representan con | y los espacios del tablero con _   

"""
"""
|                       |
|                       |
|                       |
|                       |
|                       |

"""

import random as rd

tablero=[["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],
         ["|","_","_","_","_","_","_","_","_","|"],         
         ]


def moverBola(bola):
      
 
    while(True):
        movimiento=rd.choice(vectores)  
        mostrarTablero() 
        print(bola)
        bola[0] += movimiento[0]
        bola[1] += movimiento[1]
        
        if bola[0] > 0 and bola [1]>0 and bola[0]<len(tablero) and bola[1]<len(tablero):
            
            if tablero[bola[0]][bola[1]] == "|":
                bola[0] -= movimiento[0]
                bola[1] -= movimiento[1]
                continue
            else:
                continue
        else:
            break
            
def mostrarTablero():
    tablero[bola[0]][bola[1]]="B"
    for i in range (len(tablero)):
        print(tablero[i])
        
bola = [5,5]
vectores = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[1,1]]

moverBola(bola)   




        
