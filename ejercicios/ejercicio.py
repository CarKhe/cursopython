#Promedio Cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_cursos = 1.5 

#diferencia de duracion
dif_con_min =100 - (dalto_cursos / otros_cursos_min *100)
dif_con_max =  100 -(dalto_cursos *1000 // otros_cursos_max /10)
dif_con_prom =  100 -(dalto_cursos/ otros_cursos_promedio *100)

print (f"El curso de dalto es {dif_con_min}% más rapido")
print (f"El curso de dalto es {dif_con_max}% más rapido")
print (f"El curso de dalto es {dif_con_prom}% más rapido")