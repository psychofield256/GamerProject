#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
module with the class Equipment.
"""

from item import Item


class Equipment(Item):
    """Class used to create equipments.

    Takes a dict, as Item, but with more attributes (explained in items.py).
    for example, see in items.py, at equip"""

    def __init__(self, args):
        """Will call the mother constructor to set the general attributes.
        Then, saves other caracteristics"""
        Item.__init__(self, args)
        # saves the stat boost
        self.takeStats(args)
        # the slot used (weapon, helmet,...) and the type (axe, sword, bow,...)
        self.slot = args["slot"]
        self.type = args["type"]
        self.lvl = args["lvl"]
        # the itemType can be "jewel", "equipment" or "item"
        self.iType = "equipment"
        # the number of items that can be inserted
        self.empty_slots = args["emptySlots"]
        # the items inserted (used for removing)
        self.used_slots = []

    def __str__(self):
        """
        return a paragraph describing the equipment.

        take the Item.__str__ function, and add the equipment caracteristics
        """
        var = Item.__str__(self)
        var += "\n" + "equipment"
        var += self.sayStats()
        return var

    def insert(self, item):
        """insert a jewel in the equipment"""
        # todo
        self.empty_slots -= 1
        self.used_slots.append(item)
        self.str += item.str
        self.dex += item.dex
        self.vit += item.vit
        self.int += item.int
        self.wis += item.wis
        self.luk += item.luk

    def remove(self, number):
        """function for removing a jewel from self
        add 1 to the index for easier use"""
        to_remove = self.used_slots[number+1]
        self.str -= to_remove.str
        self.dex -= to_remove.dex
        self.vit -= to_remove.vit
        self.int -= to_remove.int
        self.wis -= to_remove.wis
        self.luk -= to_remove.luk
        del self.used_slots[number+1]
