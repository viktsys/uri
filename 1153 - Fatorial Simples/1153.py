# -*- coding: utf-8 -*-

def fat(n):
  if(n == 1):
    return 1;
  else:
    return n * fat(n - 1)

i = int(input())
print(fat(i))
