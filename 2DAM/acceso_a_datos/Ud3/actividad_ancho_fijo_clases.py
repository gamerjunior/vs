"""
📚 ACTIVIDAD: LA TIENDA DE CÓMICS
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Hoy ponemos en práctica:
    - open() con sus modos (w, a, r, r+) y with
    - seek() / tell() para saltar a un registro concreto
    - Ficheros de ancho fijo
    - Clases: __init__, __repr__, __str__
    - @dataclass y __post_init__
    - Decoradores (con functools.wraps)

El fichero comics.txt guarda UN cómic por línea con columnas de ancho fijo:

    columna      ancho   alineación
    código         4     izquierda
    título        18     izquierda
    precio         7     derecha (2 decimales)
    stock          5     derecha
    + '\\n'         1
                  --
    LONG_LINEA    35 caracteres por registro

Como todas las líneas miden lo mismo, el registro número n empieza
exactamente en la posición n * LONG_LINEA. ¡Eso nos permite saltar a él con seek()!

Completa cada TODO. Al final, el programa tiene unas comprobaciones (assert):
si todo está bien verás "Todo correcto". Usa SOLO caracteres ASCII (sin tildes ni ñ).
"""

import functools
import os
from dataclasses import dataclass

FICHERO = "comics.txt"
ANCHOS = [4, 18, 7, 5]
LONG_LINEA = sum(ANCHOS) + 1      # +1 por el salto de línea


# ===========================================================
# PARTE 1 · Decorador: contar cuántas veces se llama a una función
# ===========================================================

def cuenta_llamadas(func):
    # TODO 1: usa @functools.wraps(func) y define la función interna "envoltorio(*args, **kwargs)".
    # Cada vez que se ejecute debe sumar 1 a envoltorio.llamadas y devolver func(*args, **kwargs).
    @functools.wraps(func)
    def envoltorio(*args, **kwargs):
        envoltorio.llamadas += 1
        return func(*args, **kwargs)
    # TODO 2: inicializa el contador envoltorio.llamadas a 0 y devuelve el envoltorio (sin paréntesis).
    envoltorio.llamadas = 0
    return envoltorio


# ===========================================================
# PARTE 2 · Clase "de toda la vida": __init__, __repr__, __str__
# ===========================================================

class Comic:
    def __init__(self, codigo, titulo, precio, stock):
        # TODO 3: guarda los cuatro parámetros como atributos de la instancia (self.codigo, ...).
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        # TODO 4: devuelve el texto "Comic('0001', 'Tintin', 12.5, 3)" (para programadores:
        # usa !r dentro de la f-string para que los str salgan con comillas).
        return f"Comic({self.codigo!r}, {self.titulo!r}, {self.precio!r}, {self.stock!r})"

    def __str__(self):
        # TODO 5: devuelve algo legible para el usuario, p. ej.: "0001 | Tintin | 12.50 EUR | 3 uds"
        return f"{self.codigo} | {self.titulo} | {self.precio:.2f} EUR | {self.stock} uds"

    def a_linea(self):
        """Convierte el cómic en una línea de ancho fijo (termina en \\n)."""
        # TODO 6: f-string con el formato: código <4, título <18, precio >7.2f, stock >5, y "\\n" al final.
        return f"{self.codigo:<4}{self.titulo:<18}{self.precio:>7.2f}{self.stock:>5}\n"


# ===========================================================
# PARTE 3 · La misma idea con @dataclass + __post_init__
# ===========================================================

@dataclass
class ComicDC:
    codigo: str
    titulo: str
    precio: float
    stock: int = 0

    def __post_init__(self):
        # TODO 7: al leer de un fichero todo llega como texto. Convierte precio a float y stock a int.
        self.precio = float(self.precio)
        self.stock = int(self.stock)
        # TODO 8: si el precio es negativo, lanza ValueError("Precio negativo").
        if self.precio < 0:
            raise ValueError("Precio negativo")

    @classmethod
    def desde_linea(cls, linea):
        """Trocea una línea de ancho fijo y devuelve un ComicDC."""
        # TODO 9: corta la línea con slicing según ANCHOS (0:4, 4:22, 22:29, 29:34) y quita
        # los espacios sobrantes con .strip(). Devuelve cls(codigo, titulo, precio, stock).
        codigo = linea[0:4].strip()
        titulo = linea[4:22].strip()
        precio = linea[22:29].strip()
        stock = linea[29:34].strip()
        return cls(codigo, titulo, precio, stock)


# ===========================================================
# PARTE 4 · Trabajando con el fichero: open, seek, tell
# ===========================================================

def crear_fichero(comics):
    """Crea (o machaca) comics.txt con la lista de Comic recibida."""
    # TODO 10: abre FICHERO en modo escritura ("w") con encoding="utf-8" y newline="" (usa with)
    # y escribe la línea de cada cómic con a_linea().
    with open(FICHERO, "w", encoding="utf-8", newline="") as f:
        for comic in comics:
            f.write(comic.a_linea())


def anadir_comic(comic):
    """Añade un cómic al final SIN borrar lo que ya hay."""
    # TODO 11: ¿qué modo de open() añade al final sin borrar? Úsalo (encoding y newline como antes).
    with open(FICHERO, "a", encoding="utf-8", newline="") as f:
        f.write(comic.a_linea())


@cuenta_llamadas
def leer_registro(n):
    """Devuelve el ComicDC número n (empezando en 0) SIN leer los anteriores."""
    with open(FICHERO, "r", encoding="utf-8", newline="") as f:
        # TODO 12: salta con seek() a la posición n * LONG_LINEA, lee UNA línea con readline()
        # y devuelve ComicDC.desde_linea(linea).
        f.seek(n * LONG_LINEA)
        linea = f.readline()
        return ComicDC.desde_linea(linea)


def contar_registros():
    """Cuántos cómics hay, sin leer el fichero entero."""
    with open(FICHERO, "r", encoding="utf-8", newline="") as f:
        # TODO 13: ve al final con f.seek(0, 2), pregunta la posición con f.tell()
        # y divide (división entera) entre LONG_LINEA.
        f.seek(0, 2)
        return f.tell() // LONG_LINEA


def cambiar_stock(n, nuevo_stock):
    """Modifica EN SITIO el stock del registro n, sin reescribir el resto del fichero."""
    # TODO 14: abre en modo "r+" (leer y escribir). Salta al registro n con seek,
    # y luego avanza hasta la columna del stock (4+18+7 = 29 caracteres más).
    # Escribe nuevo_stock con formato f"{nuevo_stock:>5}".
    with open(FICHERO, "r+", encoding="utf-8", newline="") as f:
        f.seek(n * LONG_LINEA + 29)
        f.write(f"{nuevo_stock:>5}")


def leer_todos():
    with open(FICHERO, "r", encoding="utf-8", newline="") as f:
        return [ComicDC.desde_linea(linea) for linea in f]


# ===========================================================
# PROGRAMA PRINCIPAL (comprobaciones)
# ===========================================================

if __name__ == "__main__":
    # --- Clase normal
    c = Comic("0001", "Tintin", 12.5, 3)
    assert repr(c) == "Comic('0001', 'Tintin', 12.5, 3)", repr(c)
    assert str(c) == "0001 | Tintin | 12.50 EUR | 3 uds", str(c)
    assert c.a_linea() == "0001" + "Tintin".ljust(18) + "  12.50" + "    3" + "\n", repr(c.a_linea())
    assert len(c.a_linea()) == LONG_LINEA

    # --- Fichero
    crear_fichero([c, Comic("0002", "Asterix", 9.95, 10), Comic("0003", "Mortadelo", 7, 0)])
    assert os.path.getsize(FICHERO) == 3 * LONG_LINEA
    anadir_comic(Comic("0004", "Superlopez", 8.25, 4))
    assert contar_registros() == 4

    # --- Seek + dataclass
    d = leer_registro(2)
    print(d)                       # el repr automático de @dataclass
    assert d == ComicDC("0003", "Mortadelo", 7.0, 0)
    assert leer_registro(3).titulo == "Superlopez"

    # --- Modificar en sitio
    cambiar_stock(1, 99)
    assert leer_registro(1).stock == 99
    assert leer_registro(0).stock == 3          # el resto no se ha tocado
    assert os.path.getsize(FICHERO) == 4 * LONG_LINEA

    # --- Validación
    try:
        ComicDC("0009", "Roto", "-5", 1)
        raise AssertionError("debería haber lanzado ValueError")
    except ValueError as e:
        print("Error esperado:", e)

    # --- Decorador
    assert leer_registro.llamadas == 4, leer_registro.llamadas
    assert leer_registro.__name__ == "leer_registro"   # gracias a functools.wraps

    print("Todo correcto")

    # ------------------------------------------------------
    # PARA PENSAR (contesta en comentarios):
    #  a) ¿Qué pasaría si añadimos "Pequeño Ñandú" como título (con tildes) y luego
    #     llamamos a leer_registro(n) con un n posterior? Pruébalo.
    #     (Pista: seek() en modo texto cuenta BYTES, no caracteres.)
    #  b) ¿Qué ocurre si abres con "w" en vez de "a" en anadir_comic?
    #  c) ¿Por qué usamos newline=""?
    # ------------------------------------------------------
