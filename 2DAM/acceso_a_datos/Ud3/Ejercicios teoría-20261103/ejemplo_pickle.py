
from ejemplo_csv_tipado import lectura_de_planetas
import pickle

# lectura de planetas de un csv
planetas = list(lectura_de_planetas('planetas.csv'))

with open('pickled_planetas', 'wb') as fw:
    # preparamos un stream de datos pickle para escribir en fw 
    pickler = pickle.Pickler(fw) 
    # guarda la versión pickle de planetas en el fichero
    pickler.dump(planetas) 

with open('pickled_planetas', 'rb') as fr:
    # prepara stream de lectura desde fr y 
    # lee objetos pickle pasándolos a objetos Python
    planetas_serializados = pickle.Unpickler(fr).load()

print(f'planetas serializados {planetas_serializados}')

assert planetas == planetas_serializados