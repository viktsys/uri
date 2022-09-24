# -*- coding: utf-8 -*-

c = 0
total = 0

while c != 2:
  cod, num, vlr = raw_input().split()
  cod = int(cod)
  num = int(num)
  vlr = float(vlr)
  total = total + num * vlr
  c = c + 1 

print "VALOR A PAGAR: R$", "%.2f" % total