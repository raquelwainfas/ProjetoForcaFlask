# -*- coding: utf-8 -*-
from .main import categorias

class Forca:
    def __init__(self, categoria):
        self.opcao = categorias[categoria]()

    def palavra(self):
        return self.opcao.palavra_sorteada


if __name__ == '__main__':

    with open("Animais.txt", "r", encoding="utf8") as animais:
        sorteio = animais.read().split('\n')
        tam = len(sorteio)
        palavra_sorteada = (sorteio[random.randrange(0,tam)]) #noqa
    # print(palavra_sorteada.upper()+'\n')

    qtd_letras = (len(palavra_sorteada))
    #print(qtd_letras)
    escondida = qtd_letras * '_'
    print(qtd_letras * '_ ')

    lista_palavra = list(palavra_sorteada.upper())
    escondida = list(escondida)

    # print(lista_palavra)
    # print(escondida)

    while "_" in escondida:

        letra_ipt = input("Digite uma letra: ")

        for index in range(len(lista_palavra)):
            if letra_ipt.upper() in lista_palavra[index]:
                #print(index)
                escondida[index] = letra_ipt.upper()
                #print(escondida)
                final = " ".join(escondida)
        os.system('cls') #noqa
        print(final)