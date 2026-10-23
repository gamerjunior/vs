
import csv
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

def lectura_de_planetas(nombre_fichero):
    '''función generadora: cada vez que se llame devuelve objeto Planeta
    producido a partir de una fila del fichero'''
    planetas=[]
    with open(nombre_fichero, 'r') as fr:
        reader = csv.reader(fr)
        tiene_cabecera = csv.Sniffer().has_header(fr.read(1024))
        fr.seek(0) # coloca la posición de lectura al inicio de nuevo
        if tiene_cabecera:
            cabecera = next(reader) # ignora la cabecera
        for fila in reader:
            yield Planeta(*fila)


for p in lectura_de_planetas('planetas.csv'): # iterador de Planetas
    print(f'La gravedad en {p.nombre} es {p.gravedad}')
