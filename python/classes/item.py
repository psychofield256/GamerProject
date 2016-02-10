#!/usr/bin/env python

"""Module containing the Item, Equipment, and Potion classes."""


class Item(object):
    """Class used to create items. Takes a dict defined in items.py."""

    def __init__(self, src):
        """
        Unpack the source dict into the item's infos attribute.

        jewel is used for applying different process on them, by
        giving it the stats
        """
        # unpack the src dict's informations
        self.infos = {}
        for info in ["name", "lore", "lvl", "weight"]:
            self.infos[info] = src[info]

        # saves the source dict (used for recognizing the item)
        self.src = src
        self.itemtype = "item"

        # used for recognizing jewels
        """
        if False:
            # creates the stats dict
            self.stats = {}
            self.takestats(src)
            # erases the old value
            self.itemtype = "jewel"
        """

    def __str__(self):
        """Method returning an str version of the instance."""
        var = ""
        i = self.infos
        var += "name: " + i["name"] + "\n"
        var += "lore: " + i["lore"] + "\n"
        var += "lvl: " + str(i["lvl"]) + "\n"
        var += "weight: " + str(i["weight"]) + "\n"
        return var

    def __eq__(self, other):
        """
        Method returning True or False in an equallity.

        If the other is None, it's always False.
        """
        # if the other item is just void, return false.
        # else, if they have the same source dict, they're equal
        if other is None:
            return False
        return self.src == other.src


class Jewel(Item):
    """
    Class for Jewel.

    A jewel is an item, but it can be inserted in an equipment,
    and it has got stats.
    """

    def __init__(self, src):
        Item.__init__(self)
        self.stats = {}
        for key, value in src["stats"].items():
            self.stats[key] = value
        self.itemtype = "jewel"

    def __str__(self):
        """Method returning an str version of the instance.

        Call super(), and add "insertable" and the stats"""
        var = Item.__str__(self)
        var += "\ninsertable" + "\nstats:"
        # add the stats to var
        for stat, value in self.stats.items():
            var += "\n"
            var += "%s: %d" % stat, value
        return var
