from ficha import Ficha

class Tablero:
    def __init__(self,equipo1,equipo2):
        self.fila=6
        self.columna=7
        self.equipo1=equipo1
        self.equipo2=equipo2
        self.tablero=[]
        for i in range (self.fila):
            fila=[]
            for j in range (self.columna):
                fila.append("_")
            self.tablero.append(fila)    
    #recorrer la columna para saber la posición de una ficha, si la columna esta ocupada se devuelve un -1 si la fila esta ocupada también.
    def comprobarColumna(self, columna):
        for i in range(self.fila-1,-1,-1):
            if self.tablero[i][columna] != "_":
                continue
            else: 
                return i
        return -1 
    def colocarFicha(self, columna, equipoActual):
        fila = self.comprobarColumna(columna)
        if fila == -1:
            return False
        else: 
            ficha = Ficha (fila, columna, equipoActual)
            self.tablero[fila][columna]= ficha
            return True   
    def imprimirTablero(self):
        for i in range(len(self.tablero)):
           # print(self.tablero[i])
            for j in range(len(self.tablero[i])):
                print(self.tablero[i][j], end=" ")
            print()
    def verificarGanador(self):       
        vectores=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1]]
        contador=0
        for i in range(len(self.tablero)):
            if self.tablero[0][i] != "_":
                pos=[]
                pos[0]=self.tablero[0]
                pos[1]=self.tablero[i]
                pos+=vectores
                if pos==self.tablero[0][i]:
                    contador+=1
                    if contador==4:
                        print("Hay cuatro en raya")
        
tablero = Tablero ("O","X")
tablero.colocarFicha(4,"O")
tablero.colocarFicha(4,"X")
tablero.colocarFicha(4,"O")
tablero.colocarFicha(4,"X")
tablero.colocarFicha(5,"X")
tablero.colocarFicha(5,"X")
tablero.colocarFicha(5,"X")
tablero.colocarFicha(5,"X")
tablero.colocarFicha(1,"X")

tablero.imprimirTablero()