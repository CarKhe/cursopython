class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})" 
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)    
    
carlos = Persona("Carlos",24)
enrique = Persona("Enrique",24)

result = carlos+enrique
print(result)


#objeto_string = carlos.__str__()
# repre = repr(carlos)
# resultado = eval(repre)
# print(repre)
# print(resultado.nombre)