"""
actividad_dml_videoclub.py
Acceso a Datos · Repaso Python + SQLite (DML)

Continuamos con la base de datos del videoclub. Aquí solo tocamos DML
(Data Manipulation Language): INSERT, UPDATE, DELETE.
Necesitas haber ejecutado antes actividad_ddl_videoclub.py, para que
existan las tablas PELICULA, SOCIO y PRESTAMO.

"""
import sqlite3

conn = sqlite3.connect("VIDEOCLUB.db")
cur = conn.cursor()

# ===========================================================
# PASO 1 · Insertar películas (una a una, con parámetros ?)
# ===========================================================

# TODO 1: inserta estas 3 películas 
#         con ? (una sentencia, ejecutada 3 veces):
#         (1, "Matrix", "Ciencia ficción", 1999, 1)
#         (2, "El Padrino", "Drama", 1972, 1)
#         (3, "Coco", "Animación", 2017, 1)

sentencia_aniadir = """INSERT INTO PELICULA (id,titulo,genero,anyo,disponible) VALUES (?,?,?,?,?) """

cur.execute(sentencia_aniadir, (1, "Matrix", "Ciencia ficción", 1999, 1))
cur.execute(sentencia_aniadir, (2, "El Padrino", "Drama", 1972, 1))
cur.execute(sentencia_aniadir, (3, "Coco", "Animación", 2017, 1))
# ===========================================================
# PASO 2 · Insertar socios
# ===========================================================

# TODO 2: inserta estos 2 socios en SOCIO, también con ?:
#         ("11111111A", "Marta Ruiz", "600111222")
#         ("22222222B", "Pedro Gil", "600333444")
sentencia_socios =  """INSERT INTO SOCIO (dni,nombre,telefono) VALUES (?,?,?)"""

cur.execute(sentencia_socios, ("11111111A", "Marta Ruiz", "600111222"))
cur.execute(sentencia_socios, ("22222222B", "Pedro Gil", "600333444"))

print("Películas y socios insertados.")


# ===========================================================
# PASO 3 · Inserción masiva 
# ===========================================================
# Vamos a añadir varias películas más de golpe, con una lista de tuplas.
# Ojo, termina la lista.

### TODO 
peliculas = {
    (4, "Spirited Away", "Animación", 2001, 1),
    (5, "Parasite", "Drama", 2019, 1),
    (6, "Interstellar", "Ciencia ficción", 2014, 1),
}

# TODO 3: inserta la lista ed una vez.
cur.executemany(sentencia_aniadir, peliculas)




# ===========================================================
# PASO 4 · Registrar un préstamo (UPDATE + INSERT relacionados)
# ===========================================================
# Marta (11111111A) se lleva prestada "Matrix" (id 1) hoy.

# TODO 4: inserta el préstamo en PRESTAMO:
#         (1, 1, "11111111A", "2026-10-01")

cur.execute("""INSERT INTO PRESTAMO (id,fecha_prestamo,pelicula_id,socio_id) VALUES (?,?,?,?)""", (1,"2026-10-01",1,"11111111A") )

# TODO 5: ahora actualiza la película 1 ("Matrix") para marcarla como
#         NO disponible (disponible = 0)

cur.execute("""UPDATE PELICULA SET disponible = 0 WHERE id = ? """,(1,))

print("Préstamo registrado y película marcada como no disponible.")


# ===========================================================
# PASO 5 · Devolución (DELETE + UPDATE)
# ===========================================================
# Marta devuelve la película. Hay que borrar el préstamo Y volver a
# marcar la película como disponible.

# TODO 6: borra de PRESTAMO el registro.
cur.execute("""DELETE FROM PRESTAMO WHERE ID = ? """,(1,))

# TODO 7: vuelve a poner disponible la película.

cur.execute("""UPDATE PELICULA SET disponible = 1 WHERE id = ? """,(1,))

print("Devolución registrada.")


# ===========================================================
# PASO 6 · Rómpelo: errores típicos de DML
# ===========================================================

print("\n--- Probando errores típicos ---")

# TODO 8: intenta insertar OTRA película con id = 1 (que ya existe).
#         Envuélvelo en try/except sqlite3.IntegrityError y muestra el
#         mensaje de error, sin que el programa se detenga.

try:
    cur.execute("""INSERT INTO PELICULA (id,titulo,genero,anyo,disponible) VALUES (?,?,?,?,?)""", (1,"300","ACCIÓN",1999,1))
except sqlite3.IntegrityError as e:
    print("error: ", e)
    

# TODO 9: intenta insertar una película dando solo 2 valores en vez de
#         los 5 que tiene la tabla (columna incompleta). Captura el
#         except sqlite3.OperationalError.


# ===========================================================
# Comprobación final (ya dada, no hace falta tocarla)
# ===========================================================
print("\n--- Estado final ---")
cur.execute("SELECT * FROM PELICULA ORDER BY id")
print("PELICULA:")
for fila in cur.fetchall():
    print(" ", fila)

cur.execute("SELECT * FROM SOCIO")
print("SOCIO:")
for fila in cur.fetchall():
    print(" ", fila)

cur.execute("SELECT * FROM PRESTAMO")
print("PRESTAMO:")
for fila in cur.fetchall():
    print(" ", fila)

conn.close()
