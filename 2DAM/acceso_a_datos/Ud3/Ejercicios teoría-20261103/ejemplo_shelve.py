
import shelve
from ejemplo_csv_tipado import lectura_de_planetas

nombre_db = 'planetas' # fichero para persistir dicts
d = shelve.open(nombre_db) # abrimos base de datos y obtenemos objeto Shelf

# genera una lista de objetos Planeta
planetas = list(lectura_de_planetas('planetas.csv'))

# se guarda en el Shelf
d['planetas'] = planetas

# planeta tierra
tierra = [p for p in planetas if p.nombre == 'Tierra'][0]
# lista planetas mayores que la tierra
p_mayores = [p for p in planetas if p.radio > tierra.radio]
# lista planetas mayores que la tierra
p_menores = [p for p in planetas if p.radio < tierra.radio]

# se guardan en el Shelf
d['planetas_mayores'] = p_mayores
d['planetas_menores'] = p_menores

d.close() # se cierra y se persisten los cambios

# se abre de nuevo y tiene los datos de antes
d = shelve.open(nombre_db)
print(f'Claves guardadas en shelve: {list(d.keys())}')
for k, v in d.items():
    print(f'{k} -> {v}')