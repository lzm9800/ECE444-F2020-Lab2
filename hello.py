from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h>Hello World!</h>'

@app.route('/<name>')
def user(name):
    return '<h>Hello {}!</h>'.format(name)
