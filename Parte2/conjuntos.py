#Creando conjunto con set

conjunto = set(["a", "b"])

conjunto2 =frozenset( {"a", "a"})
conjunto3 = {conjunto2,"dato4"}

print(conjunto3)

conjunto4 = {1,3,5,7}
conjunto5 = {1,3,7}

result = conjunto4.issuperset(conjunto5)
result = conjunto4.issubset(conjunto5)

result = conjunto4.isdisjoint(conjunto5)#Si hay numero en comun

print(result)