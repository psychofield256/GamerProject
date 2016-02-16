#!/usr/bin/env python

import sys
import os

import constants as c


class Inventory:
    """
    Class used to create the inventory of entities
    takes:
    -(optionnal) An Item list
    -(optionnal) An unepacked equipment dict (see the doc)
    You can make a dict first and use **<dict>, or use a
    826 characters line. I recommand to unpack the dict.
    """
    def __init__(self, items=[], **equipments):
        # creates the equipment dict
        self.equipment = c.empty_equipment_dict
        self.equipment.update(equipments)
        #creates the different sections of the inventory
        self.items = []
        self.equipments = []
        self.potions = []
        self.gems = []
        """
        for item in items:
            #if the item is an equipment, add it to equipments
            if item.iType == "equipment":
                self.equipments.append(item)
            #if it's a potion, it goes in potions
            elif item.iType == "potion":
                self.potions.append(item)
            #else, add it to items
            else:
                self.items.append(item)
        self.slots = {"helmet": helmet, "chestplate": chestplate,
        "leggings": leggings, "boots": boots, "weapon": weapon}
        """
    def sayItems(self):
        """generator returning all the items in the items section"""
        for item in self.items:
            yield item
            
    def sayEquipments(self):
        """generator returning all the items in the equipments section"""
        for equip in self.equipments:
            yield equip
            
    def sayPotions(self):
        """generator returning all the items in the potions section"""
        for p in self.potions:
            yield p
            
    def saySlots(self):
        """
        Return a tuple with the actual equipment:
        1: Weapon, 2: Helmet, 3: Chestplate, 4: Leggings, 5: Boots
        """
        return self.slots["weapon"], self.slots["helmet"], self.slots["chestplate"],
        self.slots["leggings"], self.slots["boots"]
    
    def add(self, item):
        """Add the item given to the section corresponding to its type"""
        if item.iType == "equipment":
            self.equipments.append(item)
        elif item.iType == "potion":
            self.potions.append(item)
        elif item.iType == "item" or item.iType == "jewel":
            self.items.append(item)
    def equip(self, position):
        """
        Method for equipping an equipment in the inventory to the corresponding slot
        and unequipping the old one.
        Take the equipment position in the equipments section.
        """
        try:
            #takes the equipment to equip
            equip = self.equipments[position]
            #unequip the slot of the item to equip
            self.unequip(equip.slot)
            #copy the new one in the equipment and delete the old one
            self.slots[equip.slot] = equip
            del self.equipments[position]
        #if the equipment doesn't have the attributes of an equipment,
        #it's not one
        except AttributeError:
            print("this is not an equipment!")

    def unequip(self, slot):
        """
        Method for unnequipping the slot selected.
        Takes a str which can be "weapon",
        "helmet", "chestplate", "leggings" or "boots"
        """
        #check if the actual equipment is not None.
        #Then, take the item in the slot selected and copy it to the inventory.
        #then, replace it with None
        #if it was None, don't do anything, because equip will replace it when there will be something
        try:
            if self.slots[slot] != None:
                self.add(self.slots[slot])
                self.slots[slot] = None
        #if the slot is not one in the list
        except KeyError:
            print("this slot doesn't exist")
        