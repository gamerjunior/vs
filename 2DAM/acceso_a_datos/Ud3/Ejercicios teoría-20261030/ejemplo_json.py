
import json
from ejemplo_importar_archivos_XML import Planeta

def como_planetas(dct):
    '''Retorna objeto Planeta a partir de un diccionario 
    que se le pasa como parámetro
    '''
    return Planeta(dct['nombre'], dct['masa'], dct['radio'])

class PlanetaEncoder(json.JSONEncoder):
    '''Si el objeto es de tipo Planeta lo pasa a dict 
    para que json.JSONEncoder pueda codificarlo.
    En otro caso, json.JSONEncoder lo codifica directamente'''
    def default(self, obj):
        if isinstance(obj, Planeta):
            return dict(nombre=obj.nombre, masa=obj.masa, radio=int(obj.radio), gravedad=obj.gravedad)
        return json.JSONEncoder.default(self, obj)
    
with open('planetas.json', 'r') as fr:
    # deserializa planetas.json a objetos Python
    planetas = json.load(fr, object_hook=como_planetas)
    print(planetas[0])

with open('planetas_con_gravedad.json', 'w') as fw:
    # serializa planetas (objetos Python) a planetas_con_gravedad.json
    json.dump(planetas, fw, cls=PlanetaEncoder, indent=4)