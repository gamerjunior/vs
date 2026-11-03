
from html.parser import HTMLParser

class HTMLParserPropio(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Comienzo de etiqueta: {tag}')
    
    def handle_endtag(self, tag):
        print(f'Fin de etiqueta: {tag}')

    def handle_data(self, data):
        info = data.strip()
        if info:
            print(f'Contenido: {info}')

parser = HTMLParserPropio()
parser.feed('<html><head><title>Ejemplo simple</title></head>'
            '<body><h1>ejemplo especial</h1></body>')