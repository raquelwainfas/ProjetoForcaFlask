# -*- coding: utf-8 -*-
from .main import categorias
from flask import session

class Forca:
    def __init__(self, categoria):
        self.opcao = categorias[categoria]()
        session['palavra'] = self.opcao.palavra_sorteada

    @staticmethod
    def verificar(letra):
        pos = [i+1 for i, l in enumerate(session['palavra'].lower()) if l == letra.lower()]

        if pos:
            return {'status': True, 'pos':pos}
        return {'status': False}
