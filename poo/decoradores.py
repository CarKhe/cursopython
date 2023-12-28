def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de ejecutar al funcion")
    return funcion_modificada

# def saludo():
#     print("Hola carlos")
    

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludar():
    print("Hola carlos")
    
saludar()