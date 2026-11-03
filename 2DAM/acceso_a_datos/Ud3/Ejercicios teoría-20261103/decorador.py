def mi_decorador(funcion):
    def envoltura():
        """Documentacion envoltura"""
        print("Esto se imprime antes de la función original")
        funcion()
        print("Esto se imprime después de la función original")
    return envoltura

@mi_decorador
def mi_funcion():
    """Documentacion mi funcion"""
    print("Hola")

mi_funcion()
print(mi_funcion.__doc__)