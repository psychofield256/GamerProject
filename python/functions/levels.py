"""
This module contains the functions used for calculations about level and exp
"""


def getexp(lvl):
    """
    Calculates the experience needed to get the level in arguments.

    The condition to level up is: exp = (lvl+1)^3,
    where exp is the experience needed, and lvl+1
    the next level (lvl is the current level)
    To remove the possibility of having the level 0,
    change "lvl > 0" into "lvl > 1" (however, tests won't work as
    I made them for the level 0)
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
    To remove the possibility of having the level 0
    (which I didn't test because I don't want to rewrite this
    another time), change all the "(lvl+1)" into "lvl" (however,
    tests won't work as I made them for the level 0).
    """
    lvl = 0
    while exp >= (lvl+1) ** 3: # while the exp is enough to up to the next level
        exp -= (lvl+1) ** 3  # removes the exp used to up
        lvl += 1
    return lvl
