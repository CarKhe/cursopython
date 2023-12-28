class Geto:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

p = Perro()
g = Geto()

hacer_sonido(g)