from functools import reduce

'''
    Se quiere crear un programa en Python para gestionar una listade tareas pendientes. El programa
    debe permitir al usuario agregar nuevas tareas, marcar tareas como completadas, eliminar tareas de la lista
    y ver todas las tareas pendientes.
   
    El programa debe de comenzar mostrando un menú de opciones al usuario, donde pueda seleccionar la
    operación que desea realizar. Se elige agregar una nueva tarea, debe ingresar la descripción de la tarea y agreagarla
    a la lista de tareas pendientes.Si se marca una tarea como completa, debe mostrar la lista de tareas pendientes
    y permitir al usuario seleccionar la tarea que desea marcar como completa.
   
    Cuando un usuario completa una tarea, debe eliminarse de la lista de tareas pendientes y agregarse a la lista
    de tareas completas. Ahi se almacena su descripción y la fecha en la que se completo. El programa tambien debe
    permitir a el usuario eliminar tareas pendientes si ya no son necesarias.
   
    Para ayudar al usuario a mantenerse organizado debe haber una opción para ver tods las tareas pendientes mostrando
    descripción y ID unico. Esto facilita la referencia cuando el usuario quiera eliminar una tarea.
'''
class Tarea:
    def __init__(self, idTarea, descripcion, fechaEntrada, fechaFin, completada) :
        self.idTarea=idTarea
        self.descripcion=descripcion
        self.fechaEntrada=fechaEntrada
        self.fechaFin=fechaFin
        self.completada=completada
    def agregarTarea (self, tarea, listaTareas):        
        listaTareas.append(tarea)
        
    def tareaCompleta (self, tarea, listaTareas):      
        if tarea  in listaTareas:
            self.completada=True
            self.fechaFin="TERMINADA"    
    def eliminarTarea (self, tarea, listaTareas):
        listaTareas.remove(tarea)
        if tarea not in listaTareas:
            self.completada=False
    
    def mostrarInfo(self):
        print("ID: ",self.idTarea," Descipcion: ",self.descripcion," Fecha entrada: ",self.fechaEntrada," Fecha fin: ",self.fechaFin," Completada: ",self.completada)
    
    def mostrarListaTareas(self, listaTareas):
        ''' for i in range(len(listaTareas)):
            print(listaTareas[i].mostrarInfo())'''
        print(list(map(mostrarInfo(), listaTareas)))
    
listaTareas=[]            
t1 = Tarea ("001","realizar el examen","26/042024","--/--/---",False)
t2 = Tarea ("002", "comprobar errores", "26/04/2024","--/--/----",False)
t3 = Tarea ("003", "estar relajado","26/04/2024", "--/--/----", False)

t1.agregarTarea(t1, listaTareas)
t2.agregarTarea(t2, listaTareas)
t3.agregarTarea(t3, listaTareas)
t3.mostrarListaTareas(listaTareas)
t2.tareaCompleta(t2, listaTareas)
t3.mostrarListaTareas(listaTareas)
