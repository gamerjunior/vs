def funcion2(funcion):
    print("Esta es la función 2")
    def envoltura():
        print("texto antes d funcion")
        funcion()
        print("texto despues de funcion")
    return envoltura

@funcion2
def mi_funcion():
    """"esta es la documentacion de la funcion"""
    print("Esta es mi función")

mi_funcion()
print(mi_funcion.__name__)  # Esto imprimirá "envoltura" en lugar de "mi_funcion"¡
print(mi_funcion.__doc__)  # Esto imprimirá "None" en lugar de la documentación de "mi_funcion"