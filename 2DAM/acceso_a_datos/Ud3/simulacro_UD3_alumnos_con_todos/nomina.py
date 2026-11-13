import csv
import json
import xml.etree.ElementTree as ET

FICHERO_EMPLEADOS = "empleados.json"
FICHERO_FICHAJES = "fichajes.csv"
FICHERO_HORAS = "horas.json"
FICHERO_ERRORES = "errores.csv"
FICHERO_DEPARTAMENTOS = "departamentos.xml"


def minutos(hora):
    # TODO 1
    datos = hora.split(":")
    try:
        if len(datos) == 2 and len(datos[0]) == 2 and len(datos[1]) == 2:
            if datos[0].isdigit() and datos[1].isdigit():
                horas = int(datos[0])
                minutos = int(datos[1])
                if horas < 24 and minutos < 60:
                    return horas * 60 + minutos
    except ValueError:
        pass

    raise ValueError("hora inválida")


def fecha_valida(f):
    # TODO 2
    datos = f.split("-")
    try:
        if len(datos) == 3 and datos[0].isdigit() and len(datos[0]) == 4 and datos[1].isdigit() and len(datos[1]) == 2 and datos[0].isdigit() and len(datos[2]) == 2:
                if int(datos[1]) >=1 and int(datos[1]) <=12 and int(datos[2]) >= 1 and int(datos[2]) <=31:
                    return True
                else:
                    return False
        else:
            return False    
    except ValueError:
        return False



def validar(fila, empleados):
    # TODO 3
    if len(fila) != 4:
        return None, "fila inválida"
    if fila[0] not in empleados:
        return None, "empleado desconocido"
    if not fecha_valida(fila[1]):
        return None, "fecha inválida"

    try:
        entrada = minutos(fila[2])
        salida = minutos(fila[3])
    except ValueError:
        return None, "hora inválida"

    if salida <= entrada:
        return None, "salida anterior o igual a entrada"

    return salida - entrada, None


def cargar_empleados():
    # TODO 4
    dic = {}
    with open(FICHERO_EMPLEADOS, "r", encoding="utf-8") as f:
        datos = json.load(f)
        for i in datos:
            dic[i["id"]] = i
    return dic


def procesar_fichajes(empleados):
    # TODO 5
    mins = {id_empleado: 0 for id_empleado in empleados}
    errores = []
    validos = 0
    with open(FICHERO_FICHAJES, "r", encoding="utf-8", newline="") as fr:
        reader = csv.reader(fr, delimiter=";")
        next(reader, None)
        linea = 1
        for fila in reader:
            linea += 1
            minutos_trabajados, motivo = validar(fila, empleados)
            if motivo is None:
                mins[fila[0]] += minutos_trabajados
                validos += 1
            else:
                errores.append([linea, motivo, ";".join(fila)])
                
    return mins, errores, validos
            


def escribir_horas(empleados, mins, validos):
    #TODO 6
    lista_empleados = []
    for id_empleado in sorted(empleados):
        empleado = empleados[id_empleado]
        horas = round(mins[id_empleado] / 60, 2)
        importe = round(horas * empleado["precio_hora"], 2)
        lista_empleados.append({
            "id": id_empleado,
            "nombre": empleado["nombre"],
            "departamento": empleado["departamento"],
            "horas": horas,
            "importe": importe
        })

    datos = {
        "fichajes_validos": validos,
        "empleados": lista_empleados
    }
    with open(FICHERO_HORAS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def escribir_errores(errores):
    #TODO 7
    with open(FICHERO_ERRORES, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["linea", "motivo", "contenido"])
        writer.writerows(errores)


def escribir_departamentos(empleados, mins):
    #TODO 8
    departamentos = {}
    for id_empleado, empleado in empleados.items():
        nombre = empleado["departamento"]
        if nombre not in departamentos:
            departamentos[nombre] = {
                "empleados": 0,
                "horas": 0,
                "importe": 0
            }

        horas = round(mins[id_empleado] / 60, 2)
        importe = round(horas * empleado["precio_hora"], 2)
        departamentos[nombre]["empleados"] += 1
        departamentos[nombre]["horas"] += horas
        departamentos[nombre]["importe"] += importe

    raiz = ET.Element("departamentos")
    for nombre in sorted(departamentos):
        datos = departamentos[nombre]
        ET.SubElement(
            raiz,
            "departamento",
            nombre=nombre,
            empleados=str(datos["empleados"]),
            horas=f"{datos['horas']:.2f}",
            importe=f"{datos['importe']:.2f}"
        )

    ET.indent(raiz)
    ET.ElementTree(raiz).write(
        FICHERO_DEPARTAMENTOS,
        encoding="utf-8",
        xml_declaration=True
    )


def main():
    empleados = cargar_empleados()
    mins, errores, validos = procesar_fichajes(empleados)
    escribir_horas(empleados, mins, validos)
    escribir_errores(errores)
    escribir_departamentos(empleados, mins)
    print(f"Validos: {validos} - Errores: {len(errores)}")


if __name__ == "__main__":
    main()
