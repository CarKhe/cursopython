class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola soy una persona")
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad =habilidad
    def habilidad(self):
        print(f"mi habilidad es: {self.habilidad}")

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habiliad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habiliad)
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        return super().habilidad()

roberto = EmpleadoArtista("Roberto",24,"Mexicano","Cantar",2500,"Tecs")

roberto.presentarse()

instancia = isinstance(roberto, EmpleadoArtista)
print(instancia)