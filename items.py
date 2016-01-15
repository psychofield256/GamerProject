#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#IMPORTANT:
#Don't forget to set "insertable": False when you don't want an error


#items
i = {"name": "item", "id": "TestItem1","lore": "description", "usedIn": "alchemy", "weight": 1, "insertable": False}
t = {"name": "itemtest", "id": "TestItem2" ,"lore": "", "usedIn": "Nothing", "weight": 1, "insertable": False}

#equipments
#the doc example
equipExample = {
	"name": "sword of devil",
	"id": "EquipTest1",
	"lore": "the sword left by the blue demon",
	"usedIn": "forge",
	"weight": 10,
	"insertable": False,
	"emptySlots": 2, #emptySlots if for inserting items which provide stat boosts
	"slot": "weapon", #weapon, helmet, chestplate, leggings or boots
	"type": "sword", #sword, axe, bow...
	"str": 10, "dex": 15, "vit": 10,
	"int": 0, "wis": 0, "luk": 0,
	}

beginningSword = {
	"name": "wooden stick",
	"id": "FirstSword",
	"lore": "a wooden stick you \"borrowed\" at someone you didn't know",
	"usedIn": "Nothing.",
	"weight": 12,
	"insertable": False,
	"emptySlots": 0,
	"slot": "weapon",
	"type": "sword",
	"str": 5, "dex": 0, "vit": 0,
	"int": 0, "wis": 0, "luk": 0,
}
