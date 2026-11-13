
import csv

def lectura_csv(nombre_fichero):
    '''abre un fichero en formato csv y lo 
    muestra por pantalla
    '''

     
    with open(nombre_fichero, 'r') as fr:
        reader = csv.reader(fr) # obtenemos iterador sobre las líneas del fichero csv
        for fila in reader:
            print(fila) # list

lectura_csv('planetas.csv')