#!/usr/bin/env python
"""
This module contains the parsed jsons.

It contains the bunches for items.
"""

import json
from bunch import Bunch

# import constants as c
from functions.display import new_bunch_str as n

# redefines Bunch.__str__ (in order not to create a new class for this)
Bunch.__str__ = n

item_shop = []
weapon_shop = []
armor_shop = []

with open("config/town/item_shop.json", "r") as f:
    for item in json.load(f):
        # unpack the dict to make a Bunch
        item = Bunch(**item)
        # tag it ro recognize it after
        item.type = "item"
        # add it to the shop
        item_shop.append(item)

with open("config/town/weapon_shop.json", "r") as f:
    for weapon in json.load(f):
        weapon = Bunch(**weapon)
        weapon.type = "equipment"
        weapon_shop.append(weapon)

with open("config/town/armor_shop.json", "r") as f:
    for equip in json.load(f):
        equip = Bunch(**equip)
        equip.type = "equipment"
        armor_shop.append(equip)
