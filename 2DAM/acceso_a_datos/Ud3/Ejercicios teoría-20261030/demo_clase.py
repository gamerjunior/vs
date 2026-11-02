"""
DEMO DE CLASE · HTML, parsers y BeautifulSoup
Acceso a Datos · UD3

Uso:   python demo_clase.py          -> ejecuta todos los bloques
       python demo_clase.py 3        -> ejecuta solo el bloque 3
       python demo_clase.py 3 5      -> bloques 3 y 5

Necesita calidad_aire.html en la misma carpeta  (pip install beautifulsoup4 lxml)
"""
import sys
from html.parser import HTMLParser

from bs4 import BeautifulSoup

FICHERO = "calidad_aire.html"


def cabecera(n, titulo):
    print(f"\n{'=' * 60}\nBLOQUE {n} · {titulo}\n{'=' * 60}")


def soup_local():
    with open(FICHERO, "r", encoding="utf-8") as f:
        return BeautifulSoup(f.read(), "html.parser")


# ---------------------------------------------------------
def bloque_1():
    cabecera(1, "¿Por qué no vale split / expresiones regulares?")
    with open(FICHERO, encoding="utf-8") as f:
        texto = f.read()
    # Intento ingenuo: el nombre de la primera estación entre <h2> y </h2>
    # (¡ojo!, el primer <h2> es el título de la sección, no una estación)
    trozo = texto.split("<h2>")[1].split("</h2>")[0]
    print("split ingenuo ->", repr(trozo))
    # Cambiamos un detalle que a un humano le da igual:
    otro = texto.replace("<h2>", '<h2 class="nombre">')
    try:
        print(otro.split("<h2>")[1].split("</h2>")[0])
    except IndexError:
        print("split ya no encuentra '<h2>': se rompe con cambiar un atributo")


# ---------------------------------------------------------
class MostrarEventos(HTMLParser):
    """El parser nos AVISA de cada evento. El estado lo llevamos nosotros."""

    def handle_starttag(self, tag, attrs):
        print("  start", tag, attrs)

    def handle_endtag(self, tag):
        print("  end  ", tag)

    def handle_data(self, data):
        if data.strip():
            print("  data ", repr(data.strip()))


class NombresEstacion(HTMLParser):
    """Sacar el texto de los <h2> que están dentro de <div class="estacion">."""

    def __init__(self):
        super().__init__()
        self.en_estacion = False   # bandera: ¿estoy dentro de un div.estacion?
        self.en_h2 = False         # bandera: ¿estoy dentro de un h2?
        self.nombres = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "div" and d.get("class") == "estacion":
            self.en_estacion = True
        elif tag == "h2" and self.en_estacion:
            self.en_h2 = True

    def handle_endtag(self, tag):
        if tag == "h2":
            self.en_h2 = False
        elif tag == "div":
            self.en_estacion = False

    def handle_data(self, data):
        if self.en_h2:
            self.nombres.append(data.strip())


def bloque_2():
    cabecera(2, "html.parser de la librería estándar: eventos")
    MostrarEventos().feed("<p class='x'>hola <b>mundo</b></p>")
    print("\nAhora, sacar los nombres de estación con banderas:")
    p = NombresEstacion()
    with open(FICHERO, encoding="utf-8") as f:
        p.feed(f.read())
    print(" ", p.nombres)
    print("  -> funciona, pero ¡mira cuánto código y cuánto estado a mano!")


# ---------------------------------------------------------
def bloque_3():
    cabecera(3, "bs4 delega en un parser: html.parser frente a lxml")
    roto = "<ul><li>Uno<li>Dos<p>Texto <b>negrita</ul>"
    print("HTML de entrada:", roto)
    for parser in ("html.parser", "lxml"):
        print(f"\n{parser:12}->", BeautifulSoup(roto, parser))
    print("\nEl HTML real viene roto y cada parser lo 'arregla' a su manera.")


# ---------------------------------------------------------
def bloque_4():
    cabecera(4, "BeautifulSoup: abrir y buscar")
    soup = soup_local()
    print("title        ->", soup.title.get_text(strip=True))
    print("h1           ->", soup.h1.get_text(strip=True))
    print("find id      ->", soup.find(id="licencia").get_text(strip=True))
    estaciones = soup.find_all("div", class_="estacion")     # class_ con guion bajo
    print("find_all     ->", len(estaciones), "estaciones")
    print("select (CSS) ->", len(soup.select("table#mediciones tbody tr")), "filas")
    print("select_one   ->", soup.select_one("div.estacion h2").get_text(strip=True))


def bloque_5():
    cabecera(5, "Texto y atributos")
    soup = soup_local()
    div = soup.find("div", class_="estacion")
    print("código (div['data-codigo']) ->", div["data-codigo"])
    print("enlace (a['href'])          ->", div.find("a")["href"])
    print("get() de atributo que no existe ->", div.get("no-existe"))
    try:
        div["no-existe"]
    except KeyError as e:
        print("div['no-existe'] -> KeyError:", e)
    fila = soup.select("table#mediciones tbody tr")[0]
    print("celdas ->", [td.get_text(strip=True) for td in fila.find_all("td")])
    print("clases de una fila alerta ->", soup.select_one("tr.alerta").get("class"))


def bloque_6():
    cabecera(6, "Errores típicos")
    soup = soup_local()
    print("find() de algo que no existe ->", soup.find("table", id="noexiste"))
    try:
        soup.find("table", id="noexiste").get_text()
    except AttributeError as e:
        print("encadenar .get_text() ->", type(e).__name__, "-", e)
    texto = soup.select("table#mediciones tbody tr")[2].find_all("td")[5].get_text(strip=True)
    print("celda de O3 sin dato ->", repr(texto))
    try:
        float(texto)
    except ValueError as e:
        print("float('-') ->", type(e).__name__, "-", e)
    print("Los textos son str: hay que convertir y tratar el '-'.")


BLOQUES = {1: bloque_1, 2: bloque_2, 3: bloque_3, 4: bloque_4, 5: bloque_5, 6: bloque_6}

if __name__ == "__main__":
    elegidos = [int(a) for a in sys.argv[1:]] or sorted(BLOQUES)
    for n in elegidos:
        BLOQUES[n]()
