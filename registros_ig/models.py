import sqlite3

def select_all():
     conexion = sqlite3.connect("data/db_movimientos.sqlite")
     cur = conexion.cursor()
     res = cur.execute("SELECT * FROM movements;")
     filas = res.fetchall()#los datos de columnas (2024-01-01,Nomina Enero, 4000)
     columnas = res.description#los nombres de columnas (id,0000)(date,000)(concep)

     lista_diccionario = []
     diccionario = {}
     for f in filas:
          posicion = 0
          diccionario = {}
          for c in columnas:
               diccionario[c[0]] = f[posicion]
               posicion += 1
          
          lista_diccionario.append(diccionario)
     conexion.close()

     return lista_diccionario

def insert(registroForm):
     conexion = sqlite3.connect("data/db_movimientos.sqlite")
     cur = conexion.cursor()
     res = cur.execute('INSERT INTO movements (date, concept, quantity) VALUES (?,?,?);', registroForm)

     conexion.commit()#Función para validar el registro

     conexion.close()