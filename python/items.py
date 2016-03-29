"""
This module contains code about items of the game.

You can import:
-shops (dict dict)
-lists (list dict)

-Functions:
--item_to_str(item: dict) --> str
--socket(item: dict, gem: dict)

"""

import json
# import sys

# game items
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

lists = {
    "items": items,
    "weapons": weapons,
    "armors": armors,
    "gems": gems
}


# town shops
items = []
weapons = []
armors = []
gems = []

with open("config/town/item_shop.json") as f:
    for index in json.load(f):
        # add the item at the index in the item list
        items.append(lists["items"][index])

with open("config/town/weapon_shop.json") as f:
    for index in json.load(f):
        weapons.append(lists["weapons"][index])

with open("config/town/armor_shop.json") as f:
    for index in json.load(f):
        armors.append(lists["armors"][index])

with open("config/town/gem_shop.json") as f:
    for index in json.load(f):
        gems.append(lists["gems"][index])

shops = {
    "items": items,
    "armors": armors,
    "weapons": weapons,
    "gems": gems
}
