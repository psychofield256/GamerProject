# pylint: disable=invalid-name,import-error
"""Module for skills and active/passive boosts"""

import sys
import os

try:
    from functions.levels import getexp, getlvl
    from constants import *
except ImportError:
    # if pythonpath is not main.py, go up until you're at it and register it
    directory = os.path.abspath(__file__)
    while not directory.endswith("python"):
        directory = os.path.dirname(directory)
    sys.path.insert(0, directory)

    from functions.levels import getexp, getlvl
    from constants import *


class PermanentBoost(object):
    """
    class for PermanentBoost.
    A permanent boost is a permanent skill that increases
    the stats of the owner. Its exp is gained in the defined cases.
    It is always turned on and doesn't require mana to be activated

    Takes:
    -an str tuple stats
    -an int tuple base boost
    -a Player/Monster instance owner
    -an str tuple exp case (in constants.py)
    -an int level (not necessary)
    """

    def __init__(self, name, stats, boosts, owner, expcases, lvl=0):
        self.name = name
        # this is a tuple because a boost should not change the boosted stats
        # it's not a dict because most of the stats will not be used
        self.boosted_stats = tuple(stats)
        self.basestats = tuple(boosts)
        self.owner = owner
        # calculates the exp needed to get the level wanted
        self.exp = getexp(lvl)
        self.expcases = expcases

    def addexp(self, exp, case):
        """Add exp to the boost"""
        self.unapply()
        if case in self.expcases:
            self.exp += exp
        self.apply()

    def getlevel(self):
        """Returns the level of the instance"""
        return getlvl(self.exp)

    def getbasestats(self):
        """
        Generator of the stats and their values at level 0 with tuples

        Yields (stat_name, value)
        stat_name is the name of the stats (str), like "str" or "dex"
        the value is the base value
        """
        for i, stat in enumerate(self.boosted_stats):
            yield (stat, self.basestats[i])

    def getstats(self):
        """
        Generator of the stats and their values under the form of a tuple

        Yields (stat_name, value)
        the value is the base value multiplied by (level+1) ^ 2
        level+1 is because if the level is 0, the boost is 0
        """
        # todo
        for i, stat in enumerate(self.boosted_stats):
            # take the value with i in self.basestats
            # and multiply it depending on the level
            value = self.basestats[i] * ((self.getlevel() + 1) ** 2)
            yield (stat, value)

    def unapply(self):
        """Method to unapply the boosts on the owner"""
        for stat, value in self.getstats():
            self.owner.stats[stat] -= value

    def apply(self):
        """Method to apply the boosts on the owner"""
        for stat, value in self.getstats():
            self.owner.stats[stat] += value


class ActiveSkill(object):
    """class for PassiveSkill.
    A passive skill is a skill """
    def __init__(self, name, stats, ):
        super(PassiveSkill, self).__init__()
        self.arg = arg
        
class PassiveSkill(PermanentBoost):
    """
    class for PassiveSkill.
    a passive skill is a skill that increases the stats of the
    owner and can be turned on/off.
    Its exp is gained in the defined cases.
    It constantly uses mana (every minute) when on,
    and not when off. If there is not enough mana to keep it
    activated, it removes itself from the owner's activated passives list.
    Can be activated in the menu (it may be activated several times
    at once, but costs most mana).
    Inherits from PermanentBoost.

    Takes:
    -an str tuple stats
    -an int tuple base boost
    -a Player/Monster instance owner
    -an str tuple exp case (all in constants.py)
    -an int mana cost/minute (not necessary, 10 at level 0 by default)
    -an int level (not necessary, 0 by default)

    """
    def __init__(self, name, stats, boosts, cost=10, owner, expcases, lvl=0):
        # same for all except the mana cost
        super(name, stats, boosts, owner, expcases, lvl)
        self.cost = cost

    def apply(self):
        """Method to apply the boosts on the owner and take mana"""
        super(self)
        self.takecost()

    def takecost(self):
        """Method to remove the mana cost to the owner"""
        try:
            self.owner.mana -= self.cost
        except ManaError:
            self.owner.passives.remove(self)
