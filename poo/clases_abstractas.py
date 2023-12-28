from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.activid = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} y soy {self.sexo}")
        
#No se puede por ser abstracto
#carlos = Persona("Carlos",24,"Hombre")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando... {self.activid}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy trabajando como... {self.activid}")



carlos = Trabajador("Carlos",24,"Hombre","Programador")

carlos.presentarse()
carlos.hacer_actividad()