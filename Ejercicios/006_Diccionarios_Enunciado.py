"""
Ejercicio 1: Crear un diccionario que almacene los nombres de estudiantes 
y sus notas finales. 
Luego, agregar funcionalidad para cambiar la nota de un estudiante y 
mostrar la nota modificada.
"""
notasestudiantes = { "Davo": 9, "Luis": 10, "Andrea": 10, "Deyby": 6}

def cambiarNota(alumnos, nombre, nota):
    if nombre in alumnos:
        alumnos[nombre]=nota
    else:
        print("No ta")    
def mostrarNota(alumnos, nombre):
    print(alumnos[nombre])

cambiarNota(notasestudiantes, "Deyby", 5)
mostrarNota(notasestudiantes, "Deyby")
"""
Ejercicio 2: Dado un diccionario con nombres de empleados y su salario,
calcular el salario medio, el salario más alto y el más bajo.
"""
from functools import reduce

empelados={"Andrea": 1000, "Luis": 1200, "Davo": 500, "Jans": 1800}
salarioMedio= reduce(lambda x,y : x+y, empelados.values())
print(salarioMedio/len(empelados))

"""
Ejercicio 3: Crear un programa que cuente la frecuencia de las
palabras de una frase dada por el usuario y almacene los resultados
en un diccionario.
"""


"""
Ejercicio 4: Dado un diccionario que almacena las preferencias
de color de los usuarios, actualizar el diccionario agregando un 
conjunto de usuarios que prefieren el mismo color.
"""

"""
Ejercicio 5: Crear un programa que utilice un diccionario para 
mapear nombres de productos y sus precios. Luego, convertir este 
diccionario en una lista de tuplas, donde cada tupla contenga el 
nombre del producto y su precio.
"""

"""
Ejercicio 6: Crear un diccionario que almacene como clave el
nombre de un país y como valor un set de ciudades de ese país.
Añadir después una nueva ciudad a uno de los países y mostrar 
el diccionario actualizado.
"""

"""
Ejercicio 7: Dado un diccionario de productos y precios,
escribir un programa que convierta los precios a otra moneda
(por ejemplo, de euros a dólares) utilizando un tipo de cambio 
fijo, y guarde los resultados en un nuevo diccionario.
"""

"""
Ejercicio 8: Implementar un sistema de votación donde 
se almacenen los votos de diferentes candidatos en un 
diccionario. Luego, contar el total de votos y determinar el ganador.
"""

"""
Ejercicio 9: Crear un diccionario que almacene números de teléfono
(como valores) asociados a nombres de personas (como claves).
Implementar una función que, dado el diccionario y un nombre,
devuelva el número de teléfono asociado o un mensaje indicando que no se encontró.
"""

"""
Ejercicio 10: Utilizar un diccionario para almacenar 
una lista de tuplas que representen artículos y sus cantidades 
en un inventario. Después, escribir una función que actualice 
la cantidad de un artículo específico.
"""

"""
Ejercicio 11: Dado un diccionario que mapea los nombres de 
varios productos a sus precios por unidad, escribir un programa 
que invierta este diccionario, mapeando los precios a una 
lista de productos con ese precio.
"""

"""
Ejercicio 12: Crear un diccionario que almacene el nombre 
de estudiantes y una lista de sus calificaciones. 
Escribir un programa que calcule la media de calificaciones 
de cada estudiante y almacene el resultado en un nuevo diccionario.
"""

"""
Ejercicio 13: Implementar un programa que almacene en un 
diccionario los votos de tres colores diferentes 
(por ejemplo, "rojo", "azul", "verde") dados por usuarios. 
El programa debe incrementar el conteo de votos cada vez que 
un color es votado y finalmente mostrar los resultados.
"""

"""
Ejercicio 14: Dado un diccionario con nombres de personas como
claves y su año de nacimiento como valores, escribir un programa 
que calcule las edades de las personas y almacene los resultados 
en otro diccionario.
"""

"""
Ejercicio 15: Crear un programa que almacene las asignaturas de 
un curso (por ejemplo, matemáticas, física, química) y los estudiantes 
inscritos en ellas. Luego, permitir al usuario introducir el nombre 
de una asignatura y mostrar todos los estudiantes inscritos en ella.
"""

"""
Ejercicio 16: Desarrollar un programa que modele un sistema de reservas
para un hotel. El sistema debe permitir agregar y eliminar reservas. 
Cada reserva debe contener el nombre del huésped, la fecha de check-in y
check-out, y el número de habitación. Utilizar un diccionario donde 
cada clave sea el número de habitación y el valor sea otro diccionario
con los detalles de la reserva.
"""

"""
Ejercicio 17: Implementar un sistema de votación por categorías, 
donde cada votante puede votar por un candidato en múltiples categorías
(por ejemplo, Mejor Director, Mejor Película). Almacenar los votos en 
un diccionario compuesto, donde las claves sean las categorías y los 
valores sean diccionarios de candidatos y la cantidad de votos recibidos.
El programa debe permitir añadir votos y determinar los ganadores por categoría.
"""

"""
Ejercicio 18: Crear un programa para gestionar el inventario de una tienda. 
El inventario debe almacenar productos y sus cantidades. Implementar funciones 
para añadir productos, actualizar cantidades y mostrar el inventario actual. 
Además, implementar una búsqueda de productos por nombre.
"""

"""
Ejercicio 19: Desarrollar un programa que simule un sistema de 
recomendación de películas. Usar un diccionario para almacenar 
géneros de películas como claves y listas de películas como valores.
Implementar una función que, dado un género, muestre las películas 
disponibles en ese género.
"""
