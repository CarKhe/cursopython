#Interface Segregation Principle
#Ningun cliente no tiene que ser forzado depender de interface que no utilice
#Eliminar dependencias que no se van a utilizar

from abc import ABC, abstractmethod

# class Trabajador(ABC):
#     @abstractmethod
#     def comer(self):
#         pass
#     @abstractmethod
#     def trabajar(self):
#         pass
#     @abstractmethod
#     def dormir(self):
#         pass
    
# class Humano(Trabajador):
    
#     def comer(self):
#         print("Humano come")
    
#     def trabajar(self):
#         print("Humano trabaja")
    
#     def dormir(self):
#         print("Humano duerme")
        
# class Robot(Trabajador):
  
#     def trabajar(self):
#         print("Robot trabaja")
    
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Comedor,Trabajador,Durmiente):
    
    def comer(self):
        print("Humano come")
    
    def trabajar(self):
        print("Humano trabaja")
    
    def dormir(self):
        print("Humano duerme")
        
class Robot(Trabajador):
    def trabajar(self):
        print("Robot trabaja")

robot = Robot()

robot.trabajar()