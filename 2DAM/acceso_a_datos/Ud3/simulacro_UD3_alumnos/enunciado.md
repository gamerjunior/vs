# Simulacro UD3 · Persistencia en ficheros

Puedes usar VSCode, tus apuntes y las actividades resueltas. **No** internet ni asistentes de IA.

---

## Situación

Una pequeña empresa registra las entradas y salidas de sus empleados en un fichero CSV y guarda los datos de los empleados en un JSON. Cada mes hay que calcular las horas trabajadas y lo que cobra cada uno. Escribe **desde cero** el programa **`nomina.py`**.

Se ejecuta con `python nomina.py` en una carpeta que contiene los dos ficheros de entrada. No recibe argumentos ni pide datos por teclado.

## Entrada

**`empleados.json`** — lista de empleados:
```json
[ {"id": "E01", "nombre": "Lucía Pons", "departamento": "Taller", "precio_hora": 10.0}, ... ]
```

**`fichajes.csv`** — separador `;`, con cabecera `empleado;fecha;entrada;salida`:
```
E01;2026-10-05;08:00;12:30
```
`empleado` es el `id` del JSON · `fecha` es `AAAA-MM-DD` · `entrada` y `salida` son `HH:MM` (24 h).

## Qué debe hacer

### RF1 · Validar cada fichaje
Un fichaje es **válido** si cumple todo:
- tiene exactamente 4 campos,
- el empleado existe en `empleados.json`,
- la fecha tiene el formato `AAAA-MM-DD` con mes entre 1 y 12 y día entre 1 y 31,
- las dos horas son válidas (horas 0–23, minutos 0–59),
- la salida es **posterior** a la entrada (mismo día).

Los fichajes no válidos se rechazan y el programa continúa. **Nunca debe terminar con un error por un dato mal formado.**

### RF2 · `horas.json`
```json
{
  "fichajes_validos": 4,
  "empleados": [
    {"id": "E01", "nombre": "Lucía Pons", "departamento": "Taller", "horas": 8.5, "importe": 85.0}
  ]
}
```
- Incluye **todos** los empleados del JSON (aunque no tengan fichajes: `horas` y `importe` a 0), ordenados por `id`.
- `horas` = suma de las duraciones de sus fichajes válidos, en horas con **2 decimales**.
- `importe` = horas trabajadas × `precio_hora`, con 2 decimales.
- Con sangría (`indent`) y acentos escritos tal cual.

### RF3 · `errores.csv`
Cabecera `linea,motivo,contenido` y una fila por fichaje rechazado:
- `linea`: número de línea en `fichajes.csv` (la cabecera es la línea 1),
- `motivo`: texto breve redactado por ti,
- `contenido`: el fichaje original (los campos unidos por `;`, sin salto de línea).

### RF4 · `departamentos.xml`
```xml
<departamentos>
  <departamento nombre="Taller" empleados="2" horas="12.50" importe="130.00"/>
  ...
</departamentos>
```
Una etiqueta por departamento, **ordenadas alfabéticamente**; `empleados` = nº de empleados del departamento (tengan fichajes o no); `horas` e `importe` = suma de los de sus empleados, con 2 decimales. Todo atributo XML es texto.

### RF5 · Mensaje final
Imprime: `Validos: N - Errores: M`

## Requisitos no funcionales (1,5 puntos)
- **RNF1** · Código dividido en funciones con nombres claros.
- **RNF2** · Nombres de fichero y valores fijos definidos una sola vez.
- **RNF3** · Ficheros abiertos con `with` y `encoding` explícito (CSV con `newline=""`).
- **RNF4** · Solo herramientas vistas en clase; sin pandas. 

## Evaluación

La nota automática se calcula con **otros datos**. Tienes `empleados.json` y `fichajes.csv` de ejemplo y `comprobar_alumno.py`; pasarlo no garantiza la nota máxima pues hay RNF que se comprueban a mano.

## Consejos
- Empieza por leer los dos ficheros y comprobar que los tienes en estructuras de Python.
- Haz una salida cada vez; una entrega con 2 de 3 ficheros bien vale más que una que no ejecuta.
