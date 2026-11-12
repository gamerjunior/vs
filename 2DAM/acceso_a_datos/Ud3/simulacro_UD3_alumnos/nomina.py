import csv
import json
from datetime import date
from datetime import time
FICHEROEMPLEADOS = "empleados.json"
FICHEROFICHAJES = "fichajes.csv"


    
        
def RF1(empleados, fichajes):
    #lista de fichaje
    fich = list()
    validos = list()
    #leemos las lineas de fichajes buscando los que tengan 4 campos
    with open(fichajes, "r", encoding="utf-8", newline="") as fr:
            reader = csv.DictReader(fr, delimiter= ";")
            next(reader)
            for fila in reader:
                 if fila.__len__() == 4:
                       fich.append(fila)
    #leemos las lienas de empleados buscando los mque estan en fichajes
    with open(empleados, "r", encoding="utf-8") as f:
        datos = json.load(f)
        for fila in fich:
            for filaatributos in datos:
                if fila[0] == filaatributos["id"]:
                    validos.append(fila)
                    break
            try:
                date.fromisoformat(fila[1])
                time.fromisoformat(fila[2])
                time.fromisoformat(fila[3])
            except ValueError:
                validos.remove(fila)
    
    for fila in validos:
        if fila[2] > fila[3]:
            validos.remove(fila)

    print(validos)
    return validos


RF1(FICHEROEMPLEADOS, FICHEROFICHAJES)
             
             


     

    

