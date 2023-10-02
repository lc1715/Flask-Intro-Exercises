# Put your app in here.

from operations import add, sub, mult, div

from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def do_add():  
    """Add a and b parameters."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a,b)
    return str(result)
    

@app.route('/sub')
def subtract():
    """Subtract a and b parameters."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))


@app.route('/mult')
def multiply():
    """Multiply a and b parameters."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))


@app.route('/div')
def divide():
    """Divide a and b parameters."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))




# Further Study:
@app.route('/math/<calc>')
"""
Will add, subtract, multiply or divide the numbers a and b
"""
def calculate(calc):  

    a = int(request.args['a'])
    b = int(request.args['b'])

    operations = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

    return str(operations[calc](a,b))
