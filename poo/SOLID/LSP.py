#Liskov's Substitution Principle
#Si B es una subclase de A, la clase A deberia poder utilizarse en todos lo lugares donde B pueda utilizarse

# class Ave:
#     def volar(self):
#         return "Estoy Volando"

# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
    

# def hacer_volar(ave = Ave):
#     return ave.volar()


# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Volando"

class AveNoVoladora(Ave):
    pass