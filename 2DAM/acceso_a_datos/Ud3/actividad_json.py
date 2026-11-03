"""
ACTIVIDAD JSON: LEER, NAVEGAR, MODIFICAR Y GUARDAR
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Trabajamos con liga.json (una liga con equipos y, dentro de cada equipo, sus jugadores).

Recuerda:
    json.load(f)        -> lee un FICHERO y devuelve dict/list...
    json.loads(texto)   -> lee una CADENA (la 's' es de string)
    json.dump(obj, f, indent=2, ensure_ascii=False)   -> escribe en un FICHERO
    json.dumps(obj)     -> devuelve una CADENA
    JSON  ->  Python:  objeto{} -> dict | array[] -> list | string -> str | number -> int/float
                       true/false -> True/False | null -> None

Completa cada TODO. Al final verás "Todo correcto".
"""

import csv
import json
from dataclasses import asdict, dataclass
from datetime import date

FICHERO = "liga.json"
FICHERO_ROTO = "liga_roto.json"


# =========================================================
# PARTE 1 · Leer y navegar
# =========================================================

def leer_json(ruta):
    """Devuelve el contenido del fichero JSON como estructura de Python."""
    # TODO 1: abre el fichero (modo 'r', encoding='utf-8') y devuelve json.load(f).
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def numero_equipos(datos):
    """Cuántos equipos hay."""
    # TODO 2: datos['equipos'] es una lista; devuelve su longitud.
    return len(datos["equipos"])


def nombres_jugadores(datos, nombre_equipo):
    """Lista con los nombres de los jugadores del equipo indicado ([] si el equipo no existe)."""
    # TODO 3: recorre datos['equipos']; cuando equipo['nombre'] coincida, devuelve
    # [j['nombre'] for j in equipo['jugadores']]. Si no lo encuentras, devuelve [].
    for equipo in datos["equipos"]:
        if equipo["nombre"] == nombre_equipo:
            return [j["nombre"] for j in equipo["jugadores"]]
    return []


def goleador(datos):
    """Nombre del jugador con más goles de TODA la liga (si hay empate, el primero)."""
    # TODO 4: recorre todos los jugadores de todos los equipos y quédate con el de más goles.
    mejor_jugador = None
    for equipo in datos["equipos"]:
        for jugador in equipo["jugadores"]:
            if mejor_jugador is None or jugador["goles"] > mejor_jugador["goles"]:
                mejor_jugador = jugador
    return mejor_jugador["nombre"] if mejor_jugador is not None else None


def goles_por_equipo(datos):
    """Diccionario {nombre_equipo: total de goles de sus jugadores}. Un equipo sin jugadores suma 0."""
    # TODO 5: construye el diccionario con sum(...) sobre los goles de cada equipo.
    return {
        equipo["nombre"]: sum(j["goles"] for j in equipo["jugadores"])
        for equipo in datos["equipos"]
    }


def equipos_sin_capitan(datos):
    """Nombres de los equipos cuyo capitán es null (None en Python)."""
    # TODO 6: en JSON, null llega como None. Usa  'is None'.
    return [
        equipo["nombre"]
        for equipo in datos["equipos"]
        if equipo["capitan"] is None
    ]


def nota_media(datos):
    """Nota media de todos los jugadores que TIENEN nota (la nota puede ser null). Redondea a 2 decimales."""
    # TODO 7: reúne las notas que no sean None y calcula la media.
    notas = [
        jugador["nota"]
        for equipo in datos["equipos"]
        for jugador in equipo["jugadores"]
        if jugador["nota"] is not None
    ]
    return round(sum(notas) / len(notas), 2) if notas else 0


# =========================================================
# PARTE 2 · Modificar y guardar
# =========================================================

def anadir_jugador(datos, nombre_equipo, jugador):
    """Añade el diccionario 'jugador' a los jugadores del equipo. Devuelve True si el equipo existe."""
    # TODO 8: busca el equipo y haz equipo['jugadores'].append(jugador). Si no existe, False.
    for equipo in datos["equipos"]:
        if equipo["nombre"] == nombre_equipo:
            equipo["jugadores"].append(jugador)
            return True
    return False


def guardar_json(ruta, datos):
    """Escribe 'datos' en 'ruta' con sangría de 2 espacios y SIN escapar los acentos."""
    # TODO 9: abre en 'w' con encoding='utf-8' y usa json.dump(datos, f, indent=2, ensure_ascii=False).
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def a_cadena_compacta(obj):
    """Cadena JSON en una sola línea, sin espacios de más, con acentos tal cual."""
    # TODO 10: json.dumps(obj, ensure_ascii=False, separators=(',', ':')).
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


# =========================================================
# PARTE 3 · Objetos propios, fechas y errores
# =========================================================

@dataclass
class Jugador:
    id: int
    nombre: str
    posicion: str
    goles: int
    activo: bool
    nota: float | None
    fichaje: date | None = None


def jugador_a_json(jugador):
    """Convierte un Jugador en una cadena JSON. La fecha (date) debe salir como 'AAAA-MM-DD'."""
    # TODO 11: json.dumps(...) no sabe serializar ni la dataclass ni el date.
    # Pasa el objeto a diccionario con asdict(jugador) y usa el parámetro default=str
    # (se llama para todo lo que no sepa convertir). Añade ensure_ascii=False.
    return json.dumps(asdict(jugador), default=str, ensure_ascii=False)


def leer_seguro(ruta):
    """Como leer_json, pero devuelve None si el fichero no existe o NO es un JSON válido."""
    # TODO 12: captura FileNotFoundError y json.JSONDecodeError (en el mismo except, como tupla).
    try:
        return leer_json(ruta)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def a_csv(datos, destino):
    """Aplana la liga a un CSV con columnas: equipo, id, nombre, posicion, goles (una fila por jugador)."""
    # TODO 13: con csv.DictWriter (fieldnames=['equipo','id','nombre','posicion','goles'], extrasaction='ignore'),
    # escribe la cabecera y una fila por jugador (el diccionario del jugador más la clave 'equipo').
    # Abre con newline='' y encoding='utf-8'.
    fieldnames = ["equipo", "id", "nombre", "posicion", "goles"]
    with open(destino, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(
            f, fieldnames=fieldnames, extrasaction="ignore"
        )
        escritor.writeheader()
        for equipo in datos["equipos"]:
            for jugador in equipo["jugadores"]:
                fila = dict(jugador)
                fila["equipo"] = equipo["nombre"]
                escritor.writerow(fila)


# =========================================================
# COMPROBACIONES
# =========================================================

if __name__ == "__main__":
    datos = leer_json(FICHERO)
    assert isinstance(datos, dict) and datos["liga"] == "Liga Escolar de Torrent"
    assert numero_equipos(datos) == 4
    assert nombres_jugadores(datos, "Paterna Atlético") == ["Carlos Mora", "Noelia Gil"]
    assert nombres_jugadores(datos, "Inventado FC") == []
    assert goleador(datos) == "Marta Pérez"                       # 12 goles, y gana al empate de Àngela
    assert goles_por_equipo(datos) == {"Torrent CF": 16, "Paterna Atlético": 10,
                                       "Alaquàs Club": 17, "Picanya Unió": 0}, goles_por_equipo(datos)
    assert equipos_sin_capitan(datos) == ["Paterna Atlético"]
    assert nota_media(datos) == 7.75, nota_media(datos)

    nuevo = {"id": 9, "nombre": "Aitana Boix", "posicion": "defensa", "goles": 2, "activo": True, "nota": None}
    assert anadir_jugador(datos, "Picanya Unió", nuevo) is True
    assert anadir_jugador(datos, "Inventado FC", nuevo) is False
    assert goles_por_equipo(datos)["Picanya Unió"] == 2
    guardar_json("liga_nueva.json", datos)
    texto = open("liga_nueva.json", encoding="utf-8").read()
    assert "Ñíguez" in texto and "\\u" not in texto and texto.startswith('{\n  "liga"')
    assert leer_json("liga_nueva.json") == datos                  # ida y vuelta sin pérdidas
    assert a_cadena_compacta({"a": [1, 2], "n": "Peña"}) == '{"a":[1,2],"n":"Peña"}'

    j = Jugador(10, "Eva Ríos", "portera", 0, True, None, date(2026, 10, 28))
    assert jugador_a_json(j) == ('{"id": 10, "nombre": "Eva Ríos", "posicion": "portera", "goles": 0, '
                                 '"activo": true, "nota": null, "fichaje": "2026-10-28"}'), jugador_a_json(j)
    assert leer_seguro(FICHERO) is not None
    assert leer_seguro("no_existe.json") is None
    assert leer_seguro(FICHERO_ROTO) is None

    a_csv(leer_json(FICHERO), "liga_jugadores.csv")
    lineas = open("liga_jugadores.csv", encoding="utf-8").read().splitlines()
    assert lineas[0] == "equipo,id,nombre,posicion,goles" and len(lineas) == 9, len(lineas)
    assert lineas[1] == "Torrent CF,1,Marta Pérez,delantera,12"

    print("Todo correcto")

    # ------------------------------------------------------
    # PARA PENSAR (con respuestas):
    #  a) ¿Qué diferencia hay entre json.load y json.loads? ¿Y entre dump y dumps?
    #       load/dump trabajan con un FICHERO; loads/dumps con una CADENA ('s' = string).
    #  b) json.dumps({1: 'a'}) y luego json.loads(...): ¿qué clave recuperas?
    #       "1" (str): en JSON las claves SIEMPRE son cadenas. La ida y vuelta no es idéntica.
    #  c) ¿Qué pasa con una tupla (1, 2) al hacer dumps + loads?
    #       vuelve como lista [1, 2]: JSON no tiene tuplas.
    #  d) ¿Por qué falla json.dumps(date(2026, 1, 1))? ¿Qué hacen asdict y default=str?
    #       TypeError: Object of type date is not JSON serializable. JSON solo conoce dict, list, str, número, bool y None. asdict convierte la dataclass a dict; default=str se llama para lo que no sabe convertir (la fecha sale como 'AAAA-MM-DD').
    #  e) ¿Por qué un JSON con coma final {"a": 1,} da error y en Python el diccionario no?
    #       El formato JSON es estricto (comillas dobles, sin comas finales, sin comentarios). Lanza json.JSONDecodeError, que es subclase de ValueError.
    #  f) ¿Qué ventaja tiene JSON frente a CSV para esta liga? ¿Y qué desventaja?
    #       Guarda jerarquía (equipos con jugadores dentro) y tipos (número, bool, null) sin aplanar. A cambio, para tablas planas (CSV/pandas) hay que aplanar, como en a_csv.
    # ------------------------------------------------------
