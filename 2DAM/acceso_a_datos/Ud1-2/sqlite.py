import sqlite3

conn = sqlite3.connect("ejemplos.db")
cur = conn.cursor()

sentencia='''create table if not exists  prueba (
c1 TEXT,
c2 TEXT,
PRIMARY KEY(c1)
)'''

cur.execute(sentencia)


#v1 = input("Introduce el dato 1:")
#v2 = input("Introduce el dato 2:")

lista =[("uno","dos"),("tres","cuatro")] 

#sentencia = "Insert into prueba values (?,?)"
sentencia = "select * from prueba"

#cur.execute(sentencia,(v1,v2))
#cur.executemany(lista)
res = cur.fetchone()
print(type(res))
print(res)
conn.commit()
conn.close
