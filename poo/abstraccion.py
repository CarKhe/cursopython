class Auto():
    def __init__(self):
        self._estado = "apagado"
    def encender(self):
        self._estado ="encendido"
        print("Carro encendido")
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo")

mi_auto = Auto()
mi_auto.conducir()