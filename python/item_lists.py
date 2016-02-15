#!/usr/bin/env python
#pylint: disable=invalid-name
"""
This module parses the json files in config/items.

Json files are parsed, and the module is replaced by a dict.
The dict contains the "items", "weapons" and "armors" keys.
The values are lists of item dicts.

Pylint: invalid name is disabled as items/weapons/armors/gems are
changed in a for and shops is the total of all.
"""

import json
import sys

items = []
weapons = []
armors = []
gems = []

# parse the json files
with open("config/items/item_list.json", "r") as f:
    for item in json.load(f):
        # tag it ro recognize it after
        item["type"] = "item"
        # add it to the shop
        items.append(item)

with open("config/items/weapon_list.json", "r") as f:
    for weapon in json.load(f):
        weapon["type"] = "equipment"
        # this is not defined before for a better looking json
        weapon["slot"] = "weapon"
        # already inserted items
        weapon["gems"] = []
        weapons.append(weapon)

with open("config/items/armor_list.json", "r") as f:
    for equip in json.load(f):
        equip["type"] = "equipment"
        equip["gems"] = []
        armors.append(equip)

with open("config/items/gem_list.json", "r") as f:
	for gem in json.load(f):
		gem["type"] = "gem"
		gems.append(gem)

shops = {
    "items": items,
    "weapons": weapons,
    "armors": armors,
    "gems": gems
}

sys.modules[__name__] = shops
