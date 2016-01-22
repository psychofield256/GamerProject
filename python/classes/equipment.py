#!/usr/bin/env python
# -*- coding:utf-8 -*-

from classes.item import Item


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
        self.emptySlots = args["emptySlots"]
        # the items inserted (used for removing)
        self.usedSlots = []

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
        #todo
        self.emptySlots -= 1
        self.usedSlots.append(item)
        self.str += item.str
        self.dex += item.dex
        self.vit += item.vit
        self.int += item.int
        self.wis += item.wis
        self.luk += item.luk
    def remove(self, number):
        """function for removing a jewel from self
        add 1 to the index for easier use"""
        toRemove = self.usedSlots[number+1]
        self.str -= item.str
        self.dex -= item.dex
        self.vit -= item.vit
        self.int -= item.int
        self.wis -= item.wis
        self.luk -= item.luk
        del self.usedSlots[number+1]
