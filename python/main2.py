#!usr/bin/env python

"""
Game made by psychofield.

Its objectives are to adapt the manga "The Gamer" as a real rpg.
"""

import json
from bunch import Bunch

import constants as c
from functions.display import new_bunch_str as n

# redefine Bunch.__str__()
Bunch.__str__ = n

weapon_shop = []

with open("config/town/weapon_shop.json", "r") as f:
	for weapon in json.load(f):
		weapon = Bunch(**weapon)
		weapon.type = "weapon"
		weapon_shop.append(weapon)


for weapon in weapon_shop:
	print("---------------")
	print(weapon)
