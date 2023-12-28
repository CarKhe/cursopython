class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def set_nombre(self,new_nombre):
        self.__nombre = new_nombre
    def set_edad(self,new_edad):
        self.__edad = new_edad

carlos = Persona("Carlos",24)

print(carlos.get_nombre())

carlos.set_nombre("Enrique")

print(carlos.get_nombre())
