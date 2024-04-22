'''
Escribe una funcion calcular promedio que tome una lista de frases como entrada
y devuelva el promedio de la longitud de las palabras de las frases.
El promedio se redondea a 2 decimales.
Se pueden usar todas las funcioones auxiliares necesarias. se ignoran palabras de 2 o menos carateres, cada palabra se 
identifica los espacios.
Los signos que quedan junto a las palabras se consideran parte de la palabra.

frases["Hola, ¿Como estas?",
        "Me gusta programar en python",
        "Python es genial"]
'''

frases=["Hola, ¿Como estas?",
        "Me gusta programar en python",
        "Python es genial"]

def palabras(x):
    for i in range(len(x)):
            print(i)
print(list(map(palabras, frases)))
    