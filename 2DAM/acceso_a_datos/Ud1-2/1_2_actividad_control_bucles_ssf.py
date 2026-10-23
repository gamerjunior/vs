"""
Actividad 2
Acceso a Datos · UD1 - Introducción a Python

Hoy toca:
    - Estructuras alternativas: if, elif, else
    - Bucles: while, for
    - range() (con y sin len())
    - break, continue, pass

No hace falta usar funciones propias (def) todavía, eso llega después.
Completa cada TODO. Ejecuta y comprueba que el resultado tiene sentido
ANTES de pasar al siguiente ejercicio.
"""


# ===========================================================
# EJERCICIO 1 · El veredicto del Frikímetro
# ===========================================================
# El otro día calculamos un nivel_friki pero solo lo comparábamos con print().
# Hoy vamos a ponerle nombre y apellidos al resultado.

nivel_friki = float(input("Introduce tu nivel friki de ayer (o invéntatelo): "))

# TODO 1: Imprime un veredicto según estas reglas:
#   nivel_friki < 30           -> "Nivel: Novato de la Comarca"
#   30 <= nivel_friki < 70     -> "Nivel: Aficionado con Estilo"
#   nivel_friki >= 70          -> "Nivel: Leyenda Friki Certificada"
if nivel_friki < 30:
    print("Nivel: Novato de la Comarca")
elif 30 <= nivel_friki < 70:
    print("Nivel: Aficionado con Estilo")
else:
    print("Nivel: Leyenda Friki Certificada")


# ===========================================================
# EJERCICIO 2 · El portero
# ===========================================================
# Hay una fiesta muy exclusiva. Para entrar hace falta la contraseña
# correcta: "supercalifragilistico"  (todo en minúsculas)

# TODO 2: escribe un bucle que siga pidiendo la contraseña
#         MIENTRAS lo que se introduzca no sea la contraseña correcta.
#         Cada vez que se intente, suma 1 a "intentos".
contraseña_correcta = "supercalifragilistico"
intentos = 0

while True:
    contraseña_introducida = input("Introduce la contraseña: ")
    intentos += 1
    if contraseña_introducida == contraseña_correcta:
        break

print(f"¡Bienvenido a la fiesta! Te ha costado {intentos} intento(s).")


# ===========================================================
# EJERCICIO 3 · Cuenta atrás para el estreno
# ===========================================================

# TODO 3: escribe un bucle que cuente hacia atrás desde 10 hasta 1
#         (ambos incluidos) e imprima cada número.
#         Al terminar el bucle, imprime "¡Empieza la peli!"
for i in range(10, 0, -1):
    print(i)
print("¡Empieza la peli!")

# ===========================================================
# EJERCICIO 4 · El escáner de vocales 
# ===========================================================

palabra = input("Escribe una palabra o frase: ")
vocales = "aeiouAEIOUÁÉÍÓÚáéíóú"
contador_vocales = 0

# TODO 4: cuenta cuántas vocales hay en tu "palabra"
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1

print(f"Esa palabra tiene {contador_vocales} vocales.")


# ===========================================================
# EJERCICIO 5 · El detector de posiciones 
# ===========================================================

letra_buscada = input("¿Qué letra quieres buscar en la palabra anterior?: ")

# TODO 5: retomando el ejercicio 4, cada vez que aparezca letra_buscada, imprime:
#         "La encontré en la posición i"
#         (Si no aparece ninguna vez, no pasa nada, simplemente no se imprime nada)
for i in range(len(palabra)):
    if palabra[i] == letra_buscada:
        print(f"La encontré en la posición {i+1}")#asi es normal, si no empezaria por el 0

# ¿Ves la diferencia con el ejercicio 4? Allí no nos importaba la posición,
# solo contar. Aquí sí nos importa la posición, así que necesitamos el índice.


# ===========================================================
# EJERCICIO 6 · break y continue: el orden importa
# ===========================================================
# Antes de ejecutar cada bloque, escribe en el comentario "Predicción:"
# qué crees que va a imprimir. LUEGO ejecútalo y comprueba si acertabas.

memes_vistos = ["doge", "pepe", "shrek", "among us", "rickroll"]

print("\n--- Versión A ---")
# Predicción:doge pepe shrek
for meme in memes_vistos:
    print("Revisando:", meme)
    if meme == "shrek":
        break
print("Fin de la búsqueda A")

print("\n--- Versión B ---")
# Predicción:doge pepe 
for meme in memes_vistos:
    if meme == "shrek":
        break
    print("Revisando:", meme)
print("Fin de la búsqueda B")

# TODO 6a: en un comentario, explica con tus palabras por qué la Versión A
#          y la Versión B no imprimen exactamente lo mismo, aunque el
#          bucle y la condición son iguales.
#por que en la version A primero muestra el meme y despues compara con shrek, mientras que en la B primero compara y despues muestra.

print("\n--- Versión C ---")
# Predicción:2 4  contador: 2
contador = 0
for n in range(1, 6):
    if n % 2 != 0:
        continue
    contador += 1
    print("Par encontrado:", n)
print("Total pares (C):", contador)

print("\n--- Versión D ---")
# Predicción: contador: 5 2 4
contador = 0
for n in range(1, 6):
    contador += 1
    if n % 2 != 0:
        continue
    print("Par encontrado:", n)
print("Total pares (D):", contador)

# TODO 6b: ¿por qué "Total pares (C)" y "Total pares (D)" NO dan el
#          mismo número, si el código parece casi idéntico?
#          Pista: ¿qué instrucciones se ejecutan ANTES del continue
#          en cada versión, y cuáles se saltan?
#por que en el c primero comprueba si es par y en la d primero cuenta cuantos numeros han pasado y depues si son pares.

print("\n--- Fin del ejercicio 2 ---")
