#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This file contains all the informations about items.

Ordinary items are in the items list, jewels are in the jewels list, and
equipments are in the equipments list
"""

ITEMS = [
    # example
    {
        "name": "item name",
        "lore": "description",
        "weight": 1,
    },

]

JEWELS = [
    # jewel example
    {
        "name": "jewel test",
        "lore": "A jewel that can decorate an equipment",
        "weight": 1,
        "str": 300, "dex": 300, "vit": 300,
        "int": 300, "wis": 300, "luk": 300
    }
]

EQUIPMENTS = [
    # example
    {
        "name": "Example Sword",
        "lore": "description",
        "lvl": 1,
        "weight": 10,
        "emptySlots": 1,
        # emptySlots if for inserting items, which provide stat boosts
        "slot": "weapon",  # weapon, helmet, chestplate, leggings or boots
        "type": "sword",  # sword, axe, bow...
        "str": 100, "dex": 100, "vit": 100,
        "int": 100, "wis": 100, "luk": 100
    }, {
        "name": "sword of devil",
        "lore": "the sword left by the blue demon",
        "lvl": 10,
        "weight": 10,
        "emptySlots": 2,
        "slot": "weapon",
        "type": "sword",
        "str": 10, "dex": 15, "vit": 10,
        "int": 0, "wis": 0, "luk": 0
    }, {
        "name": "wooden stick",
        "lore": "a wooden stick you \"borrowed\" at someone you didn't know",
        "lvl": 1,
        "weight": 12,
        "insertable": False,
        "emptySlots": 0,
        "slot": "weapon",
        "type": "sword",
        "str": 5, "dex": 0, "vit": 0,
        "int": 0, "wis": 0, "luk": 0
    }, {
        "name": "test chestplate",
        "lore": "a wonderful cheat armor",
        "lvl": 1,
        "weight": 0,
        "emptySlots": 5,
        "slot": "chestplate",
        "type": "LightArmor",
        "str": 500, "dex": 500, "vit": 500,
        "int": 500, "wis": 500, "luk": 500
    }, {
        "name": "helmet",
        "lore": "cheat test helmet",
        "lvl": 1,
        "weight": 0,
        "emptySlots": 4,
        "slot": "helmet",
        "type": "LightArmor",
        "str": 500, "dex": 500, "vit": 500,
        "int": 500, "wis": 500, "luk": 500
    }
]
