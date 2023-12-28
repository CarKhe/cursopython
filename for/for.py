#funciona tambien para tuplas y conjuntos
animales = ["Perro","Gato","Castor"]
numeros=(21,687,35,48,86,87,765)

diccionario = {
    "nombre": "Carlos",
    "apellido": "RDZ",
    "edad": 24
}

frutas = ["Manzana","Banana","Ciruela","Pera","Naranja"]

cadena = "Hola Carlos"

#for animal in animales:
    #print(f'La variable es: {animal}')
    
    
for animal,numero in zip(animales,numeros):
    print(f'La variable es: {animal}')
    print(f'La variable es: {numero}')
    
for numero in range(5,10):
    print(numero)

for animal in enumerate(animales):
    index = animal[0]
    value = animal[1]
    print(f'indice: {index}, valor: {value}')

for num in numeros:
    print(f"valor acutal del bucle: {num}")
else:
    print("bucle terminado")
    
for key in diccionario.items():
    print(key)
    
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"Llave: {key} con datos: {value}")
    

for fruta in frutas:
    if (fruta == "Manzana") | (fruta == "Pera"):
        continue
    print(f"Comí: {fruta}")
else:
    print("Terminado")
    
for fruta in frutas:
    if fruta == "Pera" :
        break
    print(f"Comí: {fruta}")

for letra in cadena:
    print(letra)
    
#numeros_duplicados = list()
#for numero in numeros:
#    numeros_duplicados.append(numero*2)
    
numeros_duplicados = [x*2  for x in numeros]

print(numeros_duplicados)