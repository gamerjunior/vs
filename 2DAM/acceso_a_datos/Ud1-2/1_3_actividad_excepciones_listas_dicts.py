"""
Actividad 3 
Acceso a Datos · UD1 - Introducción a Python

Hoy toca combinar:
    - Listas (indexado, len, append, pop)
    - Diccionarios (acceso, keys/values/items, pop)
    - Excepciones (try / except / else / finally)

AVISO: en clase solo vimos ValueError y ZeroDivisionError como ejemplos,
pero al trabajar con listas y diccionarios te vas a encontrar con DOS
tipos de error nuevos: IndexError y KeyError. No pasa nada, funcionan
exactamente igual: el nombre solo cambia según qué haya fallado.
    - IndexError  -> pides una posición de una lista que no existe
    - KeyError    -> pides una clave de un diccionario que no existe

Completa cada TODO. Ejecuta y comprueba el resultado antes de seguir.
"""


# ===========================================================
# EJERCICIO 1 · La estantería de funkos (listas + IndexError)
# ===========================================================

coleccion_funkos = ["Goku", "Baby Yoda", "Deadpool", "Pikachu", "Homelander"]

posicion = input("¿Qué posición de la estantería quieres ver (0 a 4)?: ")

# TODO 1: dentro de un try, convierte "posicion" a int y muestra
#         coleccion_funkos[posicion_int].
#         Añade un except IndexError que muestre un mensaje simpático
#         tipo "Esa balda de la estantería está vacía"
#         Añade también un except ValueError por si no se ha escrito
#         un número, con el mensaje "Eso no es un número"


# ===========================================================
# EJERCICIO 2 · La lista de precios (diccionarios + KeyError)
# ===========================================================

precios_funkos = {
    "Goku": 16.99,
    "Baby Yoda": 19.50,
    "Deadpool": 14.95,
}

nombre_funko = input("¿De qué funko quieres saber el precio?: ")

# TODO 2: dentro de un try, muestra precios_funkos[nombre_funko].
#         Añade un except KeyError que muestre:
#         "Ese funko no está en catálogo... ¿te lo has inventado?"

# ===========================================================
# EJERCICIO 3 · El precio medio de la colección (ZeroDivisionError)
# ===========================================================

# TODO 3: dentro de un try, calcula el precio medio de precios_funkos
#         (pista: sum(precios_funkos.values()) / len(precios_funkos))
#         e imprímelo. Añade un except ZeroDivisionError con el mensaje
#         "No hay ningún funko todavía, no se puede calcular la media"
#         Para comprobar que funciona, prueba primero con el diccionario
#         de arriba y LUEGO con un diccionario vacío: {}


# ===========================================================
# EJERCICIO 4 · La tienda (try / except / else / finally)
# ===========================================================
# Aquí combinamos TODO: una lista (el carrito) y un diccionario (el stock),
# usando la estructura completa try / except / else / finally.

stock_tienda = {
    "camiseta": 5,
    "taza": 2,
    "poster": 0,
}
carrito = []

articulo = input("¿Qué quieres comprar? (camiseta / taza / poster): ")
cantidad = input("¿Cuántas unidades?: ")

# TODO 4: completa esta estructura:
#
# try:
#     cantidad_int = ...                     # conviértelo a int (puede fallar -> ValueError)
#     unidades_disponibles = stock_tienda[...]  # puede fallar -> KeyError si el artículo no existe
# except ValueError:
#     print("La cantidad debe ser un número")
# except KeyError:
#     print("Ese artículo no lo vendemos aquí")
# else:
#     # este bloque solo se ejecuta si NO ha habido ningún error arriba
#     if cantidad_int <= unidades_disponibles:
#         carrito.append(articulo)
#         print(f"¡Añadido! Llevas {len(carrito)} artículo(s) en el carrito")
#     else:
#         print("No queda stock suficiente")
# finally:
#     # esto se ejecuta SIEMPRE, haya ido bien o mal la compra
#     print("Gracias por visitar la Tienda, ¡vuelve pronto!")
