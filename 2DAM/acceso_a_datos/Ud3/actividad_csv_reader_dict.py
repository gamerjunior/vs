"""
ACTIVIDAD CSV (2): reader, writer, DictReader y DictWriter
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Trabajamos con los jugadores de una liga escolar. Ficheros (en la misma carpeta):
    jugadores.csv         -> nombre,equipo,posicion,goles,partidos   (con cabecera, comas)
    jugadores_pv.csv      -> los mismos campos SIN cabecera y separados por ';'
    jugadores_sucio.csv   -> con filas a las que les faltan o les sobran columnas

Vas a leer y escribir ficheros con las CUATRO herramientas del módulo csv:
    csv.reader / csv.writer          -> filas = listas   (posicional)
    csv.DictReader / csv.DictWriter  -> filas = diccionarios (por nombre) y muchas opciones útiles

Completa cada TODO. Al final verás "Todo correcto".
Abre SIEMPRE los ficheros con encoding="utf-8" y newline="".
"""

import csv

FICHERO = "jugadores.csv"


# =========================================================
# PARTE 1 · csv.reader y csv.writer (listas)
# =========================================================

def total_goles_reader(nombre_fichero):
    """Suma los goles de todos los jugadores usando csv.reader."""
    total = 0
    with open(nombre_fichero, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        # TODO 1: salta la cabecera con next(reader). Luego recorre las filas y suma int(fila[3]).
        # (con reader, la cabecera es una fila más y las columnas se acceden por POSICIÓN)
        next(reader)  
        for fila in reader:
            total += int(fila[3])
    return total


def resumen_writer(origen, destino):
    """Lee 'origen' con csv.reader y escribe en 'destino' con csv.writer un resumen con
    las columnas nombre,goles_por_partido (goles / partidos redondeado a 2 decimales)."""
    with open(origen, "r", encoding="utf-8", newline="") as fr, \
         open(destino, "w", encoding="utf-8", newline="") as fw:
        reader = csv.reader(fr)
        writer = csv.writer(fw)
        # TODO 2: salta la cabecera de la entrada y escribe la cabecera nueva
        # ['nombre', 'goles_por_partido'] con writerow.
        next(reader)
        writer.writerow(['nombre', 'goles_por_partido'])
        # TODO 3: por cada fila de la entrada, escribe con writerow una lista con el nombre (fila[0])
        # y los goles por partido: round(int(fila[3]) / int(fila[4]), 2)
        for fila in reader:
            writer.writerow([fila[0], round(int(fila[3]) / int(fila[4]), 2)])

# =========================================================
# PARTE 2 · csv.DictReader
# =========================================================

def leer_jugadores(nombre_fichero):
    """Devuelve una lista de diccionarios con los jugadores, con goles y partidos como int."""
    jugadores = []
    with open(nombre_fichero, "r", encoding="utf-8", newline="") as f:
        # TODO 4: crea un csv.DictReader(f) y recorre las filas. Cada fila es un diccionario
        # con las claves de la cabecera (todo str). Convierte fila['goles'] y fila['partidos']
        # a int y añade la fila a la lista.
        reader = csv.DictReader(f)
        for fila in reader:
            fila['goles'] = int(fila['goles'])
            fila['partidos'] = int(fila['partidos'])
            jugadores.append(fila)
    return jugadores


def nombres_columnas(nombre_fichero):
    """Devuelve la lista con los nombres de las columnas SIN leer ninguna fila."""
    with open(nombre_fichero, "r", encoding="utf-8", newline="") as f:
        # TODO 5: crea un DictReader y devuelve su atributo fieldnames.
        reader = csv.DictReader(f)
        return reader.fieldnames


def leer_sin_cabecera(nombre_fichero):
    """Lee jugadores_pv.csv: separado por ';' y SIN cabecera. Devuelve la lista de diccionarios."""
    with open(nombre_fichero, "r", encoding="utf-8", newline="") as f:
        # TODO 6: crea el DictReader indicando fieldnames=['nombre','equipo','posicion','goles','partidos']
        # (porque el fichero no tiene cabecera) y delimiter=';'. Devuelve list(reader).
        reader = csv.DictReader(f, fieldnames=['nombre','equipo','posicion','goles','partidos'], delimiter=';')
        return list(reader)


def filas_incompletas(nombre_fichero):
    """Lee jugadores_sucio.csv. Devuelve dos listas de NOMBRES de jugadores:
    (los que tienen datos de menos, los que tienen datos de más)."""
    faltan, sobran = [], []
    with open(nombre_fichero, "r", encoding="utf-8", newline="") as f:
        # TODO 7: DictReader con restval='?' (valor que se pone cuando faltan columnas) y
        # restkey='extra' (clave donde se guarda la lista de valores sobrantes).
        reader = csv.DictReader(f, restval='?', restkey='extra')
        for fila in reader:
        # TODO 8: por cada fila: si '?' está en fila.values(), añade fila['nombre'] a 'faltan';
        # si la fila tiene la clave 'extra', añade fila['nombre'] a 'sobran'.
            if '?' in fila.values():
                faltan.append(fila['nombre'])
            if 'extra' in fila:
                sobran.append(fila['nombre'])
    return faltan, sobran


# =========================================================
# PARTE 3 · csv.DictWriter
# =========================================================

def escribir_goleadores(jugadores, destino):
    """Escribe en 'destino' los 3 máximos goleadores (nombre y goles) de la lista de diccionarios."""
    mejores = sorted(jugadores, key=lambda j: j["goles"], reverse=True)[:3]
    with open(destino, "w", encoding="utf-8", newline="") as f:
        # TODO 9: DictWriter con fieldnames=['nombre','goles'] y extrasaction='ignore'
        # (los diccionarios traen más claves y no queremos que falle).
        # Escribe la cabecera con writeheader() y las filas con writerows(mejores).
        writer = csv.DictWriter(f, fieldnames=['nombre','goles'], extrasaction='ignore')
        writer.writeheader()
        writer.writerows(mejores)


def escribir_con_huecos(destino):
    """Escribe filas a las que les faltan claves, con ';' como separador y '-' en los huecos."""
    filas = [{"nombre": "Ana", "equipo": "Rayos"}, {"nombre": "Luis", "goles": 3}]
    with open(destino, "w", encoding="utf-8", newline="") as f:
        # TODO 10: DictWriter con fieldnames=['nombre','equipo','goles'], delimiter=';' y restval='-'
        # (valor que se escribe cuando a un diccionario le falta una clave).
        # Escribe la cabecera y las filas.
        writer = csv.DictWriter(f, fieldnames=['nombre','equipo','goles'], delimiter=';', restval='-')
        writer.writeheader()
        writer.writerows(filas)


def lanza_valueerror(fila):
    """Devuelve True si un DictWriter con fieldnames=['nombre'] (configuración por defecto)
    lanza ValueError al escribir el diccionario 'fila', y False si no."""
    with open("prueba.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre"])
        # TODO 11: intenta writer.writerow(fila) dentro de un try; si salta ValueError devuelve True;
        # si todo va bien, devuelve False.
        


# =========================================================
# PARTE 4 · Leer, modificar y reescribir (lo que haremos en el gestor)
# =========================================================

def anadir_columna(origen, destino):
    """Copia 'origen' a 'destino' añadiendo la columna 'goles_por_partido'."""
    with open(origen, "r", encoding="utf-8", newline="") as fr:
        reader = csv.DictReader(fr)
        filas = list(reader)
        # TODO 12: guarda en 'columnas' las columnas de entrada MÁS la nueva:
        # reader.fieldnames + ['goles_por_partido']   (fieldnames es una lista)
        ...
    # TODO 13: a cada diccionario de 'filas' añádele la clave 'goles_por_partido' con
    # round(int(goles) / int(partidos), 2).
    ...
    with open(destino, "w", encoding="utf-8", newline="") as fw:
        # TODO 14: DictWriter con fieldnames=columnas; escribe cabecera y todas las filas.
        ...


# =========================================================
# COMPROBACIONES
# =========================================================

if __name__ == "__main__":
    # Parte 1
    assert total_goles_reader(FICHERO) == 56
    resumen_writer(FICHERO, "resumen.csv")
    with open("resumen.csv", encoding="utf-8", newline="") as f:
        filas = list(csv.reader(f))
    assert filas[0] == ["nombre", "goles_por_partido"] and filas[1] == ["Ana Ruiz", "1.2"], filas[:2]
    assert filas[7][0] == "Soler, Eva"          # la coma entre comillas no rompe nada
    assert len(filas) == 11

    # Parte 2
    jug = leer_jugadores(FICHERO)
    assert len(jug) == 10 and jug[0] == {"nombre": "Ana Ruiz", "equipo": "Rayos", "posicion": "Delantera",
                                         "goles": 12, "partidos": 10}, jug[0]
    assert nombres_columnas(FICHERO) == ["nombre", "equipo", "posicion", "goles", "partidos"]
    pv = leer_sin_cabecera("jugadores_pv.csv")
    assert len(pv) == 3 and pv[0]["nombre"] == "Carla Mir" and pv[2]["goles"] == "0", pv
    assert filas_incompletas("jugadores_sucio.csv") == (["Luis Perez"], ["Marta Gil"])

    # Parte 3
    escribir_goleadores(jug, "goleadores.csv")
    with open("goleadores.csv", encoding="utf-8", newline="") as f:
        assert f.read() == "nombre,goles\r\nRaul Diaz,14\r\nAna Ruiz,12\r\nMarta Gil,9\r\n"
    escribir_con_huecos("huecos.csv")
    with open("huecos.csv", encoding="utf-8", newline="") as f:
        assert f.read() == "nombre;equipo;goles\r\nAna;Rayos;-\r\nLuis;-;3\r\n"
    assert lanza_valueerror({"nombre": "Ana", "equipo": "Rayos"}) is True
    assert lanza_valueerror({"nombre": "Ana"}) is False

    # Parte 4
    anadir_columna(FICHERO, "jugadores_ext.csv")
    ext = leer_jugadores("jugadores_ext.csv")
    assert nombres_columnas("jugadores_ext.csv")[-1] == "goles_por_partido"
    assert ext[0]["goles_por_partido"] == "1.2" and len(ext) == 10

    print("✅ Todo correcto")

    # ------------------------------------------------------
    # PARA PENSAR (contesta en comentarios):
    #  a) En la Parte 1, ¿qué pasaría si no saltaras la cabecera con next(reader)?
    #  b) ¿Qué pasa en leer_sin_cabecera si olvidas fieldnames? ¿Y si olvidas delimiter=';'?
    #  c) En escribir_goleadores, ¿qué ocurre si quitas extrasaction='ignore'?
    #  d) En escribir_con_huecos, quita restval='-'. ¿Qué se escribe en los huecos?
    #  e) Si el csv cambiara el orden de sus columnas, ¿qué funciones de las Partes 1 y 2 dejarían
    #     de funcionar? ¿Y las de DictReader?
    # ------------------------------------------------------
