#!/usr/bin/env python
"""
This module contains the parsed jsons.

It contains the bunches for items.
"""

import json
from bunch import Bunch

import constants as c
from functions.display import new_bunch_str as n

# redefines Bunch.__str__ (in order not to create a new class for this)
Bunch.__str__ = n

item_shop = []
weapon_shop = []
armor_shop = []

with open("config/town/items.json", "r") as f:
	for item in json.load(f):
		# unpack the dict to make a Bunch
		item = Bunch(**item)
		# tag it ro recognize it after
		item.type = "item"
		# add it to the shop
		item_shop.append(item)

