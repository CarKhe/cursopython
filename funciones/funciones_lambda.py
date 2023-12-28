#funciones anonimas
multp_por_2 = lambda x : x*2

print(multp_por_2(4))

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#def es_par(num):
#    if(num%2==0):
#        return True

num_par = filter(lambda x: x%2==0,numeros)

print(list(num_par))