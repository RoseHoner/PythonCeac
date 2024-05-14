'''
modos:
r para abrir archivo de lectura
w para escribir fichero desde 0| si el fichero no existe lo crean
a añadir texto nuevo           |

'''



try:         #_____ruta_____  _modo_ __Encoding__
   with open("./ejemplo.txt", "w", encoding="UTF-8") as archivo:
       archivo.write("Hola buenas!\n")
       print("Se ha escrito con éxito")
except IOError as e:
    print("Error en la escritura del archivo"+str(e))
    
    
try:         #_____ruta_____  _modo_  __Encoding__
   with open("./ejemplo.txt", "a", encoding="UTF-8") as archivo:
       archivo.write("Hola buenas\n")
       print("Se ha escrito con éxito")
except IOError as e:
    print("Error en la escritura del archivo"+str(e))
    
try:         #_____ruta_____  ____modo_____
   with open("./ejemplo.txt", "r") as archivo:
       print(archivo.read())
except IOError as e:
    print("Error en la escritura del archivo"+str(e))