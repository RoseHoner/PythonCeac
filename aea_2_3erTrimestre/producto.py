class Producto:
#Constructor de producto
    def __init__(self, nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.descripcion=""
 #Función que permite añadir o modificar una descripción   
    def modificarInfo(self):
       self.descripcion=input("Introduzca una descripción o su modificación")