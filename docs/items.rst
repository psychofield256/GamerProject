Items
=====

The items are made by adding lines to the config files.

There are several types of items:

.. toctree::
   :maxdepth: 1

   items/armors
   items/weapons
   items/items
   items/consumables
   items/gems

The files are all in the config directory.

In items.rst, you can see several sections. They all correspond to a
place where items can be found. For example:

- The town-shop section contains all the items of the shop in the town.
- The dungeon-chests section contains all those of the chests in the
  dungeons.
- ...

In every section, there is a ``all.yml`` file. It just contains
``!include`` directives to join the contents together. The other files
are ``items.yml``, ``weapons.yml``, ``armors.yml``,
``consumables.yml``, and ``gems.yml``. They contain the description of
the items in the game. They are the file you will soon edit.

.. * basic items, gems, and consumables cannot be renamed, and their name is used as id. But armors and weapons can, and need an id
.. - slot: not needed, the game will fill it with "left-weapon"
.. - double-handed: true or false. If false, both can be equipped
