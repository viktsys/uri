# -*- coding: utf-8 -*-
valores = raw_input().split()
codigo, qte = valores

qte = int(qte)

if codigo == "1":
  resultado = qte * 4.00
if codigo == "2":
  resultado = qte * 4.50
if codigo == "3":
  resultado = qte * 5.00
if codigo == "4":
  resultado = qte * 2.00
if codigo == "5":
  resultado = qte * 1.50

print "Total: R$",  '%.2f' % resultado