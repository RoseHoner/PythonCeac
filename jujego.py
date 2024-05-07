"""
crea una matriz de 10x10 y crea el juego de la pelota 
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
bola=[5,5]
vectores=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

def moverBola(bola):
    #tablero[bola[0]][bola[1]]="O"
    while (True):
        movimiento=rd.choice(vectores)
        bola[0]+=movimiento[0]
        bola[1]+=movimiento[1]
        if bola [0]<0 or bola [1]<0 or bola[0]>9 or bola[1]>9:
            bola[0]-=movimiento[0]
            bola[1]-=movimiento[1]
            if tablero [bola[0]][bola[1]]=="|":
                bola[0]-=movimiento[0]
                bola[1]-=movimiento[1]
            else:
                print("la bola salio, perdiste")
                break
        else:
            continue
        
        
def imprimirtablero():
    for i in range(len(tablero)):
        tablero[bola[0]][bola[1]]="O"
        print(tablero[i])
        
 
       
moverBola(bola)
imprimirtablero()

      
        
                    