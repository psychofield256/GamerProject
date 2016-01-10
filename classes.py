#!/usr/bin/env python
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod


class Inventory:
	"""Class used to create the inventory of entities
	takes:
	-an Equipment tuple (or list)
	-every Item you want (or a tuple)"""
	def __init__(self, equipments=None, *items):
		self.itemList = []
		for equip in equipments:
			#todo
			pass

class Item:
	"""Class used to create items.
	takes a dict with:
	-an str name
	-an str lore (use None if you don't want)
	-an str usedIn (same as above)"""

	def __init__(self, args):
		"""unpack the name, lore and usedIn attributes."""
		self.name, self.lore, self.usedIn = args["name"], args["lore"], args["usedIn"]
		#self.name = args["name"]
		#self.lore = args["lore"]
		#self.usedIn = args["usedIn"]

class Equipment(Item):
	"""Class used to create equipments.
	takes a dict, as Item, but with every stat boost defined in.
	e.g. equip = {
	"name": "sword of devil",
	"lore": "the sword left by the blue demon",
	"usedIn": "forge",
	"str": 10, "dex": 15, "vit": 10,
	"int": 0, "wis": 0, "luk": 0
	}"""

	def __init__(self, args):
		"""Will call the mother constructor to set the name, lore and usedIn attributes.
		Then, unpack every stat (I didn't figure out a more "general" way to do this without
			interfering with name/lore/usedIn)"""
		Item.__init__(self, args)
		#could have made this in one instruction, but by make a multi-line/ugly instruction
		self.str, self.dex, self.vit = args["str"], args["dex"], args["vit"]
		self.int, self.wis, self.luk = args["int"], args["wis"], args["luk"]