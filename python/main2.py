#!usr/bin/env python

"""
Game made by psychofield.

Its objectives are to adapt the manga "The Gamer" as a real rpg.
"""

import json

with open("config/town/weapon_shop.json", "r") as f:
	weapons = json.load(f)

print(weapons)
