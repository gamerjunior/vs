
# de aquí se importa lectura de planetas para obtener una lista de objetos Planeta a partir de un csv
from ejemplo_csv_tipado_escritura import lectura_de_planetas
# para construir un arbol de nodos
import xml.etree.ElementTree as ET

def planeta_en_xml(planeta):
    '''
    retorna un elemento planeta_xml con sus elementos hijo
    a partir de un objeto Planeta
    '''
    planeta_xml = ET.Element('planeta')
    for campo in ['nombre', 'masa', 'radio', 'gravedad']:
        campo_xml = ET.Element(campo)
        campo_xml.text = str(getattr(planeta, campo))
        planeta_xml.append(campo_xml)
    return planeta_xml

def escribir_xml(planeta):
    '''se ocupa de escribir el fichero xml de un planeta'''
    planeta_xml = planeta_en_xml(planeta)
    arbol = ET.ElementTree(planeta_xml)
    arbol.write(f'{planeta.nombre}.xml')

def escribir_planetas_xml(planetas):
    planetas_xml = ET.Element('planetas')
    for planeta in planetas:
        planeta_xml = planeta_en_xml(planeta)
        planetas_xml.append(planeta_xml)
    arbol = ET.ElementTree(planetas_xml)
    arbol.write('planetas.xml')

if __name__ == '__main__':
    # obtenemos lista de objetos Planeta
    planetas = list(lectura_de_planetas('planetas.csv'))
    # escritura del fichero xml de cada planeta
    for planeta in planetas:
        escribir_xml(planeta)
    # escritura del fichero xml de todos los plsnetas
    escribir_planetas_xml(planetas)
