import random as rd

"""
Ejercicio 1:
Crear una lista vacía y agregar elementos.
Escribe un programa que cree una lista vacía llamada "mi_lista" y agregue los números del 1 al 5 a esta lista.
"""
print("<----------------------Ejercicio 1------------------------>")

mi_lista = []

mi_lista = [1,2,3,4,5]

print(mi_lista)
    


"""
Ejercicio 2:
Acceder a elementos de una lista.
Escribe un programa que defina una lista llamada "colores" que contenga los nombres de varios colores y muestre el primer y el último elemento de la lista.
"""
print("<----------------------Ejercicio 2------------------------>")

colores=["azul","rojo","verde","amarillo"]

print(colores[0])

print(colores[len(colores)-1])  

"""
Ejercicio 3:
Modificar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y cambie el tercer elemento de la lista por el número 10.
"""
print("<----------------------Ejercicio 3------------------------>")

listaNum=[1,2,3,4,5]
listaNum[2]=10
print(listaNum)

"""
Ejercicio 4:
Eliminar elementos de una lista.
Escribe un programa que tenga una lista de nombres de frutas y elimine el segundo elemento de la lista.
"""
print("<----------------------Ejercicio 4------------------------>")

listaborrar= ["naranja","pera","manzana","fresa","platano"]
listaborrar.pop(1)
print(listaborrar)

"""
Ejercicio 5:
Contar elementos de una lista.
Escribe un programa que cuente cuántas veces aparece la palabra "perro" en una lista dada.
"""
print("<----------------------Ejercicio 5------------------------>")

listaPerrro= ["perro","perro","perro","perro","perro"]

print(listaPerrro.count("perro"))   

"""
Ejercicio 6:
Crear una lista a partir de elementos ingresados por el usuario.
Escribe un programa que solicite al usuario ingresar 5 nombres y cree una lista con estos nombres.
"""
print("<----------------------Ejercicio 6------------------------>")

def listaNombre():
    tu_lista = []
    for i in range(1,6):
        numero = input("Dame un número")
        tu_lista.append(numero)
    print(tu_lista)

"""
Ejercicio 7:
Concatenar dos listas.
Escribe un programa que tenga dos listas de números y las concatene para formar una sola lista.
"""
print("<----------------------Ejercicio 7------------------------>")

listaNumero1 = [1,2,3,4,5]
listaNumero2 = [6,7,8,9,10]

print(listaNumero1+listaNumero2)    

"""
Ejercicio 8:
Ordenar una lista alfabéticamente.
Escribe un programa que tenga una lista de nombres de países y los ordene alfabéticamente.
"""
print("<----------------------Ejercicio 8------------------------>")

listaPaises=["Colombia","Brasil","Perú","Argentina","Uruguay","Venezuela"]

listaPaises.sort()  

print(listaPaises)  


"""
Ejercicio 9:
Reemplazar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y reemplace los elementos del segundo al cuarto por el número 0.
"""
print("<----------------------Ejercicio 9------------------------>")

listaReemplazo= [1,2,3,4,5] 

for indice in range(2,len(listaReemplazo)):
    listaReemplazo[indice]=0

print(listaReemplazo)   


"""
Ejercicio 10:
Buscar un elemento en una lista.
Escribe un programa que tenga una lista de números y verifique si el número 5 está presente en la lista.
"""
print("<----------------------Ejercicio 10------------------------>")

listabucsar= [3,6,9,8,5]

for indice in range(0,len(listabucsar)):
    if listabucsar[indice]==5:
        print("El número 5 está presente en la lista")
    else:  
        print("El número 5 no está presente en la lista")

"""
Ejercicio 11:
Calcular la longitud de una lista.
Escribe un programa que tenga una lista de colores y calcule cuántos elementos tiene la lista.
"""
print("<----------------------Ejercicio 11------------------------>")

listaColores=["azul","rojo","verde","amarillo"] 

print(len(listaColores))    


"""
Ejercicio 12:
Crear una lista de números pares.
Escribe un programa que cree una lista de los primeros 5 números pares a partir de un rango.
Agrega esos números pares a una lista
"""
print("<----------------------Ejercicio 12------------------------>")

pares=[]
for i in range (2,12,2):
    if i%2==0:
         pares.append(i)
print(list(pares))        
        
        
"""
Ejercicio 13:
Sumar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y sume todos sus elementos.
"""
print("<----------------------Ejercicio 13------------------------>")


listaSumar= [1,2,3,4,5,6,7,8,9,10]

print(sum(listaSumar))


"""
Ejercicio 14:
Contar elementos mayores que un número dado.
Escribe un programa que tenga una lista de números y cuente cuántos elementos son mayores que 5.
"""
print("<----------------------Ejercicio 14------------------------>")


listaMayores= [1,2,3,4,5,6,7,8,9,10]
contador=0
for indice in range(0,len(listaMayores)):
    if listaMayores[indice]>5:
        contador+=1
print("La cantidad de elementos mayores que 5 son: ",contador)
        

"""
Ejercicio 15:
Eliminar duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine los duplicados de la lista.
"""
listaDuplicada=[1,1,1,1,2,2,2,2,5,5,6,3,6,6,9,8,7,77,9]
print(set(listaDuplicada))

"""
Ejercicio 16:
Multiplicar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y multiplique todos sus elementos entre sí.
"""
print("<----------------------Ejercicio 16------------------------>")


resultado=1
listaMultiplos= [1,2,3,4,5,6,7,8,9]
for indice in range(0,len(listaMultiplos)):
    resultado*=listaMultiplos[indice]
print(resultado)

"""
Ejercicio 17:
Comprobar si una lista está vacía.
Escribe un programa que determine si una lista dada está vacía o no.
"""
print("<----------------------Ejercicio 17------------------------>")


listaVacia=[]

if len(listaVacia)==0:
        print("La lista está vacía")
else:
        print("La lista no está vacía")

"""
Ejercicio 18:
Calcular el promedio de una lista de números.
Escribe un programa que tenga una lista de números y calcule el promedio de esos números.
"""

print("<----------------------Ejercicio 18------------------------>")

listaProm=[1,2,3,4,5,6,7,8,9]
print(sum(listaProm)/len(listaProm))



"""
Ejercicio 19:
Calcular la suma de los elementos pares de una lista.
Escribe un programa que tenga una lista de números y calcule la suma de todos los elementos pares en la lista.
"""
print("<----------------------Ejercicio 19------------------------>")

sumapares=[1,2,3,4,5,6,7,8,9]
resultado=0
for indice in range(0,len(sumapares)):
    if sumapares[indice]%2==0:
        resultado+=sumapares[indice]
print(resultado)

"""
Ejercicio 20:
Reemplazar todos los elementos de una lista con un valor dado.
Escribe un programa que tenga una lista de números y reemplace todos sus elementos por un valor dado.
"""
print("<----------------------Ejercicio 20------------------------>")

valor=7
for i in range (len(sumapares)):
    sumapares[i]=valor

print(sumapares)
    

"""
Ejercicio 21:
Invertir una lista.
Escribe un programa que tenga una lista de números y la invierta, es decir, que el primer elemento se convierta en el último y viceversa.
"""

print("<----------------------Ejercicio 21------------------------>")

listainversa=[7,6,5,4,3,2,1]
listainversa.reverse()
print(listainversa)



"""
Ejercicio 22:
Dividir una lista en partes iguales.
Escribe un programa que tenga una lista de números y la divida en partes iguales de longitud especificada por el usuario.
"""

print("<----------------------Ejercicio 22------------------------>")

dividirlista=[1,2,3,4,5,6,7,8,9,1]
longitud=int(input("Ingrese la longitud de la lista: "))

for i in range(0,len(dividirlista),longitud):
    print(dividirlista[i:i+longitud])
    
   

"""
Ejercicio 23:
Ordenar una lista en orden descendente.
Escribe un programa que tenga una lista de números y la ordene en orden descendente.
"""
print("<----------------------Ejercicio 23------------------------>")

listainversa=[3,2,5,6,9,8,7]
listainversa.sort()
listainversa.reverse()
print(listainversa)

"""
Ejercicio 24:
Unir dos listas en una sola.
Escribe un programa que tenga dos listas de números y las una en una sola lista.
"""
print("<----------------------Ejercicio 24------------------------>")

lista1=[1,2,3]
lista2=[4,5,6]
lista1.extend(lista2)
print(lista1)

"""
Ejercicio 25:
Eliminar todos los elementos duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine todos los duplicados, dejando solo una ocurrencia de cada elemento.
"""
print("<----------------------Ejercicio 25------------------------>")

#usar set


'''
Ejercicio 26:
Ordenar una lista de cadenas alfabéticamente sin distinción entre mayúsculas y minúsculas:

Escribe un programa que solicite al usuario ingresar una lista de palabras 
y luego ordene la lista alfabéticamente sin distinguir entre mayúsculas y minúsculas.
Además, el programa debe eliminar cualquier palabra duplicada antes de realizar la ordenación.
'''

print("<----------------------Ejercicio 26------------------------>")

listalfabetica=["Colombia","Brasil","Perú","Argentina","Uruguay","Venezuela"]
listarenorden=[]

for i in listalfabetica:
  listarenorden.append(i.lower())
listarenorden.sort()
print(listarenorden)


'''
Ejercicio 27
Escribe un programa que genere dos listas de números aleatorios entre 1 y 20 
y luego calcule e imprima la intersección de estas dos listas,
es decir, los números que aparecen en ambas listas.
Asegúrate de que no haya duplicados en las listas generadas.
'''
print("<----------------------Ejercicio 27------------------------>")

v1 = []
v2 = []
for i in range(6):
    num1= rd.randint(1,20)
    num2 = rd.randint(1,20)
    if num1 not in v1:
        v1.append(num1)
    if num2 not in v2:
        v2.append(num2)
print(v1," y ",v2)
otro = []
for i in range(len(v1)):
    if v1[i] in v2:
        otro.append(v1[i])
print(otro)





'''
Ejercicio 28
Eliminar elementos repetidos de una lista manteniendo el orden original:

Escribe un programa que reciba una lista de números y elimine los elementos 
repetidos de la lista manteniendo el orden original.
'''
print("<----------------------Ejercicio 28------------------------>")

print("Usa set")



'''
Ejercicio 29
Calcular la media de una lista de números:
Escribe un programa que calcule la media de una lista de números ingresada por el usuario.
'''
print("<----------------------Ejercicio 29------------------------>")

print("Usa sum y divide por len")



'''
Ejercicio 30
Encontrar el elemento más grande y el más pequeño en una lista:
Escribe un programa que encuentre el elemento más grande y el más pequeño en una lista de números.
'''
print("<----------------------Ejercicio 29------------------------>")

trova=[7,8,9,5,4,3,4,56,2]
print(max(trova))

print(min(trova))