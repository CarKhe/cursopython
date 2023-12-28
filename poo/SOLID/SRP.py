#SRP
#Single Responsability Principle
#La clase solo tiene que tener una razon para cambiar (Cada clase tiene que tener solo una responsabilidad o tarea)
#Si la clase tiene que tener 2 reponsabilidades se tiene que dividir para que una haga cada una
#Evitar clase sobrecargadas
#la clase puede realizar su trabajo de forma independiente

class TanqueCombustible:
    def __init__(self,combustible):
        self.combustible = combustible
        
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad 
   
    def get_combustible(self):
        return self.combustible 
    
    def mostrar_cantidad_combustible(self):
        return f"El tanque tiene: {round(self.combustible)}% de capacidad"
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad

class Kilometraje:
    def __init__(self,kilometraje):
        self.kilometraje = kilometraje
        
    def sumar_kilometraje(self,distancia):
        self.kilometraje += distancia
    
    def get_kilometraje(self):
        return self.kilometraje
    
    def mostrar_kilometraje(self):
        return f"Kilometraje de: {self.kilometraje} Kms"

class Auto(TanqueCombustible,Kilometraje): 
    def __init__(self,combustible,kilometraje): 
        TanqueCombustible.__init__(self,combustible)
        Kilometraje.__init__(self,kilometraje)
        self.posicion = 0
        self.combustible = combustible
        
    def mover(self,distancia):
        
        if super().get_combustible()>= (distancia / 5):
            self.posicion += distancia
            super().usar_combustible(distancia / 5) 
            super().sumar_kilometraje(distancia)
            print("Se movio el auto")
        else:
            print("No hay suficiente combustible")
            
    def get_posicion(self):
        return self.posicion
        
    def mostrar_posicion(self):
        return f"Distancia recorrida: {self.posicion} Kms" 
 


auto = Auto(100,5000)

auto.mover(150)
print(auto.mostrar_cantidad_combustible())
print(auto.mostrar_posicion())
print(auto.mostrar_kilometraje())


