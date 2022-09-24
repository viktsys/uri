# -*- coding: utf-8 -*-

for i in range(10):
    entrada = int(raw_input())
    if(entrada < 1):
        entrada = 1
    print "X[%d] = %d" %(i, entrada)