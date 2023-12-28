class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Error en: {err}")
        


#raise ValueError("Error en el modulo")


try:
    raise MiExcepcion("Error no se que")
except:
    print("No vales cabeza")
    
#raise MiExcepcion("Error no se que")