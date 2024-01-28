from registros_ig import app
from flask import render_template

@app.route('/')
def index():
    diccionario = [{'Fecha':'2024-01-01', 'Concepto':'Compra de reyes', 'Monto':-100},
                   {'Fecha':'2024-01-02', 'Concepto':'Compra de comida', 'Monto':-200},
                   {'Fecha':'2024-01-03', 'Concepto':'Compra de bebida', 'Monto':-50},
                   {'Fecha':'2024-01-04', 'Concepto':'Compra de roscon', 'Monto':-20}]
    return render_template('index.html', variable=diccionario)