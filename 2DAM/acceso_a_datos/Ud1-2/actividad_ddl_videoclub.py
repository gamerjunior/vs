"""
actividad_ddl_videoclub.py
Acceso a Datos · Repaso Python + SQLite (DDL)

Hoy montamos la base de datos de un videoclub. En este ejercicio solo
tocamos DDL (Data Definition Language): crear y borrar tablas.
En el siguiente ejercicio (DML) rellenaremos estas mismas tablas con datos,
así que no borres el fichero videoclub.db al terminar.

Repaso rápido de lo que necesitas:
    nombre_conexion = sqlite3.connect(fichero)
    nombre_cursor = nombre_conexion.cursor()
    nombre_cursor.execute(sentencia_sql)
    nombre_conexion.commit()  
"""
import sqlite3

conn = sqlite3.connect("VIDEOCLUB.db")
cur = conn.cursor()

# ===========================================================
# PASO 1 · Tabla PELICULA
# ===========================================================
# Campos: id (entero, clave primaria), titulo (texto), genero (texto),
#         anyo (entero), disponible (entero: 1 = se puede prestar, 0 = prestada)

# TODO 1: crea la tabla PELICULA.

cur.execute("""CREATE TABLE IF NOT EXISTS PELICULA(
             id INTEGER PRIMARY KEY,
             titulo TEXT,
             genero TEXT,
             anyo INTEGER,
             disponible INTEGER
);
""")


# ===========================================================
# PASO 2 · Tabla SOCIO
# ===========================================================
# Campos: dni (texto, clave primaria), nombre (texto), telefono (texto)

# TODO 2: crea la tabla SOCIO.
cur.execute("""CREATE TABLE IF NOT EXISTS SOCIO(
             dni TEXT PRIMARY KEY,
             nombre TEXT,
             telefono TEXT

);
""")


# ===========================================================
# PASO 3 · Tabla PRESTAMO (los socios tienen películas)
# ===========================================================
# Campos: id (entero, clave primaria), pelicula_id (entero),
#         socio_dni (texto), fecha_prestamo (texto)
# pelicula_id es clave ajena hacia PELICULA(id)
# socio_dni es clave ajena hacia SOCIO(dni)

# TODO 3: crea la tabla PRESTAMO.
cur.execute("""CREATE TABLE IF NOT EXISTS PRESTAMO(
             id TEXT PRIMARY KEY,
             fecha_prestamo TEXT,
             pelicula_id INTEGER,
             socio_id TEXT,
             FOREIGN KEY(pelicula_id) REFERENCES PELICULA(id),
             FOREIGN KEY(socio_id) REFERENCES SOCIO(id)
);
""")
conn.commit()
print("Tablas creadas (o ya existentes): PELICULA, SOCIO, PRESTAMO")


# ===========================================================
# PASO 4 · Comprobación
# ===========================================================
# Lanza la siguiente sentencia de comprobación.

###TODO("SELECT name FROM sqlite_master WHERE type='table'")


cur.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
print("Tablas en la base de datos:", [fila[0] for fila in cur.fetchall()])


# ===========================================================
# PASO 5 · Rómpelo: borrar una tabla que no existe
# ===========================================================

# TODO 4: intenta borrar una tabla (sin IF EXISTS) llamada "PELICULA_VIEJA" (que nunca
#         hemos creado). Captura la excepción para evitar que la aplicación se rompa.
try:
    cur.execute("""DROP TABLE PELICULA_VIEJA""")
except sqlite3.OperationalError as e:
    print("error",e)

print("\n--- Fin del ejercicio de DDL. No borres videoclub.db ---")
conn.close()
