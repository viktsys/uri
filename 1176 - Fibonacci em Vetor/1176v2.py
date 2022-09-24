# -*- coding: utf-8 -*-
Fib = [0, 1]
Ant = 0
Atl = 1

for i in range(60):
    Tmp = Atl + Ant
    Fib.append(Tmp)
    Ant = Atl
    Atl = Tmp   
entrada = int(raw_input())
for i in range(entrada):
    valor = int(raw_input())
    print 'Fib(%d) = %d' % (valor, Fib[valor])