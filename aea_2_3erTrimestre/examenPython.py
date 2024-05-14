from functools import reduce

'''
Desarrollo de Clases en Python

La clase Producto en Python está diseñada para representar productos en una máquina expendedora.
Cuenta con tres atributos principales: nombre, que es un string para el nombre del producto; 
precio, que es un float que indica el precio del producto; y cantidad, que es un integer que representa 
la cantidad disponible del producto. Los métodos de esta clase incluyen el constructor para inicializar un producto,
modificar la función que devuelve una cadena que representa la información del producto (se pueden añadir todas las funciones que se deseen). 
Se considerará que dos Productos son iguales si su nombre es igual, indistintamente de si está escrito en mayúsculas como si está en minúsculas

Por otro lado, la clase MaquinaExpendedora maneja el conjunto de productos disponibles para la venta. 
Esta clase tiene un solo atributo: inventario de productos. Esta clase Incluye varios métodos: un constructor para inicializar
la máquina sin productos, una función para añadir un producto al inventario en una cantidad concreta, 
una función para reducir en 1 un producto en concreto y una función que imprime la lista de productos 
disponibles con su información detallada, por último, una función que permite a los usuarios comprar un 
producto realizando las comprobaciones necesarias y lógicas de una máquina de estas características.

En el main se deben hacer todas las comprobaciones necesarias, para probar todas las funciones realizadas.


Cada clase tiene que estar en un fichero diferente, así como el main.py


'''









lista_de_personas = [
    {'nombre': 'Ana', 'edad': 28, 'hobbies': ['leer']},
    {'nombre': 'Carlos', 'edad': 34, 'hobbies': ['pintar', 'escalar']},
    {'nombre': 'Diana', 'edad': 21, 'hobbies': ['nadar', 'correr', 'cocinar']},
    {'nombre': 'Elena', 'edad': 26, 'hobbies': ['viajar']},
    {'nombre': 'Fernando', 'edad': 31, 'hobbies': ['videojuegos', 'dibujo', 'guitarra', 'canto']},
    {'nombre': 'Gloria', 'edad': 23, 'hobbies': ['yoga', 'meditación']},
    {'nombre': 'Héctor', 'edad': 29, 'hobbies': ['fotografía']},
    {'nombre': 'Irene', 'edad': 35, 'hobbies': ['ciclismo', 'lectura', 'escribir']},
    {'nombre': 'Jorge', 'edad': 30, 'hobbies': ['teatro', 'cine', 'baile', 'escultura']},
    {'nombre': 'Laura', 'edad': 24, 'hobbies': ['ajedrez']}
]

'''
Los siguientes ejercicios solo se pueden realizar con map, filter y reduce. Se puede usar otras funciones pero no ningún tipo de bucle

- Dame la persona de más edad
- Dame la persona con mayor número de hobbies
- De cada una de las personas dame el hobbie con nombre más largo
- Dame todos los nombres las personas y sus edades con la siguiente estructura:
    - nombre1 , edad1 <-> nombre2 , edad2 <-> nombre3 , edad3 <-> ...
'''
#hacemos un map para que nos devuelva una lista con el nombre y edad de las personas
plusEdad=list(map(lambda x: (x['edad'],x['nombre']), lista_de_personas))
#aplicamos un reduce para sacar a la persona de mayor edad
masEdad=reduce(max,plusEdad)
print("la persona con mas edad es: ",masEdad)
#hacemos un filtrado que tiene en cuenta el numero total de hobbies de cada persona y si este es mayor de 3 saca a los que mas hobbies tienen :)
masHobbies=list(filter(lambda x: len(x['hobbies'])>3, lista_de_personas))
print("La persona/s con mas habbies es/son: ",masHobbies)
#mostramos los datos en vez de str en tuplas usando map y metemos de forma original el simbolo :)
estructura=list(map(lambda x: (x['nombre'],x['edad'],"<->"), lista_de_personas))
print("<->",estructura,"<->")


