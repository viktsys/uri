# -*- coding: utf-8 -*-
Vetor = []
for i in range(20):    
    entrada = int(raw_input())
    Vetor.append(entrada)
pos = 0

for l in Vetor[::-1]:
    print "N[%d] = %d" %(pos, l)
    pos += 1