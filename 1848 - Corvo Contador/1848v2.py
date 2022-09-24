# -*- coding: utf-8 -*-

for i in range(3):
  s = 0
  while True:
      piscada = raw_input()

      if piscada != 'caw caw':
        
        piscada = piscada.replace('-','0')
        piscada = piscada.replace('*','1')

        piscada = int(piscada, 2)
        s = s + piscada
      else:
        print s
        break
