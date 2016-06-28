=====
Items
=====

The path to the items config files is: config/items/<section>/items.yml

To create an item, the following attributes must be set:

- name: string, used as identifier (the item cannot be renamed)
- sprite: filepath, explanations in :ref:`sprites`
- lore: string, description (seen in inventory)
- lvl: int, used to calculate the price and maybe alchemy some day
- weight: int, used to limit the inventory
