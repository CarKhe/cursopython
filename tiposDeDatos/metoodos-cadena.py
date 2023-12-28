"""
DIR - Devolver la lista de atributos validos del objeto pasado (funcion)

UPPER - convertir a mayusculas
LOWER - convertir a minusculas
CAPITALIZE - primera mayuscula

FIND - encuentra la primera aparicion del valor especificado, si no deuvelve -1
INDEX - encuentra la primera aparicion del valor especificado, sin no deuvelve exepcion

ISNUMERIC - si es nuemrico devuelve TRUE
ISALPHA - si es alfa numerico devuelve TRUE

COUNT - devuelve el num de ocurrencias de una subcadena en la cadena dada
LEN - cuenta caracteres de la cadena

ENDSWITH verifica si una cadena comienza con 
STARTSWITH verifica si una cadena termina con 

REPLACE - Remplaza valor por otro
SPLIT - separa por el parametro dado

"""


cadena1 = "caaaaaaaarlos Rdz"
cadena2 = "c,a,r,l,o,s"
cadena3 = "54"

#Estructura de los parametros
mayusc = cadena1.upper()
minusc = cadena2.lower()
capital = cadena1.capitalize()

#Buscar string en otro string 
busqueda_find = cadena1.find("w") #Aparece en la posicion del string si no hay coincidencia sale -1
busqueda_index = cadena2.index("r") # si no aparece manda una excepecion 

#es numerico lanza true si no false
es_numerico = cadena3.isnumeric()
#Solo son validos de la a (a-z)
es_alfanumerico = cadena2.isalpha()

#devolver la cantidad de que coincida
es_count = cadena1.count("a")

# contar cuantos caracteres tiene una cadena
es_len = len(cadena1) #Funcion

#Verificar si una cadena inicia con otra cadena
empieza_con = cadena1.startswith("car")
#Verificar si una cadena termina con otra cadena
finaliza_con = cadena1.endswith("Rdz")

#remplaza un pedazo de la cadena dada por otra dada
cadena_nueva = cadena2.replace("car","record")

#Separar cadenas con la cadena que pasemos
cadena_separada = cadena2.split(",")
print (cadena_separada[4])