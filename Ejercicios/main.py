from museoEldavots import Museo
from cuadro import Cuadro
from visitante import Visitante

'''
El museo Eldavots tiene una exposición de distintos cuadros. El museo tiene un aforo máximo de 7 personas.
desde este museo se quiere llevar un registro de los cuadros expuestos donde se pueda ver el año de la obra,
el genero y el autor. Asimismo queremos registrar los datos de los visitantes entre los que deben estar el genero,
nombre y edad. Se quiere revisar cuantas mujeres mayores de 25 asisten
al museo y cuanto se recauda por parte del publico varón.
La entrada vale 35 euros.
'''

elDavots=Museo("elDavots")

c1=Cuadro("La tota lisa", 2024, "Barroco", "Kerry Konabo")
c2=Cuadro("Le grito", 2021, "Abstracto", "Kerry Konabo")
c3=Cuadro("Retrato de Napollon", 2022, "Realismo", "Kerry Konabo")
c4=Cuadro("Crisis progenitalia", 2023, "Cubismo", "Kerry Konabo")

v1=Visitante("Mujer", "Lucia", 27)
v2=Visitante("Varon", "Ambrosio", 33)
v3=Visitante("Varon", "Rigiigobegto", 21)
v4=Visitante("Mujer", "Afrastasia", 31)
v5=Visitante("Mujer", "Segismunda", 17)
v6=Visitante("Mujer", "Dubydubá", 26)
v7=Visitante("Varon", "LuigiMaricoDaSilva", 21)
v8=Visitante("Varon", "Leopel Daños", 67)

elDavots.agregarCuadro(c1)
elDavots.agregarCuadro(c2)
elDavots.agregarCuadro(c3)
elDavots.agregarCuadro(c4)
elDavots.agregarVisitantes(v1)
elDavots.agregarVisitantes(v2)
elDavots.agregarVisitantes(v3)
elDavots.agregarVisitantes(v4)
elDavots.agregarVisitantes(v5)
elDavots.agregarVisitantes(v6)
elDavots.agregarVisitantes(v7)
elDavots.agregarVisitantes(v8)
elDavots.mostrarCuadros()
elDavots.mostrarListaVistante()
elDavots.mujeres()
elDavots.recaudacion()
