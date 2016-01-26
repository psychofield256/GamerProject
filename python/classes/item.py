#!/usr/bin/env python
# -*- coding:utf-8 -*-
# pylint: disable=E0401,E0602,R0903,W0612

"""
Module containing the Item class.
"""

from constants import STATLIST, GENERALS


class Item(object):
    """Class used to create items.
    takes a dict defined in items.py (there is an example)"""

    def __init__(self, args, jewel=False):
        """unpack the name, lore and other attributes."""
        # generals contains all the general informations like name or lvl
        self.generals = {}
        for info in GENERALS:
            self.generals[info] = args[info]
        # saves the source dict used for defining the item
        self.src = args
        # creates the stats dict (even if not always used after)
        self.stats = {}
        # todo auto recognizing jezels @refactor
        # used for recognizing jewels
        if jewel:
            self.take_stats(args)
            self.item_type = "jewel"
        else:
            self.item_type = "item"

    def take_stats(self, args):
        """function for taking the stats (given in constants.py)
        from the dict used for creating the item"""
        for stat in STATLIST:
            self.stats[stat] = args[stat]

        def __str__(self):
            var = ""
            for info in GENERALS:
                var += info + ": " + self.generals[info]
            # var = self.name + "\n" + self.lore +
            # "\n" + (str(self.weight)) + "kg"
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
            for i, stat in enumerate(STATLIST):
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
