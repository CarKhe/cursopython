import pandas as pd
archivo = pd.read_csv("archivos\\archivo_csv.csv",names=["name","lastname","age"])
archivo2 = pd.read_csv("archivos\\archivo_csv.csv",names=["name","lastname","age"])
#print(archivo[0:3])
df_ordenado=archivo.sort_values("age",ascending=False)
df_concatenado = pd.concat([archivo,archivo2])   
df_head = archivo.head(4)  
df_tail = archivo.tail(1) 
#filas y columnas totales
filas_columnas = archivo.shape
filas = filas_columnas[0] 
columnas = filas_columnas[1]    

filas,columnas = archivo.shape   

#estadistica datashape
df_info = archivo.describe()

#Acceder elemento especifico
elemento_especifico1 = archivo.loc[2]
elemento_especifico = archivo.loc[1]['name']
#con indices
elemento_especifico = archivo.iloc[2,1]
#todas las filas de la columna
elemento_especifico = archivo.iloc[:,1]

#columna mayor que 30
mayor_30 = archivo.loc[archivo["age"]<30,:]

                                                                                                  
print(elemento_especifico)