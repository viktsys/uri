# -*- coding: utf-8 -*-

dilma = []

while True:
  try:
    ent = int(raw_input())
    if ent == 0:
      dilma.append('vai ter copa!')
    if ent >= 1:
      dilma.append('vai ter duas!')
  except:
    break

for txt in dilma:
  print txt