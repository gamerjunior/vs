
import zipfile

if __name__ == '__main__':

    ficheros_planetas = [
        'Mercurio.xml', 'Venus.xml', 'Tierra.xml', 'Marte.xml',
        'Jupiter.xml', 'Saturno.xml', 'Urano.xml', 'Neptuno.xml'
    ]
    nombre_zip = 'zip_planetas_separados.zip'
    fichero_zip = zipfile.ZipFile(nombre_zip, mode='w') # para escribir
    for nombre_fichero_xml in ficheros_planetas:
        fichero_zip.write(nombre_fichero_xml)
    fichero_zip.close() # persistencia

    zip_leido = zipfile.ZipFile(nombre_zip, mode='r') # para leer
    print(zip_leido.namelist())
    print(zip_leido.infolist())

    neptuno = zip_leido.getinfo('Neptuno.xml')
    print(neptuno)
    print(zip_leido.extract('Neptuno.xml', 'Neptuno_extraido'))

    nombre_zip = 'zip_planetas_unico_fichero.zip'
    fichero_zip = zipfile.ZipFile(nombre_zip, mode='w') # para escribir
    fichero_zip.write('planetas.xml')
    fichero_zip.close() # persistencia


