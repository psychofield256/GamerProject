# Python adaptation

This is the python version of the Gamer Project.

## Requirements
Currently, the needed libraries are :
* ruamel.yaml (Pyaml works too, but by changing YAML\_PARSING\_LIB in constants.py),
* pygame,
* pytmx,
* easydict (really small. I think every pythonist should know what is it)

The game was made in python 3.5, but I didn't use any specific 3.5 functionnality, and every 3.x should work

## Config
I used json files before, but I choosed to use yaml instead (easier to write)
### Equipments
In yml files, if you want to add new equipments, you have to write:
In yaml files, the files are organized like this:

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

2. added stats (Not available!)
	Note: these stats are constants, and should only be weak equipment boost (for example, if you have a total of 100 in critical or dodge rate, you're probably cheat-modding the config)
	* pres: physical resistence (% in adversary's damages)
	* mres: magical resistance (% in adversary's damages)
	* pdam: physical damages (% in your damages)
	* mdam: magical damages (% in your damages)
	* dodg: dodge rate (% added to base rate)
	* miss: miss rate (% added to base rate) (you should add a negative value for this one)
	* crit: critical rate (% added to your basic rate)
	* hmax: max hp (% of your basic max life)
	* mmax: max mana (% of your basic max mana)
	* hreg: hp regen (% of your basic life regen)
	* mreg: mana regen (% of your basic mana regen)


### Consumables (Not available!)



### Skills (Not available!)
In json files, to add a new skill, you have to write:
```json
{
	"name": "name",
	"lore": "description",
	"cases": ["case1", "case2"],
	"requirements": {
		"stat1": 5
	}
	"stats": {
		"stat1": 5
	}
}
```

In stats, it's the same that equipment. I really discourage using stats in percents, as upgrading the skill will increase the percentage (see the note in added stats)

In cases, you write the situations in which the skill will gain experience. They can be:
* fight-begin: the beginning of a fight
* fight-end: the end of a fight
* turn-begin: the beginning of a turn
* turn-end: the end of a turn
* hit: when the character hits an ennemy
* hit-defend: when the character hits an ennemy defending
* hurt: when the character is hurt
* hurt-defend: when the character is hit after choosing to defend
* use: when the skill is used (only for active skills)
