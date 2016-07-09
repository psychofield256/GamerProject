=========
Armors
=========

The path to the armors config files is: config/items/<section>/armors.yml

To create an armor, the following attributes must be set:

- name: string
- id: string, used as identifier
- sprite: filepath, explanations in :ref:`sprites`
- lore: string, description (seen in inventory)
- lvl: int, used as necessary level to equip, to calculate the price,
  and maybe alchemy some day
- weight: int, used to limit the items in inventory
- slot: string, used in inventory. Can be:

  - helmet
  - chestplate
  - leggings
  - boots
  - pendant
  - ring
  - mantle

- stats: Fill as you want. Everything in the :ref:`stats` will count.
