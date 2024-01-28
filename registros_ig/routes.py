from registros_ig import app
from flask import render_template
from registros_ig.models import *

@app.route('/')
def index():
    dic = select_all()
    return render_template('index.html', datos=dic)

@app.route('/new')
def create():
    return 'Esto es una vista de registro'