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
	"""Class used to create an item
	takes:
	-an str name
	-an str lore (use None if you don't want)
	-an str usedIn (same as above)"""

	def __init__(self, args):
		self.name = args["name"]
		self.lore = args["lore"]
		self.usedIn = args["usedIn"]