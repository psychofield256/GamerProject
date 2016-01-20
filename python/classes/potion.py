#!/usr/bin/env python
# -*- coding:utf-8 -*-

from classes.item import Item

class Potion(Item):
	"""Class used to create life/mana potions.
	takes an int level and an str type ("Life" or Mana") that is "Life" by default.
	So you just need to do Potion(3) for a lvl 3 life potion,
	and Potion(2, "Mana") for a lvl 2 mana potion"""
	
	def __init__(self, lvl, ptype="Life"):
		self.name  = ptype + " Potion lvl " + str(lvl)
		self.lvl = lvl
		self.regen = lvl * 200
		self.iType = ptype.lower()
		self.lore = "A magic beverage that instantly regenerates your " + self.iType + " from " + str(self.regen) + " points "
		self.weight = 0.1