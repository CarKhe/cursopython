import re

# text = "The quick brown fox jumped over the lazy dog"

# x = re.search("^The.*dog$", text)

# if x:
#     print("SI")
# else:
#     print("NO")


# text = "La fecha es 23/06/2023 y el telefono es el +1-555-5555"

# pattern = r"\d{2}/\d{2}/\d{4}"

# replacement = "Fecha Oculta"

# new_text = re.sub(pattern,replacement,text)

# print("Texto modificado: ",new_text)

# text = "remplazando vocales por asteriscos"

# new_text = re.sub("[aeiou]","*",text)

# print(new_text)

# email = "example@example.com"
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# result = re.match(pattern, email)

# if result:
#     print("Correcto")
# else:
#     print("invalido")

text = "Esto es un ejemplo de pagina web: https://www.youtube.com/ y se puede visitar" 
pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
result =re.findall(pattern, text)
print(result)