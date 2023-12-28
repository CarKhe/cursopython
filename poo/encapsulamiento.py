class MiClase:
    def __init__(self):
        self.valor = "Holaaa"
        self._valor_privado = "Hola"
        self.__Valor_muy_privado= "Carlos" #muy protegido
    def __hablar_muy_privado(self):
        print("Hola privado...")
    def _hablar_privado(self):
        print("Hola no tan privado...")


obj = MiClase()
print(obj._valor_privado)
obj._hablar_privado()