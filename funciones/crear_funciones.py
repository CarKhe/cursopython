def saludar(saludo,nombre):
    print(f"Hola {nombre}, {saludo}")
    
def nuevoProfesor(nombre,sexo,materia):
    sexo = sexo.lower()
    if sexo =='mujer':
        adjetivo = 'M'
    elif sexo == 'hombre':
        adjetivo = 'H'
    else:
        adjetivo = 'n/a'
    array = [nombre,adjetivo,materia]
    print(array)

def suma(v1,v2):
    return (v1+v2,"holaaWEE")

def contraseña_random(num):
    chars = "srguieofrelksdnaepiosdprno"
    num_ent = str(num)
    num = int(num_ent[0])
    c1= num - 2
    c2 = num
    c3 = num -5
    contra = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contra)
    
result,we = suma(12,45)
print(f"{result} {we}")
nuevoProfesor("Jose","HOMBRe","Matematicas")
saludar("Holaaa","Carlos")

contraseña_random(1)


