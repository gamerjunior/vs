"""
📝 ACTIVIDAD 0B: EL BLOC DE TAREAS
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Aquí NO te damos el código: te damos el esqueleto (nombre de cada función, qué recibe
y qué debe devolver) y TÚ escribes el cuerpo. Todo con funciones normales:
nada de clases ni decoradores por hoy.

El fichero tareas.txt guarda UNA tarea por línea (las líneas miden distinto).
Herramientas: open() con sus modos, with, read(), readline(), readlines(),
write(), seek(), tell().

Reglas:
  - Abre SIEMPRE con:  open(FICHERO, modo, encoding="utf-8", newline="")  y usa with.
  - Solo caracteres ASCII (sin tildes ni ñ).
  - Las funciones que devuelven texto lo devuelven SIN el "\\n" final.
  - Al final hay comprobaciones: si todo está bien verás "✅ Todo correcto".
    Ve probando función a función (puedes comentar las comprobaciones de las que aún no tengas).
"""

FICHERO = "tareas.txt"
INICIALES = [
    "Comprar pan",
    "Estudiar seek y tell",
    "Llamar a la abuela",
    "Entregar la actividad de Python",
    "Dormir",
]


# ---------------------------------------------------------
# 1 · Crear y leer
# ---------------------------------------------------------

def crear_fichero(lineas):
    """Crea (o machaca) FICHERO con una línea por cada texto de la lista 'lineas'."""
    # TODO: ¿qué modo de open() crea el fichero o lo vacía si ya existe? Escribe cada texto + "\n".
    ...


def leer_todas():
    """Devuelve una lista con todas las líneas, sin el salto de línea final."""
    # TODO: lee con readlines() (o con un for) y quita el "\n" de cada línea (rstrip o strip).
    ...


def contar_lineas():
    """Devuelve cuántas tareas hay."""
    # TODO: cuéntalas (no hace falta seek).
    ...


# ---------------------------------------------------------
# 2 · Posiciones: tell() y seek()
# ---------------------------------------------------------

def tamano_fichero():
    """Devuelve el tamaño del fichero en bytes SIN leer su contenido."""
    # TODO: pista: seek(0, 2) y tell().
    ...


def construir_indice():
    """Devuelve una lista con la posición (en bytes) donde EMPIEZA cada línea.
    Para las INICIALES debe ser [0, 12, 33, 52, 84]."""
    # TODO: bucle con while True: guarda tell() ANTES de cada readline(); sal cuando readline() devuelva "".
    # (no uses "for linea in f", con tell() da error).
    ...


def leer_linea(n, indice):
    """Devuelve la línea número n (desde 0, sin '\\n') saltando directamente con seek,
    usando la lista 'indice'. Si n no existe, devuelve None."""
    # TODO: comprueba que n es válido; abre, haz seek(indice[n]) y readline().
    ...


def leer_desde(posicion, cuantos):
    """Salta a 'posicion' y devuelve los 'cuantos' caracteres siguientes (read(cuantos))."""
    # TODO: seek + read.
    ...


# ---------------------------------------------------------
# 3 · Modificar
# ---------------------------------------------------------

def anadir_tarea(texto):
    """Añade una tarea al final sin borrar las anteriores."""
    # TODO: modo "a".
    ...


def buscar(texto):
    """Devuelve la lista de NÚMEROS de línea (desde 0) cuyas tareas contienen 'texto'
    (sin distinguir mayúsculas de minúsculas)."""
    # TODO: recorre con enumerate y compara en minúsculas.
    ...


def borrar_linea(n):
    """Borra la tarea número n. Devuelve True si se borró, False si n no existe."""
    # TODO: en un fichero de líneas de distinta longitud no se puede 'borrar en sitio':
    # lee todas las líneas, quita la n y reescribe el fichero entero (crear_fichero te sirve).
    ...


# ---------------------------------------------------------
# 4 · RETO: la última línea sin leer todo el fichero
# ---------------------------------------------------------

def ultima_linea():
    """Devuelve la última tarea (sin '\\n') SIN recorrer todo el fichero. Si está vacío, None.
    Pista: abre en modo binario "rb" (allí seek(-1, 2) sí funciona: un byte antes del final)
    y ve retrocediendo de byte en byte hasta encontrar el salto de línea anterior (b"\\n").
    Al final decodifica con .decode("utf-8")."""
    # TODO: reto. Salta al final, ignora el último "\n" y retrocede hasta el "\n" anterior.
    ...


# ---------------------------------------------------------
# COMPROBACIONES
# ---------------------------------------------------------

if __name__ == "__main__":
    crear_fichero(INICIALES)
    assert leer_todas() == INICIALES, leer_todas()
    assert contar_lineas() == 5
    assert tamano_fichero() == 91, tamano_fichero()

    indice = construir_indice()
    assert indice == [0, 12, 33, 52, 84], indice
    assert leer_linea(2, indice) == "Llamar a la abuela"
    assert leer_linea(4, indice) == "Dormir"
    assert leer_linea(7, indice) is None
    assert leer_desde(12, 7) == "Estudia"

    anadir_tarea("Hacer ejercicio")
    assert contar_lineas() == 6
    assert leer_todas()[:5] == INICIALES          # lo anterior sigue ahí
    assert buscar("LLAM") == [2]
    assert buscar("a") == [0, 1, 2, 3, 5]
    assert buscar("zzz") == []

    assert ultima_linea() == "Hacer ejercicio"
    assert borrar_linea(1) is True
    assert borrar_linea(50) is False
    assert contar_lineas() == 5
    assert "Estudiar seek y tell" not in leer_todas()
    assert ultima_linea() == "Hacer ejercicio"
    crear_fichero([])
    assert ultima_linea() is None

    print("✅ Todo correcto")
