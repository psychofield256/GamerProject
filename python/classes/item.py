#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Module containing the Item class.
"""


class Item(object):
    """Class used to create items.
    takes a dict defined in items.py"""

    def __init__(self, src, jewel=False):
        """unpack the src dict values into the item's infos attribute.
        jewel is used for applying different process on them"""

        # unpack the src dict's informations
        self.infos = {}
        for info in ["name", "lore", "lvl", "weight"]:
            self.infos[info] = src[info]

        # saves the source dict (used for recognizing the item)
        self.src = src

        # creates the stats dict (deleted if useless)
        self.stats = {}
        # used for recognizing jewels
        if jewel:
            self.take_stats(src)
            self.item_type = "jewel"
        else:
            self.item_type = "item"
            del self.stats

    def say_stats(self):
        """
        function for returning the stats of the item.
        If the item don't have any, pass because
        it will not be used"""
        var = ""
        for i, stat in enumerate(self.stats.keys()):
            # if i is a multiple of 3
            if (i % 3) == 0:
                value = str(self.stats[stat])
                var += "\n{}: {}".format(stat, value)
            else:
                value = str(self.stats[stat])
                var += " {}: {}".format(stat, value)
        return var

    def take_stats(self, args):
        """function for taking the stats from the dict used
        to create the item"""
        for stat in args.stats.keys():
            self.stats[stat] = args[stat]

    def __str__(self):
        var = ""
        for info in self.infos.keys():
            var += info + ": " + self.infos[info]
        # var = self.name + "\n" + self.lore +
        # "\n" + (str(self.weight)) + "kg"
        # if jewel
        if self.item_type == "jewel":
            var += "\n" + "insertable"
            # add the stats to var
            var += self.say_stats()
        return var

    def __eq__(self, other):
        # if the other item is just void, return false.
        # else, if they have the same source dict, they're equal
        if other is None:
            return False
        return self.src == other.src
