#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Item:
    """Class used to create items.
    takes a dict defined in items.py (there is an example)"""

    def __init__(self, args, jewel=False):
        """unpack the name, lore and other attributes."""
        self.name, self.lore = args["name"], args["lore"]
        self.weight = args["weight"]
        #saves the source dict used for defining the item
        self.src = args
        #used for recognizing jewels
        if jewel:
            self.takeStats(args)
            self.iType = "jewel"
        else:
            self.iType = "item"

    def takeStats(self, args):
        """function for taking the str, dex, vit, int, wis and luk
        from the dict used for creating the item"""
        self.str, self.dex, self.vit = args["str"], args["dex"], args["vit"]
        self.int, self.wis, self.luk = args["int"], args["wis"], args["luk"]

    def __str__(self):
        var = self.name + "\n" + self.lore + "\n" + (str(self.weight)) + "kg"
        #if jewel
        if self.iType == "jewel":
            var += "\n" + "insertable"
            #add the stats to var
            var += self.sayStats()
        return var
    def sayStats(self):
        """function for returnin the stats of the item. If the item don't have any, pass because
        it will not be used"""
        var = "\n" + "str: " + str(self.str) + " dex: " + str(self.dex) + " vit: " + str(self.vit)
        var += "\n" + "int: " + str(self.int) + " wis: " + str(self.wis) + " luk: " + str(self.luk)
        return var
    
    def __eq__(self, other):
        #if the other item is just void, return false.
        #else, if they have the same source dict, they're equal 
        if other == None:
            return False
        return self.src == other.src