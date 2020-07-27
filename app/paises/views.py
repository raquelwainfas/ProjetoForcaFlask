from flask import render_template, session, jsonify, request
from . import paises
from app.core import Forca

@paises.route('/')
def index():
    f = Forca('paises')
    session['palavra'] = f.palavra()

    return render_template('paises.html', palavra=session['palavra'])

@paises.route('/get/')
def verifica_letra():
    letra = request.args.get('letra')

    if letra in session['palavra'].lower():
        return jsonify({'status': True})
    return jsonify({'status': False})
