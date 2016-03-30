#!usr/bin/env python

"""
Game made by psychofield.

Its objectives are to adapt the manga "The Gamer" as a real rpg.
"""

# import pygame
# import pytmx

from items import shops, item_to_str
from classes.entities import *


def main():
    """test."""
    for item in shops["armors"]:
        print(item_to_str(item))

if __name__ == "__main__":
    main()


"""
for item in shops["items"]:
    print(item_to_str(item))

print("-----------")
print("-----------")
"""
"""
for weapon in shops["weapons"]:
    inv.add(weapon)

for armor in shops["armors"]:
    inv.add(armor)

for gem in shops["gems"]:
    # print(item_to_str(gem))
    inv.add(gem)

inv.equip(0)

for equip in inv.equipments:
    print(item_to_str(equip))

print("-----------")
print("-----------")

for slot, equip in inv.equipment.items():
    print("%s:\n%s" % (slot, item_to_str(equip)))
"""
