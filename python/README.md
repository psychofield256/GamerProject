# Python adaptation

This is the python version of the Gamer Project.

## Requirements
The needed libraries is json, the default python lib.
The game was made in python 3.5, but I didn't use any specific 3.5 functionnality, and every 3.x should work

## Config
### Equipments
In json files, if you want to add new equipments, you have to write:

```json
{
	"name": "name",
	"lore": "description",
	"lvl": 0,
	"weight": 10,
	"empty_slots": 2,
	"slot": "weapon/helmet/chestplate/leggings/boots/pendant/ring/mantle",
	"stats": {
		"attribute1": 8, "attribute2": 3
	}
}
```

In stats, the attributes are:

1. basic stats:
	* abbr: stat name (what it does)
	* str: strength (physical damages, physical resistance and inventory's max total weight)
	* dex: dexterity (miss and touch rates)
	* vit: vitality (the max hp and hp regen)
	* int: intelligence (the max mp and magical damages)
	* wis: wisdom (the mp regen and magical resistance)
	* luk: luck (the critical rate)

2. added stats
	Note: these stats are constants, and should only be weak equipment boost (for example, if you have a total of 100 in critical or dodge rate, you're probably cheat-modding the config)
	* pres: physical resistence (% in adversary's damages)
	* mres: magical resistance (% in adversary's damages)
	* pdam: physical damages (% in your damages)
	* mdam: magical damages (% in your damages)
	* dodg: dodge rate (% added to base rate)
	* miss: miss rate (% added to base rate) (you should add a negative value for this one)
	* maxh: max hp (% of your basic max life)
	* maxm: max mana (% of your basic max mana)
	* hreg: hp regen (% of your basic life regen)
	* mreg: mana regen (% of your basic mana regen)
	* crit: critical rate (% added to your basic rate)