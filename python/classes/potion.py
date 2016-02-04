#!/usr/bin/env python
# pylint: disable=super-init-not-called

"""
Module containing the Potion class

Potion.itemtype (str): "potion"
Potion.potiontype (str): the potion type ("life" or "mana")
Potion.regen (int): the regeneration when drank
Potion.infos (dict):
    name (str): its name
    lore (str): its lore
    lvl (int): the level of the item
    weight (int): the weight (0.1 for a potion)
"""

try:
    from classes.item import Item
except ImportError:
    from item import Item


class Potion(Item):
    """Class used to create life/mana potions.

    takes an int level and an str type ("Life" or Mana") that is
    "Life" by default.
    So you just need to do Potion(3) for a lvl 3 life potion,
    and Potion(2, "Mana") for a lvl 2 mana potion"""

    def __init__(self, lvl, potiontype="Life"):
        """The construction doesn't call
        Item.__init__ because no dict is used"""
        self.itemtype = "potion"
        self.potiontype = potiontype.lower()
        self.regen = lvl * 200
        self.infos = {
            "name": potiontype + " Potion lvl " + str(lvl),
            "lore": "A magic beverage that instantly regenerates your " +
                    self.potiontype + " from " + str(self.regen) + " points.",
            "lvl": lvl,
            "weight": 0.1,
        }
