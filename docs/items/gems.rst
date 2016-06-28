====
Gems
====

The path to the gems config giles is: config/items/<section>/gems.yml

WARNING: The gems can't be removed. It's made on purpose, as the game is very short.

To create a gem, the following attributes must be set:

- name: string
- sprite: filepath, explanations in :ref:`sprites`
- lore: string, description
- lvl: int, necessary level (if the level is greater than the level of the equipment, the level of the equipment will increase), price, alchemy
- weight: int, limit the inventory (added to the equipment)
- stats: Fill as you want. Everything in the :ref:`stats` will be added to the equipment.
