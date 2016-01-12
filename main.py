#!/usr/bin/env python
#-*-encoding:utf-8-*-

from classes import *
from items import i, t, beginningSword
a = Item(i)
b = Item(t)
c = Equipment(beginningSword)


i = Inventory(a, b, weapon=c)

for item in i.sayItems():
	print(item, "\n")

for equip in i.sayEquipment():
	print(equip, "\n")

if a == b:
	print("yes")
else:
	print("no")
if a == c:
	print("yes")
else:
	print("no")