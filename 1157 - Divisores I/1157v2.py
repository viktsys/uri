# -*- coding: utf-8 -*-

entrada = int(raw_input())

Divisores = []
C = 1

while C <= entrada:
  if entrada % C == 0:
    Divisores.append(C)
  C = C + 1

for num in Divisores:
  print num