
    
'''
Ejercicio 1
Crea un programa que procese una lista de tuplas, donde cada tupla representa una venta y contiene el nombre del producto,
la cantidad vendida y el precio unitario (ejemplo: [("manzana", 30, 0.50), ("banana", 20, 0.75)])
Filtra aquellos datos que tengan pocas unidades(menos de 10).
Quiero saber el total de ingresos de las ventas de estos productos
'''
'''
Ejercicio 2
Dado un diccionario que contiene el nombre del estudiante y su lista de calificaciones 
(por ejemplo, {"Ana": [4.5, 7.0, 8.0], "Juan": [5.0, 7.5, 6.0]}). Se requiere calcular el promedio de calificaciones de cada estudiante
seleccionando solo aquellos estudiantes con un promedio superior a 6.0.
Además, se quiere determinar el número total de estudiantes que superan este promedio.
'''
from functools import reduce

estudiantes={"Ana": [4.5, 7.0, 8.0], "Juan": [5.0, 0.0, 6.0]}
promedio=list(map(lambda x: (x[0]+x[1]+x[2])/3, estudiantes.values()))
print(promedio)
filtrado=list(filter(lambda c: c>6, promedio))
print(filtrado)

'''
Ejercicio 3
Considera que tienes una lista de diccionarios, cada uno representando a una persona con claves 
como nombre, edad y ciudad. Se quiere poder filtrar las personas para seleccionar solo las personas que pertenecen a una ciudad específica.
Los datos devueltos tienen que ser la edad promedio de las personas de la ciudad seleccionada.
'''


'''
Ejercicio 4
Crea un programa que analice una lista de comentarios de usuarios en una red social. 
Cada comentario es un texto que puede contener emociones positivas o negativas. 
El programa debe filtrar los comentarios que contengan al menos una palabra clave negativa, 
analizar el sentimiento general de los comentarios filtrados y calcular el porcentaje de comentarios
negativos respecto al total de comentarios analizados.
Crea una lista de palabras con comentarios positivos y comentarios negativos que te ayuden en el filtrado
'''
comentarios = [
    "Me encanta el nuevo diseño de la plataforma!",
    "Es terrible cómo se manejan los bugs aquí.",
    "¡Excelente trabajo con las actualizaciones!",
    "Odio la lentitud del sistema ahora.",
    "No estoy contento con el servicio de atención al cliente.",
    "¡Bravo por los esfuerzos!",
    "¡El peor cambio que han hecho hasta ahora!"
]
negatifs=["terrible", "Odio", "No", "peor"]
def compararComentarios(x):              
        for i in range (len(comentarios)):
                listaPalabras=x.split()
                for f in range (len(listaPalabras)):
                        if listaPalabras[f] in negatifs:
                                return True
                else:
                        return False
def porcentajenegatif ():
       print((len(filtrado1)/len(comentarios))*100) 
                                
                        
filtrado1=list(filter(compararComentarios, comentarios))       
print(filtrado1) 
porcentajenegatif()        

'''
Ejercicio 5
Desarrolla un programa que maneje una lista de reservas de un hotel. 
Cada reserva está representada por un diccionario que incluye información como el nombre del cliente, número de noches reservadas y tipo de habitación.
El objetivo es identificar aquellas reservas que exceden una estancia de 5 noches, procesar la información para calcular el total 
de noches reservadas por esos clientes y determinar el tipo de habitación más demandado entre esas reservas largas.
'''