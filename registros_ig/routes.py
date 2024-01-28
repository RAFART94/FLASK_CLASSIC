from registros_ig import app

@app.route('/')
def hello():
    return 'HHola esto es flask classic'