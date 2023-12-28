class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def descricion(self):
       print(f"Celular Marca: {self.marca}, del modelo {self.modelo}, con camara: {self.camara}")
    
    

c1 = Celular("Samnsung","S23","48px")  
c2 = Celular("Iphone","14","36px")

c1.descricion()