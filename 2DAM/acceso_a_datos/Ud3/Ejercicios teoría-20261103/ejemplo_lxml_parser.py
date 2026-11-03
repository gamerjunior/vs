from lxml import etree

class HTMLParserPropio(object):
    def start(self, tag, attrs):
        print(f'Comienzo de etiqueta: {tag}')
    
    def end(self, tag):
        print(f'Fin de etiqueta: {tag}')

    def data(self, data):
        info = data.strip()
        if info:
            print(f'Contenido: {info}')
    
    def comment(self, text):
        print(f'Comentario: {text}')

    def close(self):
        print('Cerrando ...')


with open('planetas.html', 'r') as fs:
    cadena_html = fs.read()

parser = etree.XMLPullParser(target=HTMLParserPropio())
parser.feed(cadena_html)
parser.close()