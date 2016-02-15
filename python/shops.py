#!/usr/bin/env python
# pylint: disable=invalid-name
"""
This module contains the shops of the game.

Json files are parsed, and the module is replaced by a dict.
The dict contains the "items", "weapons" and "armors" keys.
The values are lists of item dicts.

(pylint) invalid-name is disabled because the lists append
for every item (they're not constants)
"""

import json
import sys

# import constants as c
import item_lists as lists

items = []

with open("config/town/item_shop.json") as f:
    for index in json.load(f):
        items.append(lists["items"][index])

with open("config/town/weapon_shop.json") as f:
    for index in json.load(f):
        weapons.append(lists["weapons"][index])

with open("config/town/armor_shop.json") as f:
    for index in json.load(f):
        weapons.append(lists["armors"][index])

with open("config/town/gem_shop.json") as f:
    for index in json.load(f):
        weapons.append(lists["gems"][index])

shops = {
    "items": items,
    "armors": armors,
    "weapons": weapons,
    "gems": gems
}

sys.modules[__name__] = shops
