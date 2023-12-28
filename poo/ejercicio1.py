class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def descripcion(self):
        print(f"Estudiante: {nombre}, con {edad}, del año: {grado}")
       
    def estudiar(self):
        print("Estudiando...")
    
    def fin(self):
        print("Finalizado...")

nombre= input("Di el nombre: ")
edad= input("Di la edad: ")
grado= input("Di el grado: ")

e = Estudiante(nombre,edad,grado)

e.descripcion()

while True:
    estudiar = input()
    if (estudiar.lower() == "est"):
        e.estudiar()
    elif (estudiar.lower() == "datos"):
        e.descripcion()
    elif (estudiar.lower() == "fin"):
        e.fin()
        break
    