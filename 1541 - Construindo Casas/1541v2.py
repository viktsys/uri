# -*- coding: utf-8 -*-

x = []
resp = []

while True:
    x = raw_input()
    x = x.split()


    try:
      if x == ['0']:
        break      
      
      a, b, c = x
      a, b, c = int(a), int(b), int(c)
      A = a * b
      t = A * 100 
      t = t / c
      t = t ** 0.5

      resp.append(t)
    except:
      break
for r in resp:
  print int(r)