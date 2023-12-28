def suma(nombre,*numeros):
    return f"{nombre}, tu resultado es: {sum(numeros)}"

resultado = suma("Carlos",12,3,3456,312,4,345,24,34,34)
print(resultado)

def frase(nombre,apellido,apodo):
    return f"{nombre}, bienvenido: {apellido}, apodo: {apodo}"

frase_resultado = frase(apodo="Campeon",nombre="Carlos",apellido="RDZ")
print(frase_resultado)