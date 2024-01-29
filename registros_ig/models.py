import sqlite3
from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion

def select_all():
     conectar = Conexion('SELECT * FROM movements order by date DESC')
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

def update_by(id, registro):
     conectarUpdateBy = Conexion(f"update movements set date=?, concept=?, quantity=? where id={id};",registro)
     conectarUpdateBy.con.commit()#función para validar borrado
     conectarUpdateBy.con.close()

def select_ingreso():
     conectarIngreso = Conexion('SELECT sum (quantity) FROM movements where quantity >0;')
     resultadoIngreso = conectarIngreso.res.fetchall()
     conectarIngreso.con.close()

     return resultadoIngreso[0][0]

def select_gasto():
     conectarGasto = Conexion('SELECT sum (quantity) FROM movements where quantity <0;')
     resultadoGasto = conectarGasto.res.fetchall()
     conectarGasto.con.close()

     return resultadoGasto[0][0]
