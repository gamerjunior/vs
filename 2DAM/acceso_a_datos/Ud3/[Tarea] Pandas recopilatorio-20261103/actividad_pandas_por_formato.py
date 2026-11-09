"""
ACTIVIDAD PANDAS: UN TIPO DE FICHERO TRAS OTRO
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Repetimos, con pandas, lo que ya hicimos "a mano" con cada tipo de fichero. Son 5 partes
independientes y cortas. En todas el esquema es el mismo:

        fichero  --(pd.read_...)-->  DataFrame  --(operación)-->  resultado
        DataFrame  --(df.to_...)-->  fichero nuevo

    Parte 1 · CSV           jugadores.csv     (antes: csv.reader / DictReader)
    Parte 2 · Ancho fijo    comics.txt        (antes: seek/tell y cortes por posición)
    Parte 3 · JSON          liga.json         (antes: json.load y bucles)
    Parte 4 · XML           liga.xml          (antes: ElementTree)
    Parte 5 · HTML          calidad_aire.html (antes: BeautifulSoup)

Necesitas:  pip install pandas lxml

Lo básico de un DataFrame (df):
    df["goles"]                      una columna
    df["goles"].sum()  .mean()       suma, media (ignoran los huecos NaN)
    df[df["goles"] > 5]              filtrar filas por una condición
    df.loc[df["goles"].idxmax(), "nombre"]    valor de 'nombre' en la fila con más goles
    df.groupby("equipo")["goles"].sum()       agrupar y sumar
    serie.to_dict()  .tolist()       pasar a diccionario / lista

Completa cada TODO. Al final verás "OK Parte 1", "OK Parte 2"... hasta "Todo correcto".
"""

import json

import pandas as pd

# =========================================================
# PARTE 1 · CSV   (antes: csv.reader / DictReader)
# =========================================================


def leer_csv(ruta):
    """Devuelve un DataFrame con jugadores.csv."""
    # TODO 1: pd.read_csv(ruta). Fíjate: pandas se encarga solo de "Soler, Eva" (la coma entre comillas)
    # y de convertir goles y partidos a números.
    pd.read_csv(ruta)


def goleador(df):
    """Nombre del jugador con más goles."""
    # TODO 2: df["goles"].idxmax() devuelve la fila (el índice) del máximo.
    # Con df.loc[fila, "nombre"] obtienes el nombre de esa fila.
    ...


def media_goles_por_equipo(df):
    """Diccionario {equipo: media de goles}, redondeada a 2 decimales."""
    # TODO 3: df.groupby("equipo")["goles"].mean()  ->  .round(2)  ->  .to_dict()
    ...


def guardar_delanteras(df, destino):
    """Guarda en 'destino' (CSV) solo los jugadores cuya posicion es 'Delantera'."""
    # TODO 4: filtra con df[df["posicion"] == "Delantera"]  y escribe con .to_csv(destino, index=False).
    # (index=False evita que se escriba una columna extra con 0, 1, 2...)
    ...


# =========================================================
# PARTE 2 · ANCHO FIJO   (antes: seek/tell y cortes por posición)
# =========================================================

ANCHOS = [4, 18, 7, 5]          # codigo, titulo, precio, stock


def leer_comics(ruta):
    """DataFrame con columnas codigo, titulo, precio y stock leído de comics.txt."""
    # TODO 5: pd.read_fwf(ruta, widths=ANCHOS, names=["codigo", "titulo", "precio", "stock"], header=None,
    # dtype={"codigo": str})
    # header=None: el fichero no tiene cabecera. dtype={"codigo": str}: sin esto pandas
    # leería "0001" como el número 1 y perderías los ceros.
    ...


def valor_inventario(df):
    """Dinero total en almacén: suma de precio * stock, redondeado a 2 decimales."""
    # TODO 6: (df["precio"] * df["stock"]) multiplica columna con columna, fila a fila.
    # Después .sum() y round(..., 2).
    ...


def comics_a_csv(df, destino):
    """Convierte la tabla de ancho fijo en un CSV."""
    # TODO 7: df.to_csv(destino, index=False)
    ...


# =========================================================
# PARTE 3 · JSON   (antes: json.load y bucles anidados)
# =========================================================


def leer_jugadores_json(ruta):
    """DataFrame con UNA FILA POR JUGADOR de liga.json. El nombre del equipo queda en 'equipo_nombre'."""
    # TODO 8: abre el fichero (utf-8) y carga con json.load. Después:
    # pd.json_normalize(datos["equipos"], record_path="jugadores", meta=["nombre"], meta_prefix="equipo_")
    # record_path = la lista que se convierte en filas.  meta = campos del equipo que se copian a cada fila.
    # meta_prefix evita que 'nombre' (del equipo) choque con 'nombre' (del jugador).
    ...


def goles_por_equipo(df):
    """Diccionario {equipo: goles totales}."""
    # TODO 9: df.groupby("equipo_nombre")["goles"].sum().to_dict()
    ...


def guardar_json(df, destino):
    """Guarda el DataFrame como una lista de objetos JSON, con acentos y sangría de 2."""
    # TODO 10: df.to_json(destino, orient="records", indent=2, force_ascii=False)
    ...


# =========================================================
# PARTE 4 · XML   (antes: ElementTree)
# =========================================================


def leer_jugadores_xml(ruta):
    """DataFrame con los <jugador> de liga.xml. Los atributos (dorsal, posicion, capitan) y los hijos
    (nombre, goles, partidos) se convierten en columnas."""
    # TODO 11: pd.read_xml(ruta, xpath=".//jugador")
    # xpath=".//jugador" es la misma ruta que usaste con findall('.//jugador').
    ...


def capitanes(df):
    """Lista con los nombres de los jugadores que tienen el atributo capitan (el resto queda en NaN)."""
    # TODO 12: df["capitan"].notna() es True donde hay valor. Filtra con df[df["capitan"].notna()]
    # y saca la columna "nombre" con .tolist().
    ...


def guardar_xml(df, destino):
    """Escribe el DataFrame como XML: raíz <jugadores> y un <jugador> por fila."""
    # TODO 13: df.to_xml(destino, index=False, root_name="jugadores", row_name="jugador")
    ...


# =========================================================
# PARTE 5 · HTML   (antes: BeautifulSoup)
# =========================================================


def leer_mediciones(ruta):
    """DataFrame con la tabla de calidad_aire.html. El '-' debe contar como dato que falta (NaN)."""
    # TODO 14: pd.read_html(ruta, na_values=["-"]) devuelve una LISTA con un DataFrame por cada <table>.
    # Devuelve el primero ([0]).
    ...


def media_pm10(df):
    """Media de la columna PM10, redondeada a 2 decimales."""
    # TODO 15: df["PM10"].mean() ignora los NaN automáticamente. Compáralo con la actividad de bs4:
    # allí tuviste que filtrar los None a mano. Redondea con round(..., 2).
    ...


def estaciones_en_alerta(df):
    """Códigos de estación (sin repetir, ordenados) con alguna medición de PM10 mayor que 50."""
    # TODO 16: df[df["PM10"] > 50]["Estación"] -> .unique() -> sorted(...)
    ...


def guardar_mediciones_xml(df, destino):
    """Guarda las mediciones como XML: raíz <calidad_aire> y un <medicion> por fila."""
    # TODO 17: df.to_xml(destino, index=False, root_name="calidad_aire", row_name="medicion")
    ...


# =========================================================
# COMPROBACIONES
# =========================================================

if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    # ---- Parte 1
    jug = leer_csv("jugadores.csv")
    assert list(jug.columns) == ["nombre", "equipo", "posicion", "goles", "partidos"] and len(jug) == 10
    assert "Soler, Eva" in jug["nombre"].tolist()
    assert goleador(jug) == "Raul Diaz"
    assert media_goles_por_equipo(jug) == {"Halcones": 5.67, "Lobos": 6.33, "Rayos": 5.0}, media_goles_por_equipo(jug)
    guardar_delanteras(jug, "delanteras.csv")
    lineas = open("delanteras.csv", encoding="utf-8").read().splitlines()
    assert lineas[0] == "nombre,equipo,posicion,goles,partidos" and len(lineas) == 4, lineas
    print("OK Parte 1 · CSV")

    # ---- Parte 2
    com = leer_comics("comics.txt")
    assert list(com.columns) == ["codigo", "titulo", "precio", "stock"] and len(com) == 6
    assert com.loc[0, "codigo"] == "0001" and com.loc[3, "titulo"] == "Superlopez"
    assert valor_inventario(com) == 309.8, valor_inventario(com)
    comics_a_csv(com, "comics.csv")
    lineas = open("comics.csv", encoding="utf-8").read().splitlines()
    assert lineas[0] == "codigo,titulo,precio,stock" and lineas[1] == "0001,Tintin,12.5,3", lineas[:2]
    print("OK Parte 2 · Ancho fijo")

    # ---- Parte 3
    pj = leer_jugadores_json("liga.json")
    assert len(pj) == 8 and "equipo_nombre" in pj.columns and "nombre" in pj.columns
    assert goles_por_equipo(pj) == {"Alaquàs Club": 17, "Paterna Atlético": 10, "Torrent CF": 16}, goles_por_equipo(pj)
    guardar_json(pj, "jugadores_liga.json")
    leido = json.load(open("jugadores_liga.json", encoding="utf-8"))
    assert isinstance(leido, list) and len(leido) == 8 and leido[2]["nombre"] == "Lucía Ñíguez"
    print("OK Parte 3 · JSON")

    # ---- Parte 4
    px = leer_jugadores_xml("liga.xml")
    assert len(px) == 10 and {"dorsal", "posicion", "capitan", "nombre", "goles", "partidos"} <= set(px.columns)
    assert capitanes(px) == ["Ana Ruiz", "Marta Gil", "Raul Diaz"], capitanes(px)
    guardar_xml(px, "jugadores_liga.xml")
    raiz = ET.parse("jugadores_liga.xml").getroot()
    assert raiz.tag == "jugadores" and len(raiz.findall("jugador")) == 10
    print("OK Parte 4 · XML")

    # ---- Parte 5
    med = leer_mediciones("calidad_aire.html")
    assert list(med.columns) == ["Estación", "Fecha", "Hora", "PM10", "NO2", "O3"] and len(med) == 8
    assert med["PM10"].isna().sum() == 1                    # el '-' ha pasado a NaN
    assert media_pm10(med) == 38.27, media_pm10(med)
    assert estaciones_en_alerta(med) == ["P01", "T02"], estaciones_en_alerta(med)
    guardar_mediciones_xml(med, "calidad_aire_pandas.xml")
    raiz = ET.parse("calidad_aire_pandas.xml").getroot()
    assert raiz.tag == "calidad_aire" and len(raiz.findall("medicion")) == 8
    print("OK Parte 5 · HTML")

    print("OK Todo correcto")

    # ------------------------------------------------------
    # PARA PENSAR:
    #  a) ¿Por qué hay que poner index=False en to_csv?
    #     -> Sin él se escribe una columna extra con 0, 1, 2... y al releer aparece 'Unnamed: 0'.
    #  b) En la parte 2, ¿qué pasa si quitas dtype={"codigo": str}?
    #     -> '0001' se lee como el número 1 y pierdes los ceros iniciales.
    #  c) En la parte 3, ¿por qué no sale Picanya Unió en goles_por_equipo?
    #     -> groupby solo crea grupos con filas; ese equipo no tiene jugadores en liga.json.
    #        (En la actividad de JSON, a mano, sí salía con 0: lo habías programado tú.)
    #  d) En la parte 3, ¿qué pasa si quitas meta_prefix?
    #     -> ValueError: Conflicting metadata name nombre, need distinguishing prefix.
    #  e) En la parte 5, ¿por qué media_pm10 es tan corto comparado con la actividad de bs4?
    #     -> mean() ignora los NaN, y na_values=['-'] ya convirtió los '-' en NaN al leer.
    #  f) ¿En qué parte compensa más pandas? ¿Y cuándo preferirías la librería de siempre?
    #     -> En HTML y ancho fijo la lectura es de una línea. Para cambiar un solo dato de un
    #        fichero pequeño, csv/json/ElementTree bastan (pandas es una librería pesada).
    # ------------------------------------------------------
