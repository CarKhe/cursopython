class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
    def set_edad(self,new_edad):
        self.__edad = new_edad
    @nombre.deleter
    def nombre(self):
        del self.__nombre 

carlos = Persona("Carlos",24)

print(carlos.nombre)

carlos.nombre="Enrique" 

print(carlos.nombre)

del carlos.nombre

