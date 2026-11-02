
from bs4 import BeautifulSoup, Tag

def calc_gravedad(masa, radio):
    g_constante = 6.67e-11
    return g_constante * float(masa) / (float(radio) ** 2)

with open('planetas.html', 'r') as fs:
    cadena_html = fs.read()

html = BeautifulSoup(cadena_html, 'html.parser')
print(html.title.text)
print(html.body.find_all('h2'))
planetas = html.find_all('div', class_='planeta')
for planeta in planetas:
    masa = planeta.select_one('.masa').text
    radio = planeta.select_one('.radio').text
    gravedad = calc_gravedad(masa, radio)
    gravedad_tag = html.new_tag(name='div', attrs={'class': 'gravedad'})
    gravedad_tag.string = str(gravedad)
    planeta.append(gravedad_tag)

nombre_salida = 'planetas_con_gravedad.html'
with open(nombre_salida, 'w') as fw:
    fw.write(html.prettify())
