#!/usr/bin/env python
#-*-encoding:utf-8-*-

from classes import *
from items import i, t, equip
a = Item(i)
b = Equipment(equip)
print(b.name)
print(b.lore)
print(b.usedIn)