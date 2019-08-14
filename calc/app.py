# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/add')
def call_add():
    var = operations.add(int(request.args['a']), int(request.args['b']))
    return f"<html><head></head><body><h1>{var}</h1></body></html>"


@app.route('/sub')
def call_sub():
    var = operations.sub(int(request.args['a']), int(request.args['b']))
    return f"<html><head></head><body><h1>{var}</h1></body></html>"


@app.route('/mult')
def call_mult():
    var = operations.mult(int(request.args['a']), int(request.args['b']))
    return f"<html><head></head><body><h1>{var}</h1></body></html>"


@app.route('/div')
def call_div():
    var = operations.div(int(request.args['a']), int(request.args['b']))
    return f"<html><head></head><body><h1>{var}</h1></body></html>"