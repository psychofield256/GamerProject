===========
Consumables
===========

The path to the consumable config files is: config/items/<section>/consumables.yml

To create a consumable item, the following attributes must be set:

- name: string, used as identifier (can't be renamed)
- sprite: filepath, explanations in :ref:`sprites`
- lore: string, description (seen in inventory)
- lvl: int, used to calculate the price, and for alchemy (not implemented)
- weight: int, used to limit the inventory
- effects: object, put everything you want that is in :ref:`effects`
