# -*- coding: utf-8 -*-
import os
import random

class Base:
    caminho_arquivo = str()
    palavra_sorteada = str()

    def __init__(self):
        super(Base, self).__init__()
        self.sortear()

    def sortear(self):
        with open(self.caminho_arquivo, "r", encoding="utf8") as arquivo:
            sorteio = arquivo.read().split('\n')
            tam_lista = len(sorteio)
            self.palavra_sorteada = (sorteio[random.randrange(0,tam_lista)])

class Paises(Base):
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'arquivos/Paises.txt')

class Animais(Base):
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'arquivos/Animais.txt')

categorias = {
    'paises': Paises,
    'animais': Animais
}
