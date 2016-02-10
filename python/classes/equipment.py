#!/usr/bin/env python

"""module with the class Equipment."""

try:
    from classes.item import Item
except ImportError:
    from item import Item

try:
    from constants import STATLIST, EQUIPGENERALS
except ImportError:
    pass


class Equipment(Item):
    """
    Class used to create equipments.

    Takes a dict, as Item, but with more attributes (explained in items.py).
    for example, see in items.py, at equip.
    """

    def __init__(self, args):
        """Call the mother constructor, and saves specific caracteristics."""
        Item.__init__(self, args)
        # saves the stat boosts in the stats dict
        self.take_stats(args)
        # the slot used (weapon, helmet,...) and the type (axe, sword, bow,...)
        for info in EQUIPGENERALS:
            self.generals[info] = args[info]
        # the itemType can be "jewel", "equipment" or "item"
        self.item_type = "equipment"
        # the items inserted (used for removing)
        self.used_slots = []

    def __str__(self):
        """
        Return a paragraph describing the equipment.

        take the Item.__str__ function, and add the equipment caracteristics.
        """
        var = Item.__str__(self)
        var += "\n" + "equipment"
        var += self.say_stats()
        return var

    def insert(self, item):
        """Insert a jewel in the equipment."""
        # todo
        self.generals["empty_slots"] -= 1
        self.used_slots.append(item)

        for stat in STATLIST:
            self.stats[stat] += item.stats[stat]

    def remove(self, number):
        """
        Function for removing a jewel.

        Add 1 to the index for easier use
        (instead of doing remove(0), you do remove(1)).
        """
        to_remove = self.used_slots[number+1]
        for stat in STATLIST:
            self.stats[stat] -= to_remove.stats[stat]
        del self.used_slots[number+1]
