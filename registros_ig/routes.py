from registros_ig import app
from flask import render_template, request, redirect
from registros_ig.models import *
from datetime import date

def validarFormulario(datosFormularios):
    errores = []#Crear lista para guardar errores
    hoy = str(date.today())#Esto quita la fecha de hoy
    if datosFormularios['date'] > hoy:
        errores.append('La fecha no puede ser mayor a la actual')
    if datosFormularios['concept'] == '':
        errores.append('El concepto no puede ir vacío')
    if datosFormularios['quantity'] == '' or float(datosFormularios['quantity']) == 0.0:
        errores.append('El monto debe ser distinto de 0 y de vacío')

    return errores

@app.route('/')
def index():
    dic = select_all()
    return render_template('index.html', datos=dic)

@app.route('/new', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html', dataForm={})
    else:
        errores = validarFormulario(request.form)
        if errores:
            return render_template('create.html', errors=errores, dataForm=request.form)
        
        insert([request.form['date'],
               request.form['concept'],
               request.form['quantity']
               ])#aquí llamo a la función para registro

        return redirect('/')