"""
This module contains the functions used for calculations about level and exp
"""


def getexp(lvl):
    """
    Calculates the experience needed to get the level in arguments.

    The condition to level up is: exp = lvl^3,
    where exp is the experience needed, and lvl
    the next level.
    """
    exp = lvl ** 3
    return exp


def getlvl(exp):
    """Calculates the level depending on the current exp.

    The condition to level up is: exp = lvl^3,
    where exp is the experience needed, and lvl
    the next level.
    lvl - 1 is the current level (not used here), and lvl is the next one.
    So here, we are calculating each time the exp needed to up again.
    Actually, you can't have lvl 0, because 0 cubed = 0 and it's always 
    equal to exp
    """
    lvl = 1
    while exp >= lvl ** 3:
        lvl += 1
    return lvl
