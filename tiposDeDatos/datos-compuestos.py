#list 
lista = ["carlos","Jose",True,1.75]
print(lista)
lista[1]="Cambio de valor"
print(lista[1])

#tuplas (No se puede modificar)
tupla =("carlos","Jose",True,1.75)
#tupla[2]= "jose torres"
print(tupla[2])

#Creando conjunto (set)
#Se puede reconstruir completamente
#pero no un conjunto individual
#no permite repetir valores
#no se puede acceder por indice
#para acceder se puede ser por un for
conjunto ={"carlos","Jose",True,1.75}
print(conjunto)
conjunto ={"carloscwegfweygwye"}
print(conjunto)

#diccionario (dict) es un json

diccionario = {
    'nombre':'Carlos',
    'canal':'CarKhe',
    'estado':True,
    'altura': 1.74
}

print(diccionario["estado"])