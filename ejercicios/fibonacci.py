#Secuencia fibonacci hasta donde se pida
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

def fibonacci(num):
    secuencia=[0]
    a,b = 0,1
    secuencia.append(a+b)
    for i in range(num):
        if a+b >num: break
        secuencia.append(a+b)
        a,b=b,a+b
    return secuencia

