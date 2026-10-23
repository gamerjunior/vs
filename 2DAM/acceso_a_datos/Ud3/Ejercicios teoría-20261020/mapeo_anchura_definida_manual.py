
# from  dataclasses import dataclass

# @dataclass
# class Info: #clase para mapear los valores del fichero
#     amigos: int
#     nombre: str
#     salario: int
#     def __post_init__(self):
#         self.nombre = self.nombre.strip()

class Info:
    def __init__(self,amigos,nombre,salario):
        self.amigos = amigos
        self.nombre = nombre.strip()
        self.salario = salario
    def __repr__(self):
        return f"Info(amigos={self.amigos}, nombre={self.nombre}, salario={self.salario})"
    def imprimir(self):
        print(f"Info(amigos={self.amigos}, nombre={self.nombre}, salario={self.salario})")
    

def ancho_fijo_manual(fichero_origen, anchos):
    info = []
    headers = None
    idx = 0
    with open(fichero_origen, 'r', encoding='utf-8', newline='') as fr:
        for line in fr.readlines(): # retorna lista de cadenas
            if headers is None:
                headers = line
                continue #Omite la primera línea de cabeceras

            inicio, fin = 0, anchos[0] #0-5
            amigos = int(line[inicio:fin])

            inicio, fin = anchos[0], sum(anchos[:2]) #6-21
            nombre = line[inicio:fin]

            inicio, fin = sum(anchos[:2]), sum(anchos[:3]) #22-29
            salario = int(line[inicio:fin])

            info.append(Info(amigos, nombre, salario))
    
    return info


fichero_origen = 'ejemplo_ancho_fijo.txt'

anchos = [6, # Núm. amigos 
          16, # Nombre
          7] # Salario

print(ancho_fijo_manual(fichero_origen, anchos))