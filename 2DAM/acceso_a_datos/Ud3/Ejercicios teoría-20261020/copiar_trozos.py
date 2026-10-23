
# ejmplo de como copiar trozos de un determinado tamaño de un
# fichero a otro saltado en el contenido con un desplazamiento definido
def copiar_trozos(fichero_origen, fichero_destino, saltos=100,tamano=10):
    with open(fichero_origen, 'r', newline='') as fr:
        with open(fichero_destino, 'w', newline='') as fw:
            line = fr.read(tamano) # devuelve 0 si se ha leido el fichero completamente
            while line:
                fw.write(line)
                #Avanzando en el fichero
                new_seek = fr.tell() + saltos
                fr.seek(new_seek)
                #leyendo 10 caracteres
                line = fr.read(tamano)

def examinar_contenido(nombre_fichero):
    with open(nombre_fichero, 'r') as f:
        return f.read()

fichero_origen = 'english.txt'
fichero_destino = 'english_saltos.txt'
copiar_trozos(fichero_origen, fichero_destino)
print(examinar_contenido(fichero_destino))