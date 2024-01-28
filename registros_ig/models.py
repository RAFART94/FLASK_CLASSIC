import sqlite3
from registros_ig import ORIGIN_DATA

def select_all():
     conexion = sqlite3.connect(ORIGIN_DATA)
     cur = conexion.cursor()
     res = cur.execute("SELECT * FROM movements;")
     filas = res.fetchall()#los datos de columnas (2024-01-01,Nomina Enero, 4000)
     columnas = res.description#los nombres de columnas (id,0000)(date,000)(concep)

     lista_diccionario = []

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
     conexion = sqlite3.connect(ORIGIN_DATA)
     cur = conexion.cursor()
     res = cur.execute('INSERT INTO movements (date, concept, quantity) VALUES (?,?,?);', registroForm)

     conexion.commit()#Función para validar el registro

     conexion.close()

def select_by(id):
     conexion = sqlite3.connect(ORIGIN_DATA)
     cur = conexion.cursor()
     res = cur.execute(f"SELECT * FROM movements WHERE id={id};")
     result = res.fetchall()
     return result[0]