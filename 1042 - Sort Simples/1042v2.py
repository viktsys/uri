# -*- coding: utf-8 -*-

valores = raw_input().split()
valores = list(map(int, valores))

for v in sorted(valores):
    print v

print ''

for v in valores:
    print v