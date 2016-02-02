#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This file contains all the informations about items.

Ordinary items are in the items list, jewels are in the jewels list, and
equipments are in the equipments list
"""

# to define an item, you need to give it the following attributes:
# -name (str): its name
# -lore (str): its lore
# -lvl (int): the required level to equip it
# -weight (int): the free space required to take it in the inventory

ITEMS = [
    # example
    {
        "name": "item name",
        "lore": "description",
        "weight": 1,
        "lvl": 1
    },

]

# to define a jewel, you need to give it the following attributes:
# -name (str): its name
# -lore (str): its lore
# -lvl (int): the required level to equip it
# -weight (int): the free space required to take it in the inventory
# -stats (dict), which contains:
#   -str (int): the strenght added when equipped
#   -dex (int): the dexterity added when equipped
#   -vit (int): the vitality added when equipped
#   -int (int): the intelligence added when equipped
#   -wis (int): the wisdom added when equipped
#   -luk (int): the luck added when equipped

JEWELS = [
    # jewel example
    {
        "name": "jewel test",
        "lore": "A jewel that can decorate an equipment",
        "lvl": 1,
        "weight": 1,
        "stats": {
            "str": 300, "dex": 300, "vit": 300,
            "int": 300, "wis": 300, "luk": 300
        }
    }
]

# to define an equipment, you need to give it the following attributes:
# -name (str): its name
# -lore (str): its lore
# -lvl (int): the required level to equip it
# -weight (int): the free space required to take it in the inventory
# -slot (str): the slot used in the character's equipment. It can be:
#   -"weapon"
#   -"helmet"
#   -"chestplate"
#   -"leggings"
#   -"boots"
# -emptyslots: for inserting jewels, which provide stat boosts
# -stats (dict), which contains:
#   -str (int): the strenght added when equipped
#   -dex (int): the dexterity added when equipped
#   -vit (int): the vitality added when equipped
#   -int (int): the intelligence added when equipped
#   -wis (int): the wisdom added when equipped
#   -luk (int): the luck added when equipped

EQUIPMENTS = [
    # example
    {
        "name": "Example Sword",
        "lore": "description",
        "lvl": 1,
        "weight": 10,
        "slot": "weapon",  # weapon, helmet, chestplate, leggings or boots
        "emptyslots": 1,
        "stats": {
            "str": 100, "dex": 100, "vit": 100,
            "int": 100, "wis": 100, "luk": 100
        }
    }, {
        "name": "sword of devil",
        "lore": "the sword left by the blue demon",
        "lvl": 10,
        "weight": 10,
        "emptyslots": 2,
        "slot": "weapon",
        "type": "sword",
        "stats": {
            "str": 10, "dex": 15, "vit": 10,
            "int": 0, "wis": 0, "luk": 0
        }
    }, {
        "name": "wooden stick",
        "lore": "a wooden stick you \"borrowed\" at someone you didn't know",
        "lvl": 1,
        "weight": 12,
        "insertable": False,
        "emptyslots": 0,
        "slot": "weapon",
        "type": "sword",
        "stats": {
            "str": 5, "dex": 0, "vit": 0,
            "int": 0, "wis": 0, "luk": 0
        }
    }, {
        "name": "test chestplate",
        "lore": "a wonderful cheat armor",
        "lvl": 1,
        "weight": 0,
        "emptyslots": 5,
        "slot": "chestplate",
        "type": "LightArmor",
        "stats": {
            "str": 500, "dex": 500, "vit": 500,
            "int": 500, "wis": 500, "luk": 500
        }
    }, {
        "name": "helmet",
        "lore": "cheat test helmet",
        "lvl": 1,
        "weight": 0,
        "emptyslots": 4,
        "slot": "helmet",
        "type": "LightArmor",
        "stats": {
            "str": 500, "dex": 500, "vit": 500,
            "int": 500, "wis": 500, "luk": 500
        }
    }
]
