#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Module containing the Item class.
"""


class Item(object):
    """Class used to create items.
    takes a dict defined in items.py (there is an example)"""

    def __init__(self, args, jewel=False):
        """unpack the name, lore and other attributes."""
        self.name, self.lore = args["name"], args["lore"]
        self.weight = args["weight"]
        # saves the source dict used for defining the item
        self.src = args
        self.stats = {}
        # used for recognizing jewels
        if jewel:
            self.take_stats(args)
            self.item_type = "jewel"
        else:
            self.item_type = "item"

    def take_stats(self, args):
        """function for taking the str, dex, vit, int, wis and luk
        from the dict used for creating the item"""
        stat_list = ["str", "dex", "vit", "int", "wis", "luk"]
        for stat in stat_list:
            self.stats[stat] = args[stat]
        # self.str, self.dex, self.vit = args["str"], args["dex"], args["vit"]
        # self.int, self.wis, self.luk = args["int"], args["wis"], args["luk"]

    def __str__(self):
        var = self.name + "\n" + self.lore + "\n" + (str(self.weight)) + "kg"
        # if jewel
        if self.item_type == "jewel":
            var += "\n" + "insertable"
            # add the stats to var
            var += self.say_stats()
        return var

    def say_stats(self):
        """
        function for returning the stats of the item.

        If the item don't have any, pass because
        it will not be used"""
        var = ""
        stat_list = ["str", "dex", "vit", "int", "wis", "luk"]
        for i, stat in enumerate(stat_list):
            # if i is a multiple of 3
            if (i % 3) == 0:
                value = str(self.stats[stat])
                var += "\n{}: {}".format(stat, value)
            else:
                value = str(self.stats[stat])
                var += " {}: {}".format(stat, value)
        return var

    def __eq__(self, other):
        # if the other item is just void, return false.
        # else, if they have the same source dict, they're equal
        if other is None:
            return False
        return self.src == other.src
