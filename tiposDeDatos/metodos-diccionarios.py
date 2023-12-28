"""
keys() - devuelve las llaves
get() - devuelve el valor de una clave
clear() - elimina todos los elementos
pop() - elimina un elemento
items - iterar el diccionario

"""

diccionario = {
    "nombre": "Carlos",
    "apellido" : "Rodriguez",
    "numero" : 245125,
    "Sexo" : "M"
}
llaves = diccionario.keys()

obtener = diccionario.get("apellido")

#borrar = diccionario.clear()

eliminar = diccionario.pop("apellido")

item = diccionario.items()

print(item)