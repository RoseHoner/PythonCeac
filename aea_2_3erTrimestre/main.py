from producto import Producto
from maquinaExp import Maquina

#Creamos nuestros objetos maquina y productos

m1= Maquina("Robotron")
p1= Producto("Robo-cola", 1.80,1)
p2= Producto("Robo-monster", 2.30,1)
p3= Producto("Robo-sandwich", 3.20,1)

#Aplicamos las funcionalidades desarrolladas y observamos el funcionamiento de nuestro programa
p1.modificarInfo()
m1.agregarProducto(p1)
m1.agregarProducto(p2)
m1.agregarProducto(p3)
m1.agregarProducto(p1)
m1.mostrarProductos()
m1.comprarProducto(p1)
m1.mostrarProductos()
m1.comprarProducto(p2)
m1.mostrarProductos()
m1.comprarProducto(p2)
m1.mostrarProductos()