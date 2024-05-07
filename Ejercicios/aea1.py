tableroSudoku1=[
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
tableroSudoku2=[
    [5,3,9,8,7,6,4,1,2],
    [7,2,8,3,1,4,9,6,5],
    [6,4,1,2,9,5,7,3,8],
    [4,6,2,5,3,9,8,7,1],
    [3,8,5,7,2,1,6,4,9],
    [1,9,7,4,6,8,2,5,3],
    [2,5,6,1,8,7,3,9,4],
    [9,1,3,6,4,2,5,8,7],
    [8,7,4,9,5,3,1,2,6]
]
tableroSudoku3=[
    [5,3,9,8,7,6,4,1,1],
    [7,2,8,3,1,4,9,6,5],
    [6,4,1,2,4,5,7,3,8],
    [4,6,2,5,3,9,8,7,1],
    [3,8,5,7,2,1,6,4,9],
    [1,9,7,4,6,8,2,5,3],
    [2,5,6,1,8,3,3,9,4],
    [9,1,3,6,4,2,5,8,7],
    [8,7,4,9,5,3,1,2,6]
]

tablero3EnRaya1=[
    ['X','X','O'],
    ['','X','O'],
    ['','','O'],
]
tablero3EnRaya2=[
    ['X','O','X'],
    ['O','X','O'],
    ['O','X','O'],
]
tablero3EnRaya3=[
    ['X','X','O'],
    ['O','O','X'],
    ['O','O','X'],
]

def comprobar3EnRaya(tablero):
    #no me ha dado tiempo a reducir el codigo ni quitar los bucles, me lié con el sudoku :( al ver que no funcionaba el problema del print que tuve lo cambié todo varias veces y se ha tenido que quedar así.
    for i in range (len(tablero)):
        for j in range (len(tablero)):
            """
            Comprobamos las verticales en busca de 3 simbolos iguales consecutivos
            """
            if tablero [0][2]== 'X' and tablero [1][2]== 'X' and tablero [2][2] == 'X': 
                print("gana la x en la última vertical")
                break
            if tablero [0][2]== 'O' and tablero [1][2]== 'O' and tablero [2][2] == 'O': 
                print("gana la O en la última vertical")
                break
            if tablero [0][1]== 'X' and tablero [1][1]== 'X' and tablero [1][0] == 'X': 
                print("gana la x en la vertical central")
                break
            if tablero [0][1]== 'O' and tablero [1][1]== 'O' and tablero [1][0] == 'O': 
                print("gana la O en la vertical central")
                break
            if tablero [0][0]== 'X' and tablero [1][0]== 'X' and tablero [2][0] == 'X': 
                print("gana la x en la primera vertical")
                break
            if tablero [0][0]== 'O' and tablero [1][0]== 'O' and tablero [2][0] == 'O': 
                print("gana la O en la primera vertical")
                break
            """
            Comprobamos las horizontales en busca de 3 simbolos iguales consecutivos

            """
            if tablero [0][0]== 'X' and tablero [0][1]== 'X' and tablero [0][2] == 'X': 
                print("gana la x en la primera horizontal")
                break
            if tablero [0][0]== 'O' and tablero [0][1]== 'O' and tablero [0][2] == 'O': 
                print("gana la O en la primera horizontal")
                break
            if tablero [1][0]== 'O' and tablero [1][1]== 'O' and tablero [1][2] == 'O': 
                print("gana la O en la horizontal central")
                break
            if tablero [1][0]== 'X' and tablero [1][1]== 'X' and tablero [1][2] == 'X': 
                print("gana la x en la horizontal central")
                break
            if tablero [2][0]== 'O' and tablero [2][1]== 'O' and tablero [2][2] == 'O': 
                print("gana la O en la última horizontal")
                break
            if tablero [0][0]== 'X' and tablero [1][0]== 'X' and tablero [2][0] == 'X': 
                print("gana la x en la última horizontal")
                break
            """
            Comprobamo la diagonal en busca de 3 simbolos iguales consecutivos

            """            
            if tablero [2][0]== 'O' and tablero [1][1] == 'O' and tablero [0][2] == 'O':
                print("gana la O en la diagonal")
                break
            if tablero [2][0]== 'X' and tablero [1][1] == 'X' and tablero [0][2] == 'X':
                print("gana la X en la diagonal")
                break 
            #si no se cumplen las condiciones quiere decir que la partida queda en tablas              
            else:
                print("la partida queda en tablas")

def comprobarSudoku(tablero):
    numeros=[1,2,3,4,5,6,7,8,9]
    parte1=[[[tablero[0][0]],[tablero[0][1]],[tablero[0][2]]],
            [[tablero[1][0]],[tablero[1][1]],[tablero[1][2]]],
            [[tablero[2][0]],[tablero[2][1]],[tablero[2][2]]],
            ]
    parte2=[[[tablero[0][3]],[tablero[0][4]],[tablero[0][5]]],
            [[tablero[1][3]],[tablero[1][4]],[tablero[1][5]]],
            [[tablero[2][3]],[tablero[2][4]],[tablero[2][5]]],
            ]
    parte3=[[[tablero[0][6]],[tablero[0][7]],[tablero[0][8]]],
            [[tablero[1][6]],[tablero[1][7]],[tablero[1][8]]],
            [[tablero[2][6]],[tablero[2][7]],[tablero[2][7]]],
            ]
    
    
    for i in range (len(tablero)):
        for j in range (len(tablero)):
            for x in range (len(numeros)): 
                for y in range(len (parte1)):
                    if numeros in parte1[y]:
                        print("estan en esta seccion") 
                    else:  
                        print("No")      
                #if  tablero [i][0] in numeros:
                 #   print("tenemos los numeros") 
                #if tablero [0][j] in numeros:
                #    print("tenemos los numeros")
                if numeros[x]==tablero[i][0]:
                    print("en esta columna no estan o se repiten numeros")
                else:
                    print("en esta columna estan estan todos los numeros")
                      
                                       
         
comprobar3EnRaya(tablero3EnRaya1)      
comprobar3EnRaya(tablero3EnRaya2)
comprobar3EnRaya(tablero3EnRaya3)
comprobarSudoku(tableroSudoku2)
