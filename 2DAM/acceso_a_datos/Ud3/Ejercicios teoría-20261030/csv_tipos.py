#READER
with open('libros.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    cabecera = next(reader)           # ['isbn', 'titulo', ...] la cabecera es una fila más
    for fila in reader:
        print(fila[1], fila[3])       # por posición: título y año

#DICTREADER
with open('libros.csv', newline='', encoding='utf-8') as f:
    for fila in csv.DictReader(f):
        print(fila['titulo'], fila['anio'])   # acceso por nombre

with open('salida.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['isbn', 'titulo', 'autor'])     # la cabecera, a mano
    writer.writerow(['1', 'Dune', 'Herbert'])
    writer.writerows(lista_de_listas)                

#DICTWRITER
columnas = ['isbn', 'titulo', 'autor']
with open('salida.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=columnas)
    writer.writeheader()                      # escribe la cabecera
    writer.writerow({'isbn': '1', 'titulo': 'Dune', 'autor': 'Herbert'})
    writer.writerows(lista_de_diccionarios)   