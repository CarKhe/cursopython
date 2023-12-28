class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self) -> str:
        return f'{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad})'
    
    def __add__(self, other):
        nuevo_nombre = self.nombre +"-"+other.nombre
        nueva_fuerza = round(((self.fuerza + other.fuerza)/2)**1.2)
        nueva_velocidad = round(((self.velocidad + other.velocidad)/2)**1.2)
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    

luffy = Personaje("Luffy",78,80)
zoro = Personaje("Zoro",90,67)
sanji = Personaje("Sanji",95,85)
result = luffy +zoro
result = result + sanji
print(result)