.. _stats:

=====
Stats
=====

When one creates new equipments in the config menu, he wants to add
stat boosts. That's why there is a special attribute, ``stats``, which
can be filled with a lot of things.

The stats are regrouped under two categories: "basic" and "added"
stats. The added stats are written using a percentage, and are
calculated using the basic stats.

.. highlight:: yaml

The ``stats`` attribute looks like this::

  stats:
  attr: !int points
    str: 22
    dex: 5
    luk: 3

Here is the list of the stats:

1. Base stats

   - str: strength (physical damages, physical resistance and
     inventory max weight)
   - dex: dexterity (miss and touch rates)
   - vit: vitality (max hp, hp regen)
   - int: intelligence (max mp, magical damages)
   - wis: wisdom (mp regen, magical resistance)
   - luk: luck (critical rate)

2. Added stats

   - pres: physical resistance (% removed from enemy's damages)
   - mres: magical resistance (% removed from enemy's damages)
   - pdam: physical damages (% in your damages)
   - mdam: magical damages (% in your damages)
   - dodg: dodge rate (% added to base rate)
   - miss: miss rate (% removed to enemy's total touch rate)
   - crit: critical rate (% added to your basic rate)
   - hmax: max hp (% of your basic max life)
   - mmax: max mana (% of your basic max mana)
   - hreg: hp regen (% of your basic life regen)
   - mreg: mana regen (% of your basic mana regen)

