def suma_2():
    while True:
        try:
            a = input("Val 1: ")
            b = input("Val 2: ")
            r = int(a)/int(b)
        except ValueError as e:
            print("Error en la insercion de datos")
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        else:
            break
        finally:
            print("Ejecuta siempre")
    return r


r=suma_2()
print(r)