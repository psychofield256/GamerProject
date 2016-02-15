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

# create the shops
item_shop = []
weapon_shop = []
armor_shop = []

# parse the json files
with open("config/town/item_shop.json", "r") as f:
    for item in json.load(f):
        # tag it ro recognize it after
        item["type"] = "item"
        # add it to the shop
        item_shop.append(item)

with open("config/town/weapon_shop.json", "r") as f:
    for weapon in json.load(f):
        weapon["type"] = "equipment"
        # this is not defined before for a better looking json
        weapon["slot"] = "weapon"
        # already inserted items
        weapon["inserted"] = []
        weapon_shop.append(weapon)

with open("config/town/armor_shop.json", "r") as f:
    for equip in json.load(f):
        equip["type"] = "equipment"
        equip["inserted"] = []
        armor_shop.append(equip)

shops = {
    "items": item_shop,
    "weapons": weapon_shop,
    "armors": armor_shop
}

sys.modules[__name__] = shops
