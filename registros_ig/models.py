import sqlite3
from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion

def select_all():
     conectar = Conexion('SELECT * FROM movements;')
     filas = conectar.res.fetchall()#los datos de columnas (2024-01-01,Nomina Enero, 4000)
     columnas = conectar.res.description#los nombres de columnas (id,0000)(date,000)(concep)

     lista_diccionario = []

     for f in filas:
          posicion = 0
          diccionario = {}
          for c in columnas:
               diccionario[c[0]] = f[posicion]
               posicion += 1
          
          lista_diccionario.append(diccionario)
     conectar.con.close()

     return lista_diccionario

def insert(registroForm):
     conectarInsert = Conexion('INSERT INTO movements(date,concept,quantity) VALUES(?,?,?);', registroForm)
     conectarInsert.con.commit()#Función para validar el registro
     conectarInsert.con.close()

def select_by(id):
     conectarSelectBy = Conexion(f'SELECT * FROM movements WHERE id={id};')
     result = conectarSelectBy.res.fetchall()
     conectarSelectBy.con.close()

     return result[0]

def delete_by(id):
     conectarDeleteBy = Conexion(f"DELETE FROM movements WHERE id={id};")
     conectarDeleteBy.con.commit()#función para validar borrado
     conectarDeleteBy.con.close()