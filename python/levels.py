#!usr/bin/env python
"""
This module contains the functions used for calculations about level and exp
"""


def getexp(lvl):
    """
    Calculates the experience needed to get the level in arguments.

    The condition to level up is: exp = (lvl+1)^3,
    where exp is the experience needed, and lvl+1
    the next level (lvl is the current level)
    """
    exp = 0
    while lvl > 0:
        exp += lvl ** 3
        lvl -= 1
    return exp


def getlvl(exp):
    """Calculates the level depending on the current exp.

    The condition to level up is: exp = (lvl+1)^3,
    where exp is the experience needed, and lvl+1
    the next level.
    lvl is the current level.
    Here, we are calculating each time the exp needed to
    up with the next level (lvl+1).
    """
    lvl = 0
    # while the exp is enough to up to the next level
    while exp >= (lvl + 1) ** 3:
        exp -= (lvl + 1) ** 3  # removes the exp used to up
        lvl += 1
    return lvl
