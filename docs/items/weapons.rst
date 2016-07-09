=======
Weapons
=======

The path to the weapons config files is: config/items/<section>/weapons.yml

To create a weapon, the following attributes must be set:

- name: string
- id: string, used as identifier (for comparisons)
- sprite: filepath, explanations in :ref:`sprites`.
- lore: string, description (seen in inventory)
- lvl: used as necessary level to equip and to calculate the price,
  and maybe alchemy some day
- weight: int, used to limit the items in inventory
- type: string, used for boosts. Can be:

  - large-sword (family: sword, double-handed)
  - axe (family: axe, double-handed)
  - staff (family: magical, double-handed)
  - katana (family: sword, single-handed)
  - dagger (family: dagger, single-handed)
  - wand (family: magical, single-handed)
  - miscellaneous (family: single-handed)

- stats: Fill as you want. Everything in the :ref:`stats` will count.
