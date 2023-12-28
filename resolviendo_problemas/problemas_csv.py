import pandas as pd
df = pd.read_csv("resolviendo_problemas\\a_csv.csv")
df['age'] = df['age'].astype(str)
print(df['age'][4])
print(type(df['age'][4]))

df['name'].replace("Panam","Judy",inplace=True)
print(df['name'])

#print(df)
#borrar filas faltantes
df= df.dropna()
#borrar de las columnas
#df= df.dropna(axis=1)
print(df)


#eliminar filas repetidas
df=df.drop_duplicates()
print(df)


#Crear csv con el dataframe resultante(limpio)
df.to_csv("resolviendo_problemas\\a_csv_limpio.csv")
