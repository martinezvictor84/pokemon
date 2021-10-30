from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    a = 1
    return "return views"


@app.route("/pokemon", methods=['GET', 'POST', 'PUT', 'DELETE'])
def pokemons():
    if request.method == 'GET':
        return "obttiene los pokemos"
    elif request.method == 'POST':
        return "create pokemons"
    elif request.method == 'PUT':
        return "update pokemons"
    elif request.method == 'DELETE':
        return "create pokemons"
