# -*- coding: utf-8 -*-

I = 0
while I != 100:    
    entrada = float(raw_input())
    if(entrada <= 10):
        print "A[%d] = %.1f" %(I, entrada)
    I = I + 1
