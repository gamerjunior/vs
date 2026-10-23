"""
ACTIVIDAD 0: CALENTAMIENTO CON open(), seek() Y tell()
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Trabajamos con un fichero de texto normal: cada línea termina en salto de línea
y las líneas tienen LONGITUD DISTINTA. 

    f.tell()          -> en qué posición estoy ahora (nº de bytes desde el principio)
    f.seek(pos)       -> salta a la posición pos (desde el principio)
    f.seek(0, 2)      -> salta al FINAL del fichero (+ info en apuntes)
    f.readline()      -> lee hasta el siguiente salto de línea (si estás en final devuelve "")

Completa cada TODO. Usa SOLO caracteres ASCII (sin tildes ni ñ). Al final verás "✅ Todo correcto".
"""

FICHERO = "frases.txt"

# El programa crea el fichero de prueba por ti (no hace falta tocarlo)
with open(FICHERO, "w", encoding="utf-8", newline="") as f:
    f.write("Hola\n")
    f.write("Acceso a Datos es mi modulo favorito\n")
    f.write("Python\n")
    f.write("seek y tell\n")
    f.write("Fin\n")


# ---------------------------------------------------------
# PASO 1 · Leer y mostrar el fichero entero
# ---------------------------------------------------------
# TODO 1: abre FICHERO en modo lectura con un with,
# lee TODO el contenido con read() y guárdalo en la variable "contenido".
with open(FICHERO, "r", encoding="utf-8", newline="") as f:
    contenido = f.read()
print(contenido)
assert contenido.count("\n") == 5


# ---------------------------------------------------------
# PASO 2 · ¿Dónde empieza cada línea? (tell)
# ---------------------------------------------------------
# Vamos a construir una lista "indice" con la posición donde EMPIEZA cada línea.
# Para saber la posición antes de leer cada línea usaremos tell().
indice = []
with open(FICHERO, "r", encoding="utf-8", newline="") as f:
    for linea in f:
        # TODO 2: guarda en "posicion" la posición actual del fichero.
        posicion = f.tell()
        linea = f.readline()
        if linea == "":          # readline() devuelve "" cuando se acaba el fichero
            break
        # TODO 3: añade "posicion" a la lista "indice".
        indice.append(posicion)
print("Índice de líneas:", indice)
assert indice == [0, 5, 42, 49, 61]

#    Fíjate: las líneas miden distinto, así que no hay fórmula para saber dónde empieza
#    la línea n. Por eso hemos tenido que construir el índice leyendo todo el fichero.


# ---------------------------------------------------------
# PASO 3 · Saltar directamente a una línea (seek)
# ---------------------------------------------------------
with open(FICHERO, "r", encoding="utf-8", newline="") as f:
    # TODO 4: salta con seek() a la posición de la línea número 2 (usa la lista "indice";
    # recuerda que se cuenta desde 0) y lee esa línea con readline().
    f.seek(indice[2])
    linea2 = f.readline()
    print("Línea 2:", linea2.strip())
    assert linea2 == "Python\n"

    # TODO 5: vuelve al principio del fichero con y lee solo los 4 primeros
    # caracteres con. Guárdalos en "inicio".
    f.seek(0)
    inicio = f.read(4)
    print("Inicio:", inicio)
    assert inicio == "Hola"

    # TODO 6: ¿en qué posición estás ahora mismo? Guarda en "donde_estoy" el valor de tell().
    donde_estoy = f.tell()
    assert donde_estoy == 4


# ---------------------------------------------------------
# PASO 4 · ¿Cuánto ocupa el fichero?
# ---------------------------------------------------------
with open(FICHERO, "r", encoding="utf-8", newline="") as f:
    # TODO 7: salta al final del fichero y guarda en "tamano" lo que devuelve tell().
    f.seek(0, 2)
    tamano = f.tell()
print("Tamaño:", tamano, "bytes")
assert tamano == 65


# ---------------------------------------------------------
# PASO 5 · Añadir al final
# ---------------------------------------------------------
# TODO 8: abre FICHERO en el modo que AÑADE al final sin borrar lo que hay ("a"),
# y escribe la línea "Una mas\n".
with open(FICHERO, "a", encoding="utf-8", newline="") as f:
    f.write("Una mas\n")

with open(FICHERO, "r", encoding="utf-8", newline="") as f:
    assert len(f.readlines()) == 6

print("Todo correcto")

# ---------------------------------------------------------
# PARA PENSAR (contesta en comentarios):
#  a) ¿Qué pasa si en el TODO 8 usas "w" en vez de "a"? Pruébalo (¡con una copia!).
#  b) ¿Qué posición devuelve tell() justo después de abrir con "a"? ¿Y con "r"?
#  c) Cambia el bucle del PASO 2 por "for linea in f:" e intenta llamar a f.tell() dentro.
#     ¿Qué error da? ¿Por qué crees que Python lo prohíbe?
#  d) ¿Qué ventaja tendría que TODAS las líneas midieran lo mismo?
# ---------------------------------------------------------
