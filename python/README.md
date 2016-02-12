# Python adaptation

This is the python version of the Gamer Project.

## Config
### Equipments
In json files, if you want to add new equipments, you have to write:

```javascript
{
	"name": name,
	"lore": description,
	"lvl": lvl,
	"weight": weight,
	"empty_slots": slots_for_jewels,
	"slot": 0forweapon_1forhelmet_2forchestplate_3forleggings_4forboots,
	"stats": {
		"attribute1": value, "attribute2": value
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
	* pres: physical resistence (% added to str base value)
	* mres: magical resistance (% added to wis base value)
	* pdam: physical damages (% added to str base value)
	* mdam: magical damages (% added to int base value)

