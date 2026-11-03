
import xml.etree.ElementTree as ET
import ejemplo_importar_archivos_XML

def escribir_planetas(planetas, fichero_salida):
    raiz = ET.Element('sistemasolar-completo') # raíz del árbol final

    for planeta in planetas:
        # crea Element planeta con attrib nombre
        planeta_xml = ET.Element('planeta', attrib=dict(nombre=planeta.nombre))
        
        # crea Element masa
        masa_xml = ET.Element('masa') #agrega cada elemento de cada planeta
        masa_xml.text = str(planeta.masa)

        # crea Element radio
        radio_xml = ET.Element('radio', atrib=dict(unidad='km'))
        radio_xml.text = str(planeta.radio)

        # crea Element gravedad
        gravedad_xml = ET.Element('gravedad')
        gravedad_xml.text = str(planeta.gravedad)

        # se añaden subelementos al planeta
        planeta_xml.extend([masa_xml, radio_xml, gravedad_xml])
        
        # se engancha el planeta a la raíz
        raiz.append(planeta_xml)

    arbol = ET.ElementTree(raiz) #crea un objeto arbol para poder guardar

    arbol.write(fichero_salida) #guarda el árbol completo en un fichero

if __name__ == '__main__':
    planetas = ejemplo_importar_archivos_XML.extraer_planetas_de_xml('planetas.xml')
    fichero_xml_salida = 'planetas_completos.xml'
    escribir_planetas(planetas, fichero_xml_salida)