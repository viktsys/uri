# -*- coding: utf-8 -*-
NEnt = int(raw_input())
Lst = [None] * NEnt # Seta o tamanho da lista/vetor

Lst = list(map(int, raw_input().split()))

Pos = 0
Menor = Lst[0]
Cnt = 0

for Valor in Lst:
    if(Valor < Menor):
        Menor = Valor
        Pos = Cnt
    Cnt = Cnt + 1
    
print("Menor valor: %d" % Menor)
print("Posicao: %d" % Pos)