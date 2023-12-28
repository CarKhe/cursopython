"""
Falto el profesor
1 alumno profesor
1 asistente


(A)
Pedir edad de los compañeros que fueron a 
clases y ordenarlos de menor a mayor

(B)
El mayor es el profesor y el emnor el
asistente

"""


def ingresar_alumno(cant):
    compañeros = []
    for i in  range(cant):
        nombre = input("Ingresa el nombre:")
        edad = int(input("Ingresa edad:"))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key= lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente,profesor = ingresar_alumno(3)

print(f"El profesor será: {profesor}")
print(f"El asistente será: {asistente}")
