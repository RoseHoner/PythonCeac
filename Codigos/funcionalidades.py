import random as rd
import string as str

print("letras en mayúscula" , str.ascii_uppercase)
print("letras en minúscula" , str.ascii_lowercase)
print("todas las letras" , str.ascii_letters)
print("todos los numeros" , str.digits)
print("todos los numeros hexadecimales", str.hexdigits)
print("todas las formas de representas un espacio",list( str.whitespace))
print("signos de puntacion", str.punctuation)
print("para poner la letra mayuscula de cada palabra en un string", str.capwords("esta es una frase",' '))

print("numeros aleatorios entre [0,1)", rd.random())
print("numeros aleatorios entre 2 valores", rd.randint(0,100))
print("numeros aleatorios dentro de un rango", rd.randrange(1,100,2))

lst=list(str.ascii_letters)
print(rd.choice(lst))
rd.shuffle(lst)
print(lst)

print(rd.choices([1,2,3,4,5,6],[75,5,5,5,5,5],k=1))

print(rd.uniform(5,10))