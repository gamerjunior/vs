"""
🤓 ACTIVIDAD: EL FRIKÍMETRO 🤓
Acceso a Datos · UD1 - Introducción a Python

Hoy toca poner en práctica:
    - Tipos de datos (int, float, str, bool)
    - Operadores (aritméticos, comparación, booleanos)
    - Funciones de entrada y salida (input, print)

MISIÓN: vamos a construir un "frikímetro" que calcule, a partir de
unos datos de lo más random, tu nivel de frikismo oficial.
Ciencia pura y contrastada.

Completa cada TODO. No hace falta usar if ni bucles, ¡solo lo visto hoy!
"""
#Saúl Sánchez Fernández
# ---------------------------------------------------------
# PASO 1 · Recogida de datos (input + casting)
# ---------------------------------------------------------

nombre = input("¿Cómo te llamas, humano? 🧑: ")

# TODO 1: pide la edad por teclado y conviértela directamente a int
edad = int(input("¿Cuántos años tienes?:  "))

# TODO 2: pide cuántas tazas de café / bebidas energéticas tomas al día (int)
tazas_cafe = int(input("¿Cuántas tazas de café / bebidas energéticas tomas al día?:  "))

# TODO 3: pide cuántas horas a la semana ves series / animes / streamers (float)
horas_pantalla = float(input("¿cuantas horas ves series, peliculas, animes, streamer, etc... a la semana?: "))

# TODO 4: pregunta si tiene algún funko, figura o póster friki en su cuarto (S/N)
#          guárdalo tal cual como texto, de momento NO hace falta convertirlo
tiene_funko = input("¿Tienes algún funko, figura o póster friki? (S/N): ")


# ---------------------------------------------------------
# PASO 2 · ¡A darle a los operadores!
# ---------------------------------------------------------

# TODO 5: convierte la respuesta S/N en un booleano.
#         Pista: compara tiene_funko.upper() con "S"
es_friki_declarado = tiene_funko.upper() == "S"

# TODO 6: calcula el nivel_friki con esta fórmula tan científica:
#         nivel_friki = tazas_cafe * 5 + horas_pantalla * 2 + es_friki_declarado * 10
#         (Truco: en Python, True vale 1 y False vale 0 al operar con números 😉
#          así te ahorras un if para sumar el "bonus" de los 10 puntos)
nivel_friki = tazas_cafe * 5 + horas_pantalla * 2 + es_friki_declarado * 10

# TODO 7: calcula si tu nivel_friki es un número par (operador % y ==)
es_par = nivel_friki % 2 == 0

# TODO 8: comprueba si tu nivel_friki supera los 100 puntos (operador >)
eres_leyenda = nivel_friki > 100

# TODO 9: usa el operador ** para calcular tu "poder friki al cuadrado"
poder_al_cuadrado = nivel_friki ** 2


# ---------------------------------------------------------
# PASO 3 · Comprobando los tipos (para fliparlo)
# ---------------------------------------------------------

# TODO 10: imprime con print() y type() de qué tipo son "nivel_friki" y "eres_leyenda"
#          ¿Te esperabas ese tipo? Coméntalo con tu compañero/a.
print("nivel_friki es de tipo:", type(nivel_friki))
print("eres_leyenda es de tipo:", type(eres_leyenda))

# ---------------------------------------------------------
# PASO 4 · El resultado, con estilo (¡los 3 tipos de print de hoy!)
# ---------------------------------------------------------

# TODO 11: usando el operador %, imprime algo como:
#          "Enhorabuena Pepito, tu nivel friki es 87.0"
print("Enhorabuena %s, tu nivel friki es %.1f" % (nombre, nivel_friki))
# TODO 12: usando .format(), imprime algo como:
#          "Pepito, tu nivel friki al cuadrado es nada menos que 7569.0"
print("{}, tu nivel friki al cuadrado es nada menos que {:.1f}".format(nombre, poder_al_cuadrado))
# TODO 13: usando una f-string, imprime el veredicto final, por ejemplo:
#          "🏆 Pepito, ¿eres una leyenda friki? True. ¿Tu número es de la suerte (par)? False"
print(f"{nombre}, ¿eres una leyenda friki? {eres_leyenda}. ¿Tu número es de la suerte (par)? {es_par}")
print("\n--- Gracias por pasar por el Frikímetro Oficial ---")
