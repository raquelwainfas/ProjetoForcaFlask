#encoding: utf-8
import random
import os

with open("Animais.txt", "r", encoding="utf8") as animais:
    sorteio = animais.read().split('\n')
    tam = len(sorteio)
    palavra_sorteada = (sorteio[random.randrange(0,tam)])
    
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
    os.system('cls')
    print(final)