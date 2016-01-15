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

d = Potion(3)
print(d)