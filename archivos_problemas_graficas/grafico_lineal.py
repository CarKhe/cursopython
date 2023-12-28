import pandas as pd 
import matplotlib.pyplot as plt    
import seaborn as sbs

df = pd.read_csv("archivos_problemas_graficas\\grafico.csv")
sbs.lineplot(x="fecha",y="piezas",data=df)

#punto mas alto
plt.plot("07-01",221,"o")
plt.show()