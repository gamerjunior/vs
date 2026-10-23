
# ejemplo de como copiar líneas impares de un fichero a otro
def copia_impares(fichero_origen, fichero_destino):
    with open(fichero_origen, 'r', newline='') as fr:
        with open(fichero_destino, 'w', newline='') as fw:
            idx = 0

            for linea in fr.readlines(): # retorna una lista de str
                if not idx % 2:
                    fw.write(linea)
                idx += 1

def examinar_contenido(nombre_fichero):
    with open(nombre_fichero, 'r') as f:
        return f.read()
    
fichero_origen = 'english.txt'
fichero_destino = 'english_impares.txt'
copia_impares(fichero_origen, fichero_destino)
print(examinar_contenido(fichero_destino))
