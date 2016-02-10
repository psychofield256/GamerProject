#!/usr/bin/env python

"""Module containing the Item, Equipment, and Potion classes."""


class Item(object):
    """Class used to create items. Takes a dict defined in items.py."""

    def __init__(self, src, jewel=False):
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
        if jewel:
            # creates the stats dict
            self.stats = {}
            self.takestats(src)
            # erases the old value
            self.itemtype = "jewel"

    def saystats(self):
        """
        Function for returning the stats of the item.

        If the item don't have any, it will just stop.
        """
        var = ""
        # if the item doesn't have stats
        if not hasattr(self, "stats"):
            return

        for i, stat in enumerate(self.stats.keys()):
            # if i is a multiple of 3, jump a line
            if (i % 3) == 0:
                value = str(self.stats[stat])
                var += "\n{}: {}".format(stat, value)
            else:
                value = str(self.stats[stat])
                var += " {}: {}".format(stat, value)
        return var

    def takestats(self, args):
        """
        Function for taking the stats from the dict used in creation.

        If the item is not a jewel or an equipment,
        it will stop before making errors.
        """
        if self.itemtype == "item":
            return
        for stat in args.stats.keys():
            self.stats[stat] = args[stat]

    def __str__(self):
        """Method returning an str version of the instance."""
        var = ""
        i = self.infos
        var += "name: " + i["name"] + "\n"
        var += "lore: " + i["lore"] + "\n"
        var += "lvl: " + str(i["lvl"]) + "\n"
        var += "weight: " + str(i["weight"]) + "\n"

        # if it's a jewel, say it's insertable and its stats
        if self.itemtype == "jewel":
            var += "\n" + "insertable"
            # add the stats to var
            var += self.saystats()
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
