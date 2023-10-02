
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'This is the homepage!'


@app.route('/welcome')
def welcome():
    return f"Welcome!"
    

@app.route('/welcome/<word>')
def say_welcome(word):
    return f"Welcome {word}"


