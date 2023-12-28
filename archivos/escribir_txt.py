with open("archivos\\txt.txt",'w',encoding="utf-8") as archivo:
    #archivo.write("Que pedo cachorros")
    archivo.writelines(["holaaaaaa\n","Kiongo"])
    
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i+1} agregado\n")