"""
LIST - cuenta cantidad de elementos de una lista

APPEND - agrega un elemento a la lista
INSERT - agrega un elemento a la lista en un indice especifico
EXTEND - agrega variso elementos a la lista

POP - elimiena elemento de una lista, pide indice y devuelve valor
REMOVE - remueve elemento de una lista, pide valor
CLEAR - elimina todos los elementos de una lista

SORT - ordena de lista de forma ascendente y descendente
REVERSE - revierte elementos de uan lista
"""

lista = list(["Carlos", 24, 1.74,"Masculino"])
lista_sort = [123,457,87623,487,923,56,4568,456,34]

resultado = len(lista) #devuelve la cantidad de elementos de la lista

#agregar elemento a la lista
agregar_append = lista.append("JAJAJA")

#agregar elemento a la lista en lugar especifico
agregar_insert = lista.insert(3,"Pa")

#agregar varios elementos a la lista
agregar_extend = lista.extend([12,"Carlos3",False])

#elimina de la lista un elemento en especifico
eliminar_pop = lista.pop(4) #los num nevativos son del ultimo para adelante

#elimina de la lista elemento especifico pero del valor
eliminar_remove = lista.remove("Carlos3")

#elimina todos los elemetos de la lista
#elimina_clear = lista.clear()

#ordenar la lista
ordenar_ascendente = lista_sort.sort()
#Ordenar en reversa
ordenar_descendente = lista_sort.sort(reverse=True)

#invertir elementos
lista.reverse()

#buscar elemento especifico en la listta por su nombre resultando en la posicion 
resultado_busqueda = lista.index(1.74)
print(resultado_busqueda)