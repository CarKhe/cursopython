#Crear funcion que devuelva los numeros primos
#entre 0 y el argumento pasado

def numero_primos(num):
    for i in range(2,num-1):
        if num%i==0:  return False
    return True

def primo_hasta(num):
    primos=[]
    for i in range(3,num+1):
        result = numero_primos(i)
        if result == True: primos.append(i) 
    return primos


valor = primo_hasta(17)

print(valor)