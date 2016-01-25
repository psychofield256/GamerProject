#!/usr/bin/env python
#-*-encoding:utf-8-*-

from classes.item import Item
from classes.equipment import Equipment
from classes.inventory import Inventory
from classes.potion import Potion
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
i = Inventory()

for item in equipList:
	i.add(item)
for item in itemList:
	i.add(item)

a = Potion(4)

i.add(a)

i.equip(4)
i.equip(3)
i.unequip("helmet")

print("-----------------------")
print("actual equipment:")
for equip in i.saySlots():
	print(equip, "\n")
print("-----------------------")
print("equipments:")
for e in i.sayEquipments():
	print(e,"\n")
print("-----------------------------")
print("items:")
for item in i.sayItems():
	print(item, "\n")
print("-----------------------")
print("potions:")
for p in i.sayPotions():
	print(p, "\n")
