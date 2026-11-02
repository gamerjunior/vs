"""
ACTIVIDAD HTML: DE UNA PÁGINA WEB A UN XML
Acceso a Datos · UD3 - Persistencia de datos en ficheros

Vamos a "scrapear"una página HTML y a guardar los datos en XML.
Hoy trabajamos con una copia LOCAL de la página: calidad_aire.html (datos ficticios).
Así el ejercicio funciona siempre, sin conexión y sin molestar a ningún servidor.

Herramientas:
    from bs4 import BeautifulSoup        # pip install beautifulsoup4
    soup = BeautifulSoup(texto_html, "html.parser")
    soup.find("h1")                      -> primer elemento <h1> (o None)
    soup.find_all("div", class_="x")     -> lista de <div class="x">
    soup.find(id="licencia")             -> elemento con ese id
    soup.select("table#mediciones tr")   -> selectores CSS (lista)
    elemento.get_text(strip=True)        -> texto sin espacios sobrantes
    elemento["href"]  /  elemento.get("href")   -> atributo
    elemento.find_all("td")              -> descendientes

Y para escribir el XML, lo que vimos con xml.etree.ElementTree.

Completa cada TODO. Al final verás "Todo correcto".
"""

import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

FICHERO = "calidad_aire.html"


# ---------------------------------------------------------
# Esta función te la damos hecha: así se descargaría una página real.
# Hoy NO la usamos. Fíjate en las buenas prácticas: User-Agent, timeout, código de estado.
# ---------------------------------------------------------
def descargar(url):
    import requests
    cabeceras = {"User-Agent": "practicas-2DAM (aula; contacto: profesor@centro.example)"}
    respuesta = requests.get(url, headers=cabeceras, timeout=10)
    respuesta.raise_for_status()          # lanza excepción si el código no es 2xx
    return respuesta.text


# =========================================================
# PARTE 1 · Abrir y buscar elementos
# =========================================================

def abrir_html(nombre_fichero):
    """Devuelve el objeto BeautifulSoup de la página."""
    # TODO 1: abre el fichero (encoding='utf-8'), lee TODO el texto con read() y devuelve beatutifulsoup(texto, "html.parser").
    with open(nombre_fichero, "r", encoding="utf-8") as f:
        texto = f.read()
    return BeautifulSoup(texto, "html.parser")


def titulo_pagina(soup):
    """Texto de la etiqueta <title>."""
    # TODO 2: soup.title es la etiqueta <title>; usa get_text(strip=True).
    # También podrías hacerlo como en el ejemplo con soup.title.text.
    return soup.title.get_text(strip=True)


def licencia(soup):
    """Texto del elemento con id='licencia'."""
    # TODO 3: Obtén el texto del elemento con el selector CSS #licencia.
    soup_licncia=soup.find(id="licencia") #metodo propio
    #soup_licencia = soup.select_one("#licencia") metodo de la ia
    
    

# =========================================================
# PARTE 2 · Extraer listas de elementos
# =========================================================

def estaciones(soup):
    """Lista de diccionarios {'codigo', 'nombre', 'municipio', 'enlace'} de cada <div class='estacion'>."""
    resultado = []
    # TODO 4: recorre todos los div de clase estación y devuelve un diccionario con:
    #   - código
    #   - nombre
    #   - municipio
    #   - enlace
    for div in soup.find("div", class_="estacion"):
        codigo = div["data-codigo"]
        nombre = div.find("h2").get_text(strip=True)
        municipio = div.find("p").get_text(strip=True)
        enlace = div.find("a")["href"]
        resultado.append({"codigo": codigo, "nombre": nombre, "municipio": municipio, "enlace": enlace})
    return resultado


def a_numero(texto):
    """Convierte '23.5' en 23.5 y '-' (dato que falta) en None."""
    # TODO 5: si el texto es '-', devuelve None; si no, float(texto).
    if texto == "-":
        return None
    else:
        return float(texto)


def leer_mediciones(soup):
    """Lista de diccionarios, uno por fila de la tabla 'mediciones'.
    Claves: estacion, fecha, hora, pm10, no2, o3 (los tres últimos float o None)."""
    mediciones = []
    # TODO 6: recorre las filas del cuerpo de la tabla con soup.select('table#mediciones tbody tr').
    # De cada fila saca el texto de sus <td> en una lista:
    # celdas = [td.get_text(strip=True) for td in fila.find_all('td')]
    # y construye el diccionario (usa a_numero para pm10, no2 y o3).
    
    for fila in soup.select('table#mediciones tbody tr'):
        celdas = [td.get_text(strip=True) for td in fila.find_all('td')]
        estacion = celdas[0]
        fecha = celdas[1]
        hora = celdas[2]
        pm10 = a_numero(celdas[3])
        no2 = a_numero(celdas[4])
        o3 = a_numero(celdas[5])
        mediciones.append({"estacion": estacion, "fecha": fecha, "hora": hora, "pm10": pm10, "no2": no2, "o3": o3})
    return mediciones


def estaciones_en_alerta(soup):
    """Códigos de estación (sin repetir y ordenados) de las filas con class='alerta'."""
    # TODO 7: soup.select('tr.alerta') selecciona las filas con esa clase. De cada una, el texto de
    # su primer <td>. Quita repetidos con set() y ordena con sorted().
    codigos = [
        fila.find("td").get_text(strip=True)
        for fila in soup.select("tr.alerta")
    ]
    return sorted(set(codigos))


def media_pm10(mediciones):
    """Media de PM10 ignorando los datos que faltan (None)."""
    # TODO 8: crea una lista con los pm10 que NO sean None y calcula la media (redondeada a 2 decimales).
    pm10list = []
    for pm10 in mediciones["pm10"]:
        if pm10 != "-":
            pm10list.append(pm10)

    for i in range(len(pm10list)):
        pm10list[i] = float(pm10list[i])
    media = sum(pm10list) / len(pm10list)
    return round(media, 2)
        


# =========================================================
# PARTE 3 · Generar el XML
# =========================================================

def a_xml(lista_estaciones, mediciones, texto_licencia, destino):
    """Escribe en 'destino' un XML con esta forma:

    <calidad_aire licencia="...">
      <estaciones>
        <estacion codigo="T01" municipio="Torrent">Torrent Centro</estacion> ...
      </estaciones>
      <mediciones>
        <medicion estacion="T01" fecha="2026-10-20" hora="08:00">
          <pm10>23.5</pm10><no2>41.0</no2><o3>35.2</o3>
        </medicion> ...
      </mediciones>
    </calidad_aire>

    Si un valor falta (None), NO se crea su elemento."""
    # TODO 9: crea la raíz con ET.Element('calidad_aire', licencia=texto_licencia) y el hijo <estaciones>
    # (ET.SubElement). Por cada estación crea un <estacion codigo=... municipio=...> con
    # el nombre como texto.
    raiz = ET.element("calidad_aire", licencia=texto_licencia)
    
    
    # TODO 10: crea el hijo <mediciones>. Por cada medición crea un <medicion estacion= fecha= hora=>
    # y, dentro, un elemento por cada valor (pm10, no2, o3) que NO sea None.
    # Recuerda: el texto debe ser str -> str(valor).
    ...
    # TODO 11: ET.indent(raiz) y guarda con ET.ElementTree(raiz).write(destino, encoding='utf-8',
    # xml_declaration=True)
    ...


def comprobar_xml(destino):
    """Vuelve a leer el XML generado y devuelve (nº de <medicion>, nº de elementos <pm10>)."""
    # TODO 12: lee el fichero con ET.parse(destino).getroot() y cuenta con findall:
    # './mediciones/medicion'  y  './/pm10'
    ...


# =========================================================
# COMPROBACIONES
# =========================================================

if __name__ == "__main__":
    soup = abrir_html(FICHERO)
    assert titulo_pagina(soup) == "Calidad del aire · Red de estaciones (ejemplo)"
    assert licencia(soup).startswith("Datos publicados bajo licencia CC BY 4.0")

    est = estaciones(soup)
    assert len(est) == 4 and est[0] == {"codigo": "T01", "nombre": "Torrent Centro",
                                        "municipio": "Torrent", "enlace": "/estaciones/T01"}, est[0]

    assert a_numero("23.5") == 23.5 and a_numero("-") is None
    med = leer_mediciones(soup)
    assert len(med) == 8
    assert med[0] == {"estacion": "T01", "fecha": "2026-10-20", "hora": "08:00",
                      "pm10": 23.5, "no2": 41.0, "o3": 35.2}, med[0]
    assert med[2]["o3"] is None and med[3]["pm10"] is None
    assert estaciones_en_alerta(soup) == ["P01", "T02"]
    assert media_pm10(med) == 38.27, media_pm10(med)

    a_xml(est, med, licencia(soup), "calidad_aire.xml")
    assert comprobar_xml("calidad_aire.xml") == (8, 7)        # 8 mediciones; 7 pm10 (falta 1)

    print("✅ Todo correcto")

    # ------------------------------------------------------
    # PARA PENSAR (contesta en comentarios):
    #  a) ¿Qué devuelve soup.find('table', id='noexiste')? ¿Y si encadenas .get_text()?
    #  b) ¿Qué diferencia hay entre find() y find_all()? ¿Y entre select() y select_one()?
    #  c) Si la web cambiara la clase 'estacion' por 'estacion-card', ¿qué parte de tu código se rompe?
    #     ¿Cómo lo detectarías antes de que falle en silencio?
    #  d) ¿Por qué usamos una copia local del HTML? ¿Qué pasaría con una web real que cambia a diario?
    #  e) Mira los 7 valores de PM10 y los 8 <medicion>: ¿por qué no creamos <pm10>None</pm10>?
    #  f) Antes de raspar una web real: ¿dónde miras si te dejan hacerlo? (robots.txt, condiciones de uso)
    # ------------------------------------------------------
