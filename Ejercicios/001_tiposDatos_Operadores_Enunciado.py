import random

"""
Ejercicio 1:
Crear un programa que calcule el área de un triángulo rectángulo dado su base y altura.
Utiliza variables para almacenar la base, la altura y el resultado del cálculo del área.
"""

base = 4
altura = 8
area = (base*altura)/2
print("El area del triangulo es:", area)


"""
Ejercicio 2:
Escribir un programa que convierta grados Celsius a grados Fahrenheit.
Utiliza una variable para almacenar los grados Celsius, realiza el cálculo y muestra el resultado.
"""
gradosC = 22
gradosF = (gradosC * 9/5)+32
print("Los grados farenheit son: ",gradosF)


"""
Ejercicio 3:
Crear un programa que calcule el perímetro y el área de un círculo dado su radio.
Utiliza una variable para almacenar el radio, realiza los cálculos y muestra los resultados.
"""

radio = 13
perimetro = 2*(3.14)*radio
area = 3.14*radio**2
print("El perimetro dado el radio es de: ", perimetro, "y el area es de: ", area)

"""
Ejercicio 4:
Escribir un programa que determine si un número dado es par o impar.
Utiliza una variable para almacenar el número, aplica el operador de módulo y muestra el resultado.
"""

var = int(input("Cuantas caras tiene el dado?"))
if var%2==0:
    print("el dado es par")
else:
    print("el dado es impar")    



"""
Ejercicio 5:
Crear un programa que calcule la hipotenusa de un triángulo rectángulo dado sus catetos.
Utiliza dos variables para almacenar los catetos, aplica el teorema de Pitágoras y muestra el resultado.
"""

cat1 = 7
cat2 = 9
hipotenusa = (cat1**2+cat2**2)**(1/2)

print("la hipotenusa es: ", round(hipotenusa))

"""
Ejercicio 6:
Crear un programa que calcule el área y el perímetro de un rectángulo dados su base y su altura.
Utiliza variables para almacenar la base, la altura y realiza los cálculos correspondientes.
"""

recB = 4
recA = 6

areaR = (recB*recA)/2
print("El area es: ", areaR)


"""
Ejercicio 7:
Escribir un programa que determine si un año es bisiesto o no.
Utiliza una variable para almacenar el año, aplica las reglas para determinar si es bisiesto y muestra el resultado.
"""

anno = 366
if anno>365:
    print("el año es bisiesto")


"""
Ejercicio 8:
Crear un programa que convierta una cantidad de dólares a euros.
Utiliza una variable para almacenar la cantidad de dólares, realiza la conversión y muestra el resultado.
"""
euros=30
dollar=0.92
print("tus",euros,"euros son: ",euros*dollar," dolares")


"""
Ejercicio 9:
Escribir un programa que determine si un número dado es positivo, negativo o cero.
Utiliza una variable para almacenar el número, aplica condiciones y muestra el resultado.
"""

num1 = -3
if num1 > 0:
    print("El numero es positivo")
if num1 < 0:
    print("el numero es negativo")
if num1 == 0:
    print("El numero es 0")        


"""
Ejercicio 10:
Crear un programa que calcule el promedio de tres números dados.
Utiliza tres variables para almacenar los números, realiza el cálculo y muestra el resultado.
"""

num2=713
num3=317
num4=137
promedio = (num2+num3+num4)/3
print("El promedio es: ",promedio)

"""
Ejercicio 11:
Crear un programa que determine si un número dado es primo o no.
Utiliza una variable para almacenar el número, aplica las reglas para determinar si es primo y muestra el resultado.
"""

numero = 6
esPrimo = True
for i in range(2,numero):
    if(numero%i)==0:
       esPrimo=False
if esPrimo==False:
    print("El número",numero,"No es primo")       
else:
    print("El numero",numero,"Es primo")     

"""
Ejercicio 12:
Escribir un programa que determine si un número dado es múltiplo de otro.
Utiliza dos variables para almacenar los números, aplica el operador de módulo y muestra el resultado.
"""

num5=20
num6=13
if num5%num6==0:
    print("El numero",num5," si es multiplo de ",num6)
else:
    print("El numero",num5," no es multiplo de ",num6)
   


"""
Ejercicio 13:
Crear un programa que calcule el factorial de un número dado.
Utiliza una variable para almacenar el número, realiza el cálculo del factorial y muestra el resultado.
"""

factorial = 7
resFact = factorial
for i in range(1,factorial):
    resFact *= i
print("El resultado factorial de",factorial,"es: ",resFact)

"""
Ejercicio 14:
Escribir un programa que determine si una cadena de texto es palíndromo o no.
Utiliza una variable para almacenar la cadena, aplica condiciones y muestra el resultado.
"""
texto1 = "rojo"

for i in range(len(texto1)):
    if texto1[i]==texto1[len(texto1)-i-1]:
         print("la cadena",texto1,"es palíndroma")
    else:
        print("la cadena",texto1,"no es palíndroma")


"""
Ejercicio 15:
Crear un programa que cuente la cantidad de vocales en una cadena de texto dada.
Utiliza una variable para almacenar la cadena, itera sobre cada carácter y cuenta las vocales, luego muestra el resultado.
"""
frase1="esta vida es como una caja de bombones"
contador=0
for i in frase1:
    if i == "a":
        contador+=1
    if i == "e":
        contador+=1
    if i == "i":
        contador+=1
    if i == "o":
        contador+=1
    if i == "u":
        contador+=1
print("En esta frase hay",contador,"vocales")

"""
Ejercicio 16:
Escribir un programa que determine si una cadena de texto dada es un pangrama o no.
Un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez.
Utiliza una variable para almacenar la cadena, itera sobre cada letra y verifica si está presente en el alfabeto, luego muestra el resultado.
"""

frase2="un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez"


    
"""
Ejercicio 17:
Escribir un programa que calcule el máximo común divisor (MCD) de dos números enteros.
Utiliza dos variables para almacenar los números, aplica el algoritmo de Euclides y muestra el resultado.
"""
num1=5
num2=20
mcd = 0

for i in range(1, max (num1, num2) + 1):
        if num1%i==0 and num2%i==0:
            mcd = i
         
    
print  ("El máximo común divisor de",num1,"y",num2,"es: ",mcd)

"""
Ejercicio 18:
Crear un programa que calcule la potencia de un número dado elevado a otro número entero.
Utiliza dos variables para almacenar la base y el exponente, realiza el cálculo de la potencia y muestra el resultado.
"""

"""
Ejercicio 19:
Escribir un programa que calcule el área de un círculo dado su radio, utilizando una función.
La función debe recibir el radio como argumento y devolver el área del círculo.
"""

"""
Ejercicio 20:
Crear un programa que determine si un número dado es perfecto o no.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
Utiliza una variable para almacenar el número, realiza los cálculos y muestra el resultado.
"""
