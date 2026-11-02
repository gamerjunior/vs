
import xml.etree.ElementTree as ET
from dataclasses import dataclass

@dataclass
class Planeta:
    nombre: str
    masa: float
    radio: float

    def __post_init__(self):
        self.radio = float(self.radio)
        self.masa = float(self.masa)

    @property
    def gravedad(self):
        g_constante = 6.673e-11
        return g_constante * self.masa / (self.radio ** 2)

def extraer_planetas_de_xml(fichero_planetas):
    planetas = []
    # obtener objeto ElementTree
    xml = ET.parse(fichero_planetas)
    # obtener lista de subelementos cuyo nombre sea 'planeta'
    planetas_xml = xml.findall('planeta') # retorna list(Element)
    for planeta_xml in planetas_xml:
        planetas.append(extraer_planeta_de_xml(planeta_xml))

    return planetas # Lista de objetos Planeta

def extraer_planeta_de_xml(planeta_xml):
    # Element.attrib es un diccionario de atributos de ese elemento 
    nombre = planeta_xml.attrib['nombre']
    # buscamos primer subelemento con nombre 'masa' 
    print(planeta_xml.find('masa'))
    masa = planeta_xml.find('masa').text # text es el texto entre el tag y el tag de cierre
    # buscamos primer subelemento con nombre 'radio
    radio = planeta_xml.find('radio').text
    # generamos el objeto con dataclass
    return Planeta(nombre, masa, radio)

if __name__ == '__main__': 
    planetas = extraer_planetas_de_xml('planetas.xml')
    for p in planetas:
        print(f'Nombre: {p.nombre} gravedad: {p.gravedad}')

