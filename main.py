#!/usr/bin/env python
#-*-encoding:utf-8-*-

from classes import *
from items import items, equipments, jewels
itemList = []
for item in items:
	#creates an Item object and store it in itemList
	itemList.append(Item(item))
equipList = []
for equip in equipments:
	#same for Equipment instances
	equipList.append(Equipment(equip))
for jewel in jewels:
	itemList.append(Item(jewel, jewel=True))

l = itemList + equipList

i = Inventory(l)

for item in equipList:
	i.add(item)
for item in itemList:
	i.add(item)

#i.equip(4)
i.equip(0)
i.equip(2)
i.equip(2)
#i.equip(1)
for item in i.sayItems():
	print(item, "\n")
for equip in i.sayEquipment():
	print(equip, "\n")