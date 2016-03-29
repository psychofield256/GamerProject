"""
This module contains code about items of the game.

You can import:
-shops (dict)
-lists (dict)

-Functions:
--item_to_str(item: dict) --> str
--socket(item: dict, gem: dict) (not implemented)
(Other functions are just local ones and useless for the rest of the program)
"""

import json

from constants import *
# import sys

# game functions


def stats_to_str(item):
    """
    Return the stats of the item in a str.

    The difference between basic and added stats is already implemented,
    but commented out because added stats are still not implemented.
    """
    var = "stats:\n"
    # sort basic and added stats in tuples
    basic_stats = []
    added_stats = []
    for stat, value in item["stats"].items():
        if stat in BASIC_STATS:
            basic_stats.append((stat, value))
        else:
            added_stats.append((stat, value))

    # add them in the good order
    for stat, value in basic_stats:
        var += "\t%s: %s\n" % (stat, value)
    var += "\n"
    for stat, value in added_stats:
        var += "\t%s: %s\n" % (stat, value)
    return var


def gem_names(item):
    """Return the names of the gems in a str."""
    var = "gems:\n"
    for gem in item["gems"]:
        var += "\t%s: %s\n" % (gem["name"])
    return var


def item_to_str(item):
    """
    Function used to convert a dict item into an str.

    Equivalent to __str__(self), but a class isn't used.
    This is to avoid making a class with only
    a __str__ function and use inheritance.
    """
    var = ""
    first_values = []
    second_values = []

    if item is None:
        return var

    for key, value in item.items():
        if key in ITEM_INFOS:
            first_values.append((key, value))
        else:
            second_values.append((key, value))
    for key, value in first_values:
        var += "%s: %s\n" % (key, str(value))
    for key, value in second_values:
        var += "%s: %s\n" % (key, str(value))

    if item["type"] == "equipment":
        for key in EQUIPMENT_INFOS:
            var += "%s: %s\n" % (key, str(item[key]))
        var += stats_to_str(item)
        if item["gems"] != []:
            var += gem_names(item)
    elif item["type"] == "gem":
        var += stats_to_str(item)

    return var

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
