"""
🏟️ ACTIVIDAD XML: LA LIGA CON xml.etree.ElementTree
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Trabajamos con liga.xml.

Ideas clave de ElementTree:
    - Un Element tiene:   .tag (nombre de la etiqueta)   .attrib (dict de atributos)
                          .text (texto interior)         y HIJOS (se recorre con for)
    - elem.find('x')            -> primer hijo 'x' (o None si no hay)
    - elem.findall('x')         -> lista con TODOS los hijos 'x'
    - elem.get('a', defecto)    -> valor del atributo 'a' (o el defecto si no existe)
    - Rutas:  './equipo/jugador'   './/jugador'   './/jugador[@capitan]'   "./equipo[@nombre='Rayos']"
    - TODO lo que se guarda (texto y atributos) debe ser str. Todo lo que se lee llega como str.

Completa cada TODO. Al final verás "Todo correcto".
"""

import csv
import xml.etree.ElementTree as ET

FICHERO = "liga.xml"


# =========================================================
# PARTE 1 · Leer: parse, tag, attrib, text
# =========================================================

def leer_liga(nombre_fichero):
    """Devuelve el elemento raíz (<liga>) del fichero."""
    # TODO 1: ET.parse(nombre_fichero) devuelve un ElementTree; con .getroot() obtienes la raíz.
    raiz =ET.parse(nombre_fichero).getroot()
    return raiz

def nombre_liga(raiz):
    """Devuelve el valor del atributo 'nombre' de la raíz."""
    # TODO 2: los atributos están en el diccionario raiz.attrib.
    return raiz.attrib["nombre"]


def nombres_equipos(raiz):
    """Lista con el atributo 'nombre' de cada <equipo>, en orden."""
    # TODO 3: recorre los hijos <equipo> con raiz.findall('equipo') y recoge equipo.attrib['nombre'].
    return [equipo.attrib['nombre'] for equipo in raiz.findall('equipo')]


# =========================================================
# PARTE 2 · Buscar con find / findall / rutas
# =========================================================

def numero_jugadores(raiz):
    """Cuántos <jugador> hay en toda la liga."""
    # TODO 4: findall con la ruta './equipo/jugador' (o './/jugador') y len().
    return len(raiz.findall("./equipo/jugador"))

def goles_equipo(raiz, nombre_equipo):
    """Suma los goles de los jugadores del equipo indicado."""
    total = 0
    # TODO 5: findall con un predicado sobre el atributo:
    # f"./equipo[@nombre='{nombre_equipo}']/jugador"
    # Por cada jugador, suma int(jugador.find('goles').text)   (el texto es un str).
    for jugador in raiz.findall(f"./equipo[@nombre='{nombre_equipo}']/jugador"):
        total += int(jugador.find('goles').text)
    return total


def capitanes(raiz):
    """Lista con los nombres de los jugadores que tienen el atributo 'capitan'."""
    # TODO 6: findall('.//jugador[@capitan]') selecciona solo los que tienen ese atributo.
    # Devuelve la lista de jugador.find('nombre').text
    captinaes = []
    for jugador in raiz.findall(".//jugador[@capitan]"):
        captinaes.append(jugador.find("nombre").text)
    return captinaes

def es_capitan(jugador):
    """True si el <jugador> tiene capitan='si'. Los que no tienen el atributo NO son capitanes."""
    # TODO 7: usa jugador.get('capitan', 'no') (el segundo argumento es el valor por defecto)
    # y compáralo con 'si'.  (jugador.attrib['capitan'] daría KeyError en los demás.)
    if(jugador.get("capitan","no") == "si"):
        return True
    else:
        return False
    


def jugador_por_nombre(raiz, nombre):
    """Devuelve el elemento <jugador> con ese nombre, o None si no existe."""
    # TODO 8: recorre './/jugador' y compara j.find('nombre').text con 'nombre'.
    for jugador in raiz.findall(".//jugador"):
        if jugador.find("nombre").text == nombre:
            return jugador
        else:
            return None


# =========================================================
# PARTE 3 · Modificar el árbol
# =========================================================

def subir_goles(raiz, nombre, cuantos):
    """Suma 'cuantos' goles al jugador. Devuelve True si lo encontró."""
    jugador = jugador_por_nombre(raiz, nombre)
    if jugador is None:
        return False
    # TODO 9: el texto de <goles> es un str: conviértelo a int, súmale 'cuantos' y vuelve a
    # asignarlo como str:  elemento.text = str(...)
    num = int(jugador.find("goles").text)
    num += cuantos
    jugador.find("goles").text = str(num)
    return True


def fichar(raiz, nombre_equipo, nombre, posicion, goles=0, partidos=0):
    """Añade un <jugador> al final del equipo indicado, con sus tres hijos."""
    equipo = raiz.find(f"./equipo[@nombre='{nombre_equipo}']")
    # TODO 10: crea el jugador con ET.SubElement(equipo, 'jugador', posicion=posicion) y, dentro
    # de él, los hijos 'nombre', 'goles' y 'partidos' con ET.SubElement(...).
    # Asigna el texto de cada uno (¡siempre str!: str(goles), str(partidos)).
    jugador = ET.SubElement(equipo,"jugador", posicion=posicion)
    nombrelement = ET.SubElement(jugador, "nombre")
    golelement = ET.SubElement(jugador, "goles")
    partelement = ET.SubElement(jugador, "partidos")
    nombrelement.text = nombre
    golelement.text = str(goles)
    partelement.text = str(partidos)

def dar_de_baja(raiz, nombre):
    """Elimina del árbol al jugador con ese nombre. Devuelve True si lo encontró."""
    # TODO 11: ElementTree NO sabe cuál es el padre de un elemento. Hay que recorrer los <equipo>
    # y, dentro de cada uno, sus jugadores; al encontrar el nombre, borra con
    # equipo.remove(jugador).
    for equipo in raiz.findall("equipo"):
        for jugador in equipo.findall("jugador"):
            if jugador.find(nombre).text == nombre:
                equipo.remove(jugador)


# =========================================================
# PARTE 4 · Guardar y construir XML desde cero
# =========================================================

def guardar(raiz, destino):
    """Guarda el árbol en 'destino', bien sangrado y con la cabecera <?xml ...?>."""
    # TODO 12: ET.indent(raiz) sangra el árbol (para que sea legible);
    # ET.ElementTree(raiz).write(destino, encoding='utf-8', xml_declaration=True)
    ET.indent(raiz)
    ET.ElementTree(raiz).write(destino, encoding='utf-8', xml_declaration=True)


def csv_a_xml(fichero_csv, destino):
    """Lee jugadores.csv con DictReader y genera un XML agrupado por equipos."""
    raiz = ET.Element("liga", nombre="Liga Escolar")
    equipos = {}                      # nombre del equipo -> su Element <equipo>
    with open(fichero_csv, "r", encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            # TODO 13: si el equipo de la fila aún no está en 'equipos', crea su <equipo> con
            # ET.SubElement(raiz, 'equipo', nombre=fila['equipo']) y guárdalo en el diccionario.
            if fila['equipo'] not in equipos:
                equipos[fila['equipo']] = ET.SubElement(
                    raiz, 'equipo', nombre=fila['equipo']
                )
            # TODO 14: crea el <jugador> dentro de su equipo con el atributo posicion=fila['posicion'];
            # sus hijos <nombre>, <goles> y <partidos> con el texto correspondiente del csv.
            jugador = ET.SubElement(
                equipos[fila['equipo']],
                'jugador',
                posicion=fila['posicion']
            )
            ET.SubElement(jugador, 'nombre').text = fila['nombre']
            ET.SubElement(jugador, 'goles').text = fila['goles']
            ET.SubElement(jugador, 'partidos').text = fila['partidos']
    guardar(raiz, destino)


# =========================================================
# COMPROBACIONES
# =========================================================

if __name__ == "__main__":
    raiz = leer_liga(FICHERO)
    assert raiz.tag == "liga"
    assert nombre_liga(raiz) == "Liga Escolar"
    assert nombres_equipos(raiz) == ["Rayos", "Halcones", "Lobos"]

    assert numero_jugadores(raiz) == 10
    assert goles_equipo(raiz, "Rayos") == 20 and goles_equipo(raiz, "Lobos") == 19
    assert capitanes(raiz) == ["Ana Ruiz", "Marta Gil", "Raul Diaz"]
    assert es_capitan(jugador_por_nombre(raiz, "Ana Ruiz")) is True
    assert es_capitan(jugador_por_nombre(raiz, "Luis Perez")) is False
    assert jugador_por_nombre(raiz, "Nadie") is None
    assert jugador_por_nombre(raiz, "Soler, Eva").attrib["dorsal"] == "4"

    assert subir_goles(raiz, "Pau Ferrer", 3) is True
    assert jugador_por_nombre(raiz, "Pau Ferrer").find("goles").text == "5"
    assert subir_goles(raiz, "Nadie", 1) is False

    fichar(raiz, "Lobos", "Carla Mir", "Delantera", goles=8, partidos=10)
    assert numero_jugadores(raiz) == 11 and goles_equipo(raiz, "Lobos") == 27
    assert dar_de_baja(raiz, "Luis Perez") is True and dar_de_baja(raiz, "Luis Perez") is False
    assert numero_jugadores(raiz) == 10

    guardar(raiz, "liga_nueva.xml")
    otra = leer_liga("liga_nueva.xml")                  # se puede volver a leer
    assert numero_jugadores(otra) == 10 and nombre_liga(otra) == "Liga Escolar"
    with open("liga_nueva.xml", encoding="utf-8") as f:
        assert f.readline().startswith("<?xml version='1.0' encoding='utf-8'?>")

    csv_a_xml("jugadores.csv", "liga_desde_csv.xml")
    d = leer_liga("liga_desde_csv.xml")
    assert nombres_equipos(d) == ["Rayos", "Halcones", "Lobos"]
    assert numero_jugadores(d) == 10 and goles_equipo(d, "Halcones") == 17

    print("Todo correcto")

    # ------------------------------------------------------
    # PARA PENSAR (contesta en comentarios):
    #  a) ¿Qué devuelve raiz.find('equipo/entrenador') si no existe? ¿Y qué pasa si encadenas .text?
    #  b) Prueba ET.SubElement(raiz, 'equipo', id=1) y luego guardar(raiz, 'x.xml').
    #     ¿Falla al crear el elemento o al guardar? ¿Por qué hay que usar str(1)?
    #  c) Mira liga_desde_csv.xml: ¿qué pasa con el nombre "Soler, Eva"? ¿Hace falta entrecomillarlo
    #     como en el csv?
    #  d) Abre liga_nueva.xml y quita la llamada a ET.indent. ¿Cómo queda el fichero? ¿Sigue siendo válido?
    #  e) ¿Por qué 'if raiz.find(\"x\"):' NO es la forma correcta de saber si existe un elemento?
    #     (Pista: prueba con un elemento que existe pero no tiene hijos.)
    # ------------------------------------------------------
