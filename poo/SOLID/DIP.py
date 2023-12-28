#Dependecy Inversion Principle
#Los modulos de alto nivel no dependan del bajo nivel, si no los dos deben depender de la abstraccion
#Las abstracciones no deben depender de los detalles si no que el detalle depender de la abstraccion
#Clases de alto nivel mantenerse de forma independiente  de las de bajo nivel (Las que hacen tareas espeificas)
#Facilita el testeo

# class Diccionario:
#     def verificar_palabra(self,palabra):
#         #Logica
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diciconario = Diccionario()
#     def corregir_texto(self,texto):
#         #usar diccionario para corregirlo
#         pass


from abc import ABC, abstractmethod

class VarificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        #Logica verificar palabras
        pass
    
class Diccionario(VarificadorOrtografico):
    def verificar_palabra(self,palabra):
        #Lofgica verificar palabras si esta en el diccionario
        pass

class ServicioOnline(VarificadorOrtografico):
    def verificar_palabra(self,palabra):
        #Lofgica verificar palabras si esta en el diccionariodesde servicio web
        pass
    
class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #usar verificador para corregir el texto
        pass
    
corrector = CorrectorOrtografico(Diccionario())

online = CorrectorOrtografico(ServicioOnline())