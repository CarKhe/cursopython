class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola soy una persona")

class Empleado(Persona):
    def __init__(self,nombre,edad,empleado,trabajo,salario):
        super().__init__(nombre,edad,empleado)
        self.trabajo = trabajo
        self.salario = salario
    def hablar(self):
        print("Hola soy un empleado")
class Director(Persona):
    def __init__(self,nombre,edad,empleado,departamento):
        super().__init__(nombre,edad,empleado)
        self.departamento = departamento
    def hablar(self):
        print("Hola soy un Director")


e1 = Director("Carlos",24,"Mexicano","Contabilidad")

e1.hablar()