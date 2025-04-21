from visitante import Visitante
'''
El museo Eldavots tiene una exposición de distintos cuadros. El museo tiene un aforo máximo de 7 personas.
desde este museo se quiere llevar un registro de los cuadros expuestos donde se pueda ver el año de la obra,
el genero y el autor. Asimismo queremos registrar los datos de los visitantes entre los que deben estar el genero,
nombre y edad. Se quiere revisar cuantas mujeres mayores de 25 asisten
al museo y cuanto se recauda por parte del publico varón.
La entrada vale 35 euros.
'''
class Museo:
#CONSTRUCTOR DEL MUSEO
    def __init__(self, nombre):
        self.nombre=nombre
        self.listaCuadros=[]
        self.listaVisitantes=[]
        self.aforo=7
#FUNCION QUE PERMITE AÑADIR CUADROS AL MUSEO        
    def agregarCuadro(self, Cuadro):
        if Cuadro in self.listaCuadros:
            print("El cuadro ya ta expuesto!")
        else:
            self.listaCuadros.append(Cuadro)
            print("El cuadro fue agregado con autentico exito")
    def cuadrosExpuestos(self):
        print(self.listaCuadros)
    def mostrarCuadros (self):
        for cuadro in self.listaCuadros:
            print("Cuadro: ", cuadro.obra )
#FUNCION QUE PERMITE AÑADIR VISITANTES AL MUSEO ADEMÁS DE DELIMITAR EL AFORO AVISANDO Y ELIMINANDO AL ULTIMO VISITANTE QUE NO ENTRABA           
    def agregarVisitantes(self, Visitante):
        if Visitante in self.listaVisitantes:
            print("El visitante ya ta en el museots!")
        else:
            self.listaVisitantes.append(Visitante)
            print("Se agregó al vistante mijo!")
            
        if len(self.listaVisitantes)>self.aforo:
            self.listaVisitantes.remove(Visitante)
            print("El aforo ya está completo!")
    def mostrarListaVistante(self):
        for visitante in self.listaVisitantes:
            print("Nombre: ", visitante.name)        
    def mujeres(self):
        filtro1=list(filter(lambda x: x.gender=="Mujer", self.listaVisitantes))
        filtro2=list(filter(lambda x: x.edad>25, filtro1))
        print("Han vistado el museo: ",len(filtro2)," mujeres mayores de 25")
    def recaudacion(self):
        filtro3=list(filter(lambda x: x.gender=="Varon", self.listaVisitantes))
        print("Se recaudan ",len(filtro3)*35," euros de las entradas de los varones")