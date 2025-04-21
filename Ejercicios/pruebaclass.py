'''
Ejercicio 5
Desarrolla un programa que maneje una lista de reservas de un hotel. 
Cada reserva está representada por un diccionario que incluye información como el nombre del cliente,
número de noches reservadas y tipo de habitación.
El objetivo es identificar aquellas reservas que exceden una estancia de 5 noches, 
procesar la información para calcular el total 
de noches reservadas por esos clientes y determinar el tipo de habitación más demandado entre esas reservas
largas.
'''
from functools import reduce
reservas = [
    {"nombre": "Carlos", "noches": 4, "tipo_habitacion": "estándar"},
    {"nombre": "María", "noches": 7, "tipo_habitacion": "suite"},
    {"nombre": "Juan", "noches": 5, "tipo_habitacion": "estándar"},
    {"nombre": "Elena", "noches": 9, "tipo_habitacion": "suite"},
    {"nombre": "Pedro", "noches": 6, "tipo_habitacion": "doble"},
    {"nombre": "Lucía", "noches": 3, "tipo_habitacion": "estándar"}
]

filtrado1=list(filter(lambda x: x["noches"]>=5, reservas))
filtrado2=reduce(lambda x,y: (x+y["noches"]), filtrado1,0)
print(filtrado2)
def habitacionRepe():
    contador1=0
    contador2=0
    contador3=0
    for i in filtrado1:
        print(i)
        if i['tipo_habitacion']=='suite':
            contador1+=1
        if i['tipo_habitacion']=='doble':
            contador2+=1 
        if i['tipo_habitacion']=='estandar':
            contador3+=1
    if contador1 > contador2 and contador1 > contador3:
        print("la habitación mas demandada es la suite")
    
habitacionRepe()