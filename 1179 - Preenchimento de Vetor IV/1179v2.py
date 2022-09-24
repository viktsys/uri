# -*- coding: utf-8 -*-

Pares = []
Impares = []

for i in range(15):
    entrada = int(raw_input())
    if(entrada % 2 == 0):
        Pares.append(entrada)
    else:
        Impares.append(entrada)

    if len(Pares) == 5:
        Cnt = 0
        for v in Pares:
            print("par[%d] = %d" % (Cnt,v))
            Cnt += 1
        Pares = []
    if len(Impares) == 5:
        Cnt = 0
        for v in Impares:
            print("impar[%d] = %d" % (Cnt,v))
            Cnt += 1  
        Impares = []


if len(Impares)> 0:
    Cnt = 0
    for valor in Impares:
        print "impar[%d] = %d" % (Cnt, valor)
        Cnt = Cnt + 1

if len(Pares) > 0:
    Cnt = 0
    for valor in Pares:
        print "par[%d] = %d" % (Cnt, valor)
        Cnt = Cnt + 1