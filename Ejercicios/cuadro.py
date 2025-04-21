'''
El museo Eldavots tiene una exposición de distintos cuadros. El museo tiene un aforo máximo de 7 personas.
desde este museo se quiere llevar un registro de los cuadros expuestos donde se pueda ver el año de la obra,
el genero y el autor. Asimismo queremos registrar los datos de los visitantes entre los que deben estar el genero,
nombre y edad. Se quiere revisar cuantas mujeres mayores de 25 asisten
al museo y cuanto se recauda por parte del publico varón.
La entrada vale 35 euros.
'''
class Cuadro:
    
    def __init__(self, obra, anio, genero, autor):
        self.obra=obra
        self.anio=anio
        self.genero=genero
        self.autor=autor