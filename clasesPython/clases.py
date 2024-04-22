class Persona:
    
    def __init__(self,nombre,apellidos,edad):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        
    def decirHola(self):
        print("Hola me llamo", self.edad)
    def __str__(self) -> str:
        return "Nombre: " + self.nombre+" ,  apellidos: "+self.apellidos+ ", edad: "+ str(self.edad) 
    def __eq__(self, value):
        if self.apellidos == value.apellidos:
            return True
    
p1=Persona("David", "Martinez Moraleda", 30)
p2=Persona("Alejandro", "Martinez Moraleda", 25)

p1.decirHola()
print(p1)
print(p1==p2)

class Humano(Persona):
    def __init__(self,nombre,apellidos,edad):
        super().__init__(nombre,apellidos,edad)
    def decirHola(self):
        print("Hola me llamo", self.edad)
    def __str__(self) -> str:
        return "Nombre: " + self.nombre+" ,  apellidos: "+self.apellidos+ ", edad: "+ str(self.edad) 
    def __eq__(self, value):
        if self.apellidos == value.apellidos:
            return True
