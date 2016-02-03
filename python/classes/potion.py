#!/usr/bin/env python
# -*- coding:utf-8 -*-
# pylint: disable=super-init-not-called
"""
Module containing the Potion class
"""


# from classes.item import Item
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
        self.regen = lvl * 200,
        self.infos = {
            "name": potiontype + " Potion lvl " + str(lvl),
            "lore": "A magic beverage that instantly regenerates your " +
                    self.itemtype + " from " + str(self.regen) + " points ",
            "lvl": lvl,
            "weight": 0.1,
        }
