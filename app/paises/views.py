from flask import render_template, request, session, jsonify
from . import paises
from app.core import Forca

@paises.route('/')
def index():
    Forca('paises')
    return render_template('paises.html', palavra=session['palavra'])

@paises.route('/get')
def verifica_letra():
    letra = request.args.get('letra')
    resposta = Forca.verificar(letra)

    return jsonify(resposta)
