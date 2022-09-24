# -*- coding: utf-8 -*-

maior = 0
lista = {}
posicao = 0

while posicao < 100:
    valor = int(raw_input())
    if(valor > maior):
        maior = valor
        lista[valor] = posicao
    posicao += 1
print maior
print lista[maior]+1