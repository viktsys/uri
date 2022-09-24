# -*- coding: utf-8 -*-

resp = []

n = int(raw_input())

for i in range(n):
    x = raw_input()
    r1, r2 = map(int,x.split())
    resp.append(r1 + r2)

for r in resp:
  print r