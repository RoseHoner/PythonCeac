




#Declaración de numeros enteros
numero1=10
numero2=50
 
#Declaración de variables que almacenan el resultado de las operaciones aritmeticas realizadas con los dos numeros enteros
suma= numero1+numero2
resta= numero1-numero2
multiplicación= numero1*numero2
divición= numero1/numero2
 
#Se imprime por pantalla los resultados  
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
print(" La suma de los números es igual a:", str(suma))
print(" La resta de los números es igual a:", str(resta))
print(" La multiplicación de los números es igual a:", str(multiplicación))
print(" La división de los números es igual a:", str(divición),end="")
print(" En decimal")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
 
#<--------------------------------------------------------------------------->
#Como se potencia un numero
if(numero1<numero2):
    potencia=numero2**numero1
    print("El numero", str(numero2),"potenciado por", str(numero1),"es igual a:",str(potencia))
   
#Como se puede multiplicar un texto    
texto="Hola Mundo"
mult=3
texto*=mult
print(texto)
#<--------------------------------------------------------------------------->  
'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|     Tipos de Datos:
|         -Boolenaos
|         -Entero
|         -Decimales
|         -Listas
|         -Tuplas (Es lo mismo que un Array, solo que una ve que se le ha asignado un valor, no se puede modificar)
|         -Conjuntos o Set (Son como Arrays que solo funcionan con datos diferentes)
|         - Textos
|         -Diccionarios
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        
'''
 
'''
     Declaración de variables -->
'''
 
numeroEntero=5
numeroDecimal=5.3
texto= "Esto es un texto"
booleano=True
 
'''
     Imprimir por pantalla -->
'''
 
print("El número entero es: "+ str(numeroEntero)) #En vez de suma se puede poner una coma, la cual, dara un espacio antes de que se imprima el otro número
print(texto)
print(str(booleano))
 
'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|     OPERADORES ARITMETICOS
|         - (+)Suma
|         - (-)Resta
|         - (*)Multiplicación
|         - (/)Divición
|         - (%)Resto
|         - (**)Potencia
|         - (//)División exacta
|        
|     OPERADORES RELACIONALES
|         - (>) Mayor que
|         - (<) Menor que
|         - (>=) Mayor o igual que
|         - (<=) Menor o igual que
|         - (==) Igual que
|         - (!=) Distinto que
|        
|     OPERADORES DE ASIGNACIÓN
|         - (=) Asignar un valor
|         - (+=) Asignación de suma a variable
|         - (-=) Asignación de resta a variable
|         ..
|        
|     OPERADORES LÓGICOS
|         - (and) Y lógico --> Tiene prioridad despues de el not
|         - (or) O lógico  --> Tiene prioridad despues de el and
|         - (not) No lógico --> Tiene prioridad        
|        
|     OPERADORES DE PERTENENCIA
|         - (in) Para saber si un valor está dentro de otro
|         - (not in) Para saber si un valor no está dentro de otro
|        
|     OPERADOR DE INDENTIDAD
|         - (is) Para comprobar si un objeto es igual a otro
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        
'''

var1="5"
print(int(var1)+1)
stringvar="hola que tal hola que pasa que tal"
print(len(stringvar))

'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|
|    Para calcular el abosluto de un numero se usa el abs y para redondear utilizamos el round
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
'''

varabs=-5
print(abs(varabs))
varound=3.3
print(round(varound))

'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|
|   Con la funcion eval podemos resolver una operacion de un string
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
'''
n=2
print(eval("3+9/6*n"))

'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|
|    Con la funcion type podemos saber el tipo de dato
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
'''

print(type(5))
print(type("true"))
print(type(6.7))
print(type(False))


'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|
|    En Python los rangos son un tipo de dato muy utilizado se escribe range y hay tres formas de escribir un rango
|   1: pos inicial 0 hasta la seleccionada-1. 2: pos inicial y final-1. 3: pos inicial, final-1 y los pasos.
|   para visualizar los datos tenemos que convertirlo a una lista.
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
'''

print(range(10))
print(range(5,10))
print(range(5,10,2))

print(list(range(10)))
print(list(range(5,10)))
print(list(range(5,10,2)))

'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|           IF Y FOR
|    No son necesarios ni los parentesis ni las llaves
|   Para el for necesitamos el rango y concretar el indice
|   
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
'''

if 5<6:
    print("es menor")
elif 5<4:
    print("5<4")    
else:
    print("no es menor")    
 
var="hola buenos dias"   
for indice in range (1,len(var),2):
    print(var[indice])

for letra in var: 
    print(letra)      
    
    
'''
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|           
|    
|   
|   
|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
'''

var = input("Dame un número")
print("El numero es:",var)
