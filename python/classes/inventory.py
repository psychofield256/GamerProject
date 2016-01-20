#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Inventory:
    """Class used to create the inventory of entities
    takes:
    -every Item you want (or a tuple)
    -the four Equipment (helmet, chestplate, leggings, boots, weapon)"""
    def __init__(self, items=[], helmet=None, chestplate=None, leggings = None, boots = None, weapon=None):
        self.items = []
        self.equipments = []
        self.potions = []
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
        #self.helmet = helmet
        #self.chestplate = chestplate
        #self.leggings = leggings
        #self.boots = boots
        #self.weapon = weapon
        
    def sayItems(self):
        for item in self.items:
            yield item
    def sayEquipments(self):
        """yield the equipments stored"""
        for equip in self.equipments:
            yield equip
    def saySlots(self):
        #for equip in self.slots.values():
        #   yield equip
        yield self.slots["weapon"]
        yield self.slots["helmet"]
        yield self.slots["chestplate"]
        yield self.slots["leggings"]
        yield self.slots["boots"]
        #return self.slots["weapon"], self.slots["helmet"], self.slots["chestplate"],
        #self.slots["leggings"], self.slots["boots"]
    def sayPotions(self):
        for p in self.potions:
            yield p
    def add(self, item):
        if item.iType == "equipment":
            self.equipments.append(item)
        elif item.iType == "potion":
            self.potions.append(item)
        elif item.iType == "item" or item.iType == "jewel":
            self.items.append(item)
    def equip(self, position):
        """Method for equipping an equipment in the inventory to the corresponding slot
        and unequipping the old one"""
        try:
            #takes the equipment to equip
            equip = self.equipments[position]
            #unequip the slot of the item to equîp
            self.unequip(equip.slot)
            #copy the new one in the equipment and delete the old one
            self.slots[equip.slot] = equip
            del self.equipments[position]
        except AttributeError:
            print("this is not an equipment!")

    def unequip(self, slot):
        #check if the actual equipment is not None.
        #Then, take the item in the slot selected and copy it to the inventory.
        #then, replace it with None
        #if it was None, don't do anything, because equip will replace it when there will be something
        if self.slots[slot] != None:
            self.add(self.slots[slot])
            self.slots[slot] = None