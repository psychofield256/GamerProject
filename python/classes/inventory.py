#!/usr/bin/env python

import sys
import os

# from . import constants
# import constants as c
from constants import *


class Inventory:
    """
    Class used to create the inventory of entities
    takes:
    -(optionnal) An Item list
    -(optionnal) An unepacked equipment dict (see the doc)
    You can make a dict first and use **<dict>, or use a
    826 characters line. I recommand to unpack the dict.
    """

    def __init__(self, items=None, **equipments):
        if not items:
            items = []
        # creates an empty equipment dict and fill it with the args
        self.equipment = EMPTY_EQUIPMENT
        self.equipment.update(equipments)
        # creates the different sections of the inventory
        self.items = []
        self.equipments = []
        self.potions = []
        self.gems = []
        self.consumables = []

    def add(self, item):
        """Add the item to the section corresponding to its type."""
        t = item["type"]
        if t == "equipment":
            self.equipments.append(item)
        elif t == "potion":
            self.potions.append(item)
        elif t == "gem":
            self.gems.append(item)
        elif t == "item":
            self.items.append(item)
        elif t == "consumable":
            self.consumables.append(item)

        # this is a dictionnary mapping
        # to test. Before, I need to use the previous code
        # to make it work.
        # switch = {
        #    "equipment": lambda: self.equipment.append(item),
        #    "potion": lambda: self.equipment.append(item),
        #    "gem": lambda: self.equipment.append(item),
        #    "item": lambda: self.equipment.append(item),
        # }
        # return switch.get(item["type"])

    def equip(self, position):
        """
        Method for equipping an equipment in the inventory to the corresponding slot
        and unequipping the old one.
        Take the equipment position in the equipments section.
        """
        try:
            # takes the equipment to equip
            equip = self.equipments[position]
            # unequip the slot of the item to equip
            self.unequip(equip["slot"])
            # copy the new one in the equipment and delete the old one
            self.equipment[equip["slot"]] = equip
            del self.equipments[position]
        # if the equipment doesn't have the attributes of an equipment,
        # it's not one
        except AttributeError:
            print("this is not an equipment!")

    def unequip(self, slot):
        """
        Method for unnequipping the slot selected.
        Takes a str which can be "weapon",
        "helmet", "chestplate", "leggings" or "boots"
        """
        # check if the actual equipment is not None.
        # Then, take the item in the slot selected and copy it to the inventory.
        # then, replace it with None
        # if it was None, don't do anything, because equip will replace it when
        # there will be something
        try:
            if self.equipment[slot] != None:
                self.add(self.equipment[slot])
                self.equipment[slot] = None
        # if the slot is not one in the list
        except KeyError:
            print("this slot doesn't exist")
