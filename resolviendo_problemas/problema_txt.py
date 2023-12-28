#Liscas con  nombre y apellido

nombres = ["lucas","Matias","Camila"]
apellidos = ["Galto","Tarado","Robertix"]

with open('resolviendo_problemas\\n_ya.txt','w') as arch:
    arch.writelines('Los datos son:\n ')
    [arch.writelines(f"Nombre:{n}\n Apellido:{a}\n -------\n") for n,a in zip(nombres,apellidos)]
    
    