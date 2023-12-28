#Texto
"String"
'String'
"""Lorem ipsum dolor sit amet,
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum."""

'''Lorem ipsum dolor sit amet,
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum.'''

#Tomar un dato y convertirlo a string

nombre = 8
#concatenar con f Strings
bienvenida = f"Hola {nombre},que rollo"
#Borrar variable en la memoria
del nombre
print (bienvenida)

#buscar string en la variable
print("pedro"  in bienvenida) 
#buscar que string no este en la variable
print("pedro" not in bienvenida) 

#operadores de pertenenecia {in / not in}

#camelCase
variableCamelCase = "Hola"

#snake_case (Recomendado para python)
variable_snake_case = "Hola"