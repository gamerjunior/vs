"""
ACTIVIDAD CSV (parte 1): LOS VIDEOJUEGOS CON EL MÓDULO csv
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Trabajamos con videojuegos.csv (en la misma carpeta que este script). Columnas:
    titulo, genero, anyo, precio, horas, nota

Es el mismo planteamiento que el ejemplo de los planetas:
    - csv.reader para leer
    - un @dataclass con __post_init__ (todo llega como texto) y un @property (valor calculado)
    - una función generadora (yield) que devuelve un objeto por cada fila

Completa cada TODO. Al final verás "Todo correcto".
Después haremos EXACTAMENTE lo mismo con pandas (actividad_csv_pandas.py)
y compararemos cuántas líneas de código hemos necesitado.
"""

import csv
from dataclasses import dataclass

FICHERO = "videojuegos.csv"


# ---------------------------------------------------------
# 1 · Lectura "en crudo" (como lectura_csv del ejemplo)
# ---------------------------------------------------------

def lectura_cruda(nombre_fichero):
    """Muestra cada fila del csv como una lista (print(fila))."""
    # TODO 1: abre el fichero en modo lectura con with (encoding="utf-8", newline=""),
    # crea un csv.reader y haz print de cada fila.
    # Fíjate en la fila de "Tomb Raider, Definitive Edition": ¿cuántos elementos tiene?
    with open(nombre_fichero, "r", encoding="utf-8", newline="") as fr:
        reader = csv.reader(fr)
        for fila in reader:
            print(fila)


# ---------------------------------------------------------
# 2 · Clase con tipos y un valor calculado
# ---------------------------------------------------------

@dataclass
class Videojuego:
    titulo: str
    genero: str
    anyo: int
    precio: float
    horas: int
    nota: float

    def __post_init__(self):
        # TODO 2: del csv todo llega como texto. Convierte anyo y horas a int; precio y nota a float.
        self.anyo = int(self.anyo)
        self.precio = float(self.precio)
        self.horas = int(self.horas)
        self.nota = float(self.nota)

    @property          # convierte el método en un atributo calculado: se usa sin paréntesis
    def precio_hora(self):
        """Euros que cuesta cada hora de juego."""
        # TODO 3: devuelve precio entre horas.
        return self.precio / self.horas


# ---------------------------------------------------------
# 3 · Generador de objetos
# ---------------------------------------------------------

def leer_videojuegos(nombre_fichero):
    """Función generadora: devuelve (yield) un Videojuego por cada fila del fichero."""
    with open(nombre_fichero, "r", encoding="utf-8", newline="") as fr:
        reader = csv.reader(fr)
        # TODO 4: salta la cabecera con next(reader); luego recorre las filas y haz
        # yield Videojuego(*fila)   (el * reparte los elementos de la lista como argumentos).
        next(reader)
        for fila in reader:
            yield Videojuego(*fila)


# ---------------------------------------------------------
# 4 · Análisis "a mano" con bucles
# ---------------------------------------------------------

def nota_media(juegos):
    """Devuelve la nota media de todos los juegos (lista de Videojuego)."""
    # TODO 5: suma las notas con un bucle y divide entre cuántos hay.
    suma=0
    for juego in juegos:
        suma += juego.nota
    return suma / len(juegos)


def juegos_buenos(juegos, minimo):
    """Devuelve la lista de TÍTULOS de los juegos con nota >= minimo (respetando el orden del fichero)."""
    # TODO 6: recorre y guarda en una lista los títulos que cumplan la condición.
    return[juego.titulo for juego in juegos if juego.nota >= minimo]


def mas_barato_por_hora(juegos):
    """Devuelve el Videojuego con menor precio_hora."""
    # TODO 7: bucle guardando el mejor visto hasta ahora.
    mejor = juegos[0]
    for juego in juegos:
        if juego.precio_hora < mejor.precio_hora:
            mejor = juego
    return mejor


def nota_media_por_genero(juegos):
    """Devuelve un diccionario {genero: nota media redondeada a 2 decimales}."""
    # TODO 8: usa dos diccionarios (o uno con listas): uno acumula las notas por género y otro
    # cuenta cuántos juegos hay. Al final calcula cada media con round(..., 2).
    suma_notas = {}
    cuenta_juegos = {}
    for juego in juegos:
        if juego.genero not in suma_notas:
            suma_notas[juego.genero] = 0
            cuenta_juegos[juego.genero] = 0
        suma_notas[juego.genero] += juego.nota
        cuenta_juegos[juego.genero] += 1
    return {genero: round(suma_notas[genero] / cuenta_juegos[genero], 2) for genero in suma_notas}

# ---------------------------------------------------------
# 5 · Escritura de un csv nuevo
# ---------------------------------------------------------

def guardar_aventuras(juegos, destino):
    """Guarda en 'destino' los juegos de género Aventura ordenados de MÁS a MENOS caro,
    con cabecera titulo,precio,nota."""
    # TODO 9: filtra los de Aventura, ordénalos con sorted(lista, key=lambda j: j.precio, reverse=True),
    # abre 'destino' con "w" (encoding="utf-8", newline="") y escribe con csv.writer:
    # primero la cabecera con writerow, luego una fila por juego.
    
    aventuras = [juego for juego in juegos if juego.genero == "Aventura"]
    aventuras_ordenadas = sorted(aventuras, key=lambda j: j.precio, reverse=True)
    with open(destino, "w", encoding="utf-8", newline="") as fw:
        writer = csv.writer(fw)
        writer.writerow(["titulo", "precio", "nota"])
        for juego in aventuras_ordenadas:
            writer.writerow([juego.titulo, juego.precio, juego.nota])


# ---------------------------------------------------------
# COMPROBACIONES
# ---------------------------------------------------------

if __name__ == "__main__":
    lectura_cruda(FICHERO)

    juegos = list(leer_videojuegos(FICHERO))
    assert len(juegos) == 12, len(juegos)
    assert juegos[0].anyo == 2017 and juegos[0].precio == 59.99
    assert round(juegos[0].precio_hora, 3) == 0.667

    assert round(nota_media(juegos), 2) == 8.85
    assert juegos_buenos(juegos, 9) == ["Zelda Breath of the Wild", "Hollow Knight", "Hades",
                                        "The Witcher 3", "Stardew Valley", "Celeste", "Uncharted 4"]
    assert mas_barato_por_hora(juegos).titulo == "Stardew Valley"
    assert nota_media_por_genero(juegos) == {"Aventura": 8.97, "Plataformas": 9.2, "Deportes": 7.65,
                                             "Estrategia": 8.85, "RPG": 9.35}

    guardar_aventuras(juegos, "aventuras_csv.csv")
    with open("aventuras_csv.csv", encoding="utf-8", newline="") as f:
        filas = list(csv.reader(f))
    assert filas[0] == ["titulo", "precio", "nota"]
    assert [f[0] for f in filas[1:]] == ["Zelda Breath of the Wild", "Uncharted 4",
                                         "Tomb Raider, Definitive Edition"], filas

    print("Todo correcto")
    print("Líneas de código que has escrito tú: 38")

    # ------------------------------------------------------
    # PARA PENSAR (contesta en comentarios):
    #  a) ¿Qué pasaría con "Tomb Raider, Definitive Edition" si leyeras con linea.split(",")?
    #       pasaría que se dividiría en dos elementos: "Tomb Raider" y " Definitive Edition", perdiendo la integridad del título.
    #  b) Abre aventuras_csv.csv en el bloc de notas. ¿Cómo ha escrito csv.writer el título con coma?
    #       Lo ha escrito entre comillas: "Tomb Raider, Definitive Edition"
    #  c) ¿Por qué hace falta newline="" al abrir un csv?
    #       Para evitar que se agreguen líneas en blanco adicionales al escribir en el archivo CSV, especialmente en Windows.
    # ------------------------------------------------------
