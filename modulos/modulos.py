import modulo_saludo as num

import funciones_basicas.funciones as fb

import sys 
sys.path.append('c:\\Users\\carlo\\Escritorio\\Curso Python')
from ejercicios.fibonacci import fibonacci 


from modulo_saludo import Saludo as S1,Saludo2 as S2



result = S1("Carlos")
result2 = S2("jose torres")
edad = num.Numero(25)


resultado = fibonacci(4000)

print(result,edad,result2)



print(dir(num))

print(num.__doc__)

print(sys.path)


print(resultado)