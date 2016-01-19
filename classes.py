#!/usr/bin/env python
# -*- coding:utf-8 -*-

#todo
#not necessary for now
#from abc import ABCMeta, abstractmethod

#next commit:
#no more id needed
#inventory works!
#no more ugly "insertable": False on equipment

class Inventory:
	"""Class used to create the inventory of entities
	takes:
	-every Item you want (or a tuple)
	-the four Equipment (helmet, chestplate, leggings, boots, weapon)"""
	def __init__(self, items, helmet=None, chestplate=None, leggings = None, boots = None, weapon=None):
		self.items = []
		self.equipments = []
		for item in items:
			#todo add equipments
			#if the item is an equipment, add it to equipments
			if item.iType == "equipment":
				self.equipments.append(item)
			#else, add it to items
			else:
				self.items.append(item)
		self.equips = {"helmet": helmet, "chestplate": chestplate,
		"leggings": leggings, "boots": boots, "weapon": weapon}
		#self.helmet = helmet
		#self.chestplate = chestplate
		#self.leggings = leggings
		#self.boots = boots
		#self.weapon = weapon
		
	def sayItems(self):
		for item in self.items:
			yield item
	def sayEquipment(self):
		#for equip in self.equips.values():
		#	yield equip
		return self.equips["weapon"], self.equips["helmet"], self.equips["chestplate"],
		self.equips["leggings"], self.equips["boots"]
	def add(self, item):
		self.items.append(item)
	def equip(self, equipPosition):
		"""Method for equipping an equipment in the inventory to the corresponding slot
		and unequipping the old one"""
		try:
			#takes the equipment to equip
			item = self.equipments[equipPosition]
			#unequip the slot of the item to equîp
			self.unequip(item.slot)
			#copy the new one in the equipment and delete the old one
			self.equips[item.slot] = item
			del self.equipments[equipPosition]
		except AttributeError:
			print("this is not an equipment!")

	def unequip(self, slot):
		#check if the actual equipment is not None.
		#Then, take the item in the slot selected and copy it to the inventory.
		#then, delete it
		#if it was None, don't do anything, because equip will replace it when there will be something
		if self.equips[slot] != None:
			self.add(self.equips[slot])
			del self.equips[slot]


class Item:
	"""Class used to create items.
	takes a dict defined in items.py (there is an example)"""

	def __init__(self, args, jewel=False, equipment=False):
		"""unpack the name, lore and usedIn attributes."""
		self.name, self.lore = args["name"], args["lore"]
		self.usedIn, self.weight = args["usedIn"], args["weight"]
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
		var = self.name + "\n" + self.lore + "\n" + "used in: " + self.usedIn + "\n" + (str(self.weight)) + "kg"
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
		return self.src == other.src


class Equipment(Item):
	"""Class used to create equipments.
	takes a dict, as Item, but with the slot, the type, the emplySlots and every stat boost defined in.
	for example, see in items.py, at equip"""

	def __init__(self, args):
		"""Will call the mother constructor to set the general attributes.
		Then, saves other caracteristics"""
		Item.__init__(self, args)
		#saves the stat boost
		self.takeStats(args)
		#the slot used (weapon, helmet,...) and the type (axe, sword, bow,...)
		self.slot, self.type, self.lvl = args["slot"], args["type"], args["lvl"]
		#the itemType can be "jewel", "equipment" or "item"
		self.iType = "equipment"
		#the number of items that can be inserted
		self.emptySlots = args["emptySlots"]
		#the items inserted (used for removing)
		self.usedSlots = []
	def __str__(self):
		"""#take the Item __str__ function, and add the equipment caracteristics"""
		var = Item.__str__(self)
		var += "\n" + "equipment"
		var += self.sayStats()
		return var

	def insert(self, item):
		#todo
		try:
			something
		except:
			pass



class Potion(Item):
	"""Class used to create life/mana potions.
	takes an int level and an str type ("Life" or Mana") that is "Life" by default.
	So you just need to do Potion(3) for a lvl 3 life potion,
	and Potion(2, "Mana") for a lvl 2 mana potion"""
	
	def __init__(self, lvl, ptype="Life"):
		self.name  = ptype + " Potion lvl " + str(lvl)
		self.id = ptype + "Potion" + str(lvl) #e.g: "LifePotion2"
		self.lvl = lvl
		self.regen = lvl * 200
		self.type = ptype.lower()
		self.lore = "A magic beverage that instantly regenerates your " + self.type + " from " + str(self.regen) + " points "
		self.weight = 0.1
		self.usedIn = "Nothing"

class ToInsert(Item):
	"""Class for items that can be inserted
	takes the same args than Item, and:
	-6 int stats (str, dex, vit, int, wis, luk)"""