#!usr/bin/env python

"""
Game made by psychofield.

Its objectives are to adapt the manga "The Gamer" as a real rpg.
"""

# import json

# from functions.display import new_bunch_str as n

# import constants as c
import shops
from functions.items import item_to_str

for item in shops["items"]:
	print(item_to_str(item))

print("-----------")
print("-----------")

for weapon in shops["weapons"]:
	print(item_to_str(weapon))

print("-----------")
print("-----------")

for armor in shops["armors"]:
	print(item_to_str(armor))

print("-----------")
print("-----------")

for gem in shops["gems"]:
	print(item_to_str(gem))