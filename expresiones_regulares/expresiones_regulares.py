import re 

texto = '''Lorem ipsum dolor 78 sit amet consectetur adipiscing, elit diam faucibus nec laoreet lectus, id phasellus tellus imperdiet montes
Inceptos tempus urna fames sem cum vulputate nisl, ullamcorper avavababab 23. ligula pulvinar abababab bibendum mi euismod sagittis rhoncus, phasellus 34 nascetur praesent nibh curae sociis. 
Magnis eu fringilla  657 ad abababaabababab tellus facilisi per quis litora faucibus donec ultricies orci non at, 
penatibus lacus nascetur cras mattis mi interdum semper 657 tristique ligula aenean himenaeos dapibus.'''

resultado = re.search("mi",texto)
resultado = re.findall("mi",texto, flags=re.IGNORECASE)

# \d buscar digitos numericos
resultado = re.findall(r"\d",texto)
# \D buscar TODO menos digitos numericos
resultado = re.findall(r"\D",texto)
# \w buscar caracteres alfanumericos[a-z A-Z 0-9 _] 
resultado = re.findall(r"\w",texto)
# \W buscar TODO menos caracteres alfanumericos[a-z A-Z 0-9 _] 
resultado = re.findall(r"\W",texto)
# \s busca espacios en blanco tabs y saltos de linea
resultado = re.findall(r"\s",texto)
# \S busca TODO menos espacios en blanco tabs y saltos de linea
resultado = re.findall(r"\S",texto)
# \n busca saltos en line
resultado = re.findall(r"\n",texto)
# . busca TODO menos saltos en line
resultado = re.findall(r".",texto)
#\. cancelar caracteres especiales
resultado = re.findall(r"\.",texto)
#armando cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s",texto)

#\^ buscar el comienzo de una linea
resultado = re.findall(r"^Inceptos",texto,flags=re.M)

#\$ buscar el final de una linea
resultado = re.findall(r"montes$",texto,flags=re.M)
#{n} -> busca n cantidad de veces el valor de la izquierda y espacio
resultado = re.findall(r"\d{3}\s",texto)
#{n,n} -> busca n a m cantidad de veces el valor de la izquierda y espacio
resultado = re.findall(r"\d{1,3}\s",texto)
#{n,n} -> busca n a m cantidad de veces el valor de la izquierda y espacio
resultado = re.findall(r"(ab){2}",texto)
resultado = re.findall(r"[ab]{2}",texto)
#| buacar un valor u otro
resultado = re.findall(r"ab|cras",texto)

print(resultado)