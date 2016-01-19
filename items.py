#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#IMPORTANT:
#Don't forget to set "insertable": False when you don't want an error


#items
items = [
	#example
	{
		"id": "TestItem1",
		"name": "item",
		"lore": "description",
		"usedIn": "Nothing",
		"weight": 1,
	},
	
]

jewels = [
	#jewel example
	{
		"id": "TestJewel1",
		"name": "jewel test",
		"lore": "A jewel that can decorate an equipment",
		"usedIn": "Jewelry",
		"weight": 1,
		"str": 300, "dex": 300, "vit": 300,
		"int": 300, "wis": 300, "luk": 300 #no, that's not cheat
	}
]

#equipments
equipments = [
	#example
	{
		"id": "Example",
		"name": "Example Sword",
		"lore": "description",
		"lvl": 1,
		"usedIn": "Nothing",
		"weight": 10,
		"emptySlots": 1, #emptySlots if for inserting items which provide stat boosts
		"slot": "weapon", #weapon, helmet, chestplate, leggings or boots
		"type": "sword", #sword, axe, bow...
		"str": 100, "dex": 100, "vit": 100,
		"int": 100, "wis": 100, "luk": 100 #no, that's not cheat. that's programming.
	}, {
		"id": "BossSword1",
		"name": "sword of devil",
		"lore": "the sword left by the blue demon",
		"lvl": 10,
		"usedIn": "Nothing",
		"weight": 10,
		"insertable": False,
		"emptySlots": 2, 
		"slot": "weapon",
		"type": "sword",
		"str": 10, "dex": 15, "vit": 10,
		"int": 0, "wis": 0, "luk": 0
	}, {
		"id": "FirstSword",
		"name": "wooden stick",
		"lore": "a wooden stick you \"borrowed\" at someone you didn't know",
		"lvl": 1,
		"usedIn": "Nothing",
		"weight": 12,
		"insertable": False,
		"emptySlots": 0,
		"slot": "weapon",
		"type": "sword",
		"str": 5, "dex": 0, "vit": 0,
		"int": 0, "wis": 0, "luk": 0
	}
]



