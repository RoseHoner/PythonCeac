from producto import Producto

class Maquina:
#constructor Maquina
    def __init__(self, name):
        self.name=name
        self.listaProductos=[]
#Función que permite agregar un producto y aumentar su cantidad, si no estuviese añadido previamente lo añade a la lista de productos de la maquina        
    def agregarProducto(self, Producto):
        if Producto  in self.listaProductos:
            Producto.cantidad= Producto.cantidad+1
        else:
            self.listaProductos.append(Producto)
       
        print("El producto ha sido añadido")
#Funcion que resta cantidad de producto hasta que este se agota que quita el producto de nuestra maquina        
    def restarProducto(self, Producto):
        Producto.cantidad=Producto.cantidad-1
        if Producto.cantidad == 0:
            self.listaProductos.remove(Producto)
#Funcion que muestrea detalladamente los datos de nuestros productos en la maquina    
    def mostrarProductos(self):
        for Producto in self.listaProductos:
            print("Nombre: ", Producto.nombre, "Precio: ", Producto.precio, "Cantidad: ", Producto.cantidad, "Descripción: ", Producto.descripcion)
#Funcion para comprar un producto, en la que se llama a restar para que la cantidad y las elecciones siempre esten disponibles,
# en caso de cantidad 0 avisa de que no queda stock    
    def comprarProducto(self, Producto):
        if Producto in self.listaProductos:
           self.restarProducto(Producto)
           print("Gracias por su compra!")
        else:
            print("No queda stock del producto seleccionado!")