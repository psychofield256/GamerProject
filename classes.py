#!/usr/bin/env python
# -*- coding:utf-8 -*-

#todo
#not necessary for now
#from abc import ABCMeta, abstractmethod


class Inventory:
	"""Class used to create the inventory of entities
	takes:
	-every Item you want (or a tuple)
	-the four Equipment (helmet, chestplate, leggings, boots, weapon)"""
	def __init__(self, *items, helmet=None, chestplate=None, leggings = None, boots = None, weapon=None):
		self.items = []
		for item in items:
			self.items.append(item)
		self.equipments = {"helmet": helmet, "chestplate": chestplate,
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
		for equip in self.equipments.values():
			yield equip
		#yield self.helmet, self.chestplate, self.leggings, self.boots, self.weapon

class Item:
	"""Class used to create items.
	takes a dict with:
	-an str name
	-an str lore (use None if you don't want)
	-an str usedIn (same as above)
	-an str id (necessary)
	-an int weight"""

	def __init__(self, args):
		"""unpack the name, lore and usedIn attributes."""
		self.name, self.id, self.lore = args["name"], args["id"], args["lore"]
		self.usedIn, self.weight = args["usedIn"], args["weight"]

	def __str__(self):
		return self.name + "\n" + self.lore + "\n" + "used in: " +self.usedIn

	def __eq__(self, other):
		return self.id == other.id


class Equipment(Item):
	"""Class used to create equipments.
	takes a dict, as Item, but with the slot, the type, the emplySlots and every stat boost defined in.
	for example, see in items.py, at equip"""

	def __init__(self, args):
		"""Will call the mother constructor to set the name, lore and usedIn attributes.
		Then, unpack every stat (I didn't figure out a more "general" way to do this without
			interfering with name/lore/usedIn)"""
		Item.__init__(self, args)
		#could have made this in one instruction, but by make a multi-line/ugly instruction
		#the stat boosts
		self.str, self.dex, self.vit = args["str"], args["dex"], args["vit"]
		self.int, self.wis, self.luk = args["int"], args["wis"], args["luk"]
		#the slot and type
		self.slot, self.type = args["slot"], args["type"]



#class Potion(Item):
#	"""Class used to create life/mana potions.
#	takes an int level and an str type ("Life" or Mana") that is "Life" by default.
#	So you just need to do Potion(3) for a lvl 3 life potion,
#	and Potion(2, "Mana") for a lvl 2 mana potion"""
#	def __init__(self, lvl, type="Life")