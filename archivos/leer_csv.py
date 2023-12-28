import csv
with open("archivos\\archivo_csv.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print (row)