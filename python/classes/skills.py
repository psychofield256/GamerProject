# pylint: disable=invalid-name,import-error
"""Module for skills and active/passive boosts"""

import sys
import os

try:
    from functions.levels import getexp, getlvl
except ImportError:
    # if pythonpath is not main.py, go up until you're at it and register it
    directory = os.path.abspath(__file__)
    while not directory.endswith("python"):
        directory = os.path.dirname(directory)
    sys.path.insert(0, directory)

    from functions.levels import getexp, getlvl


class PassiveBoost(object):
    """class for PassiveBoost.

    Takes:
    -an str tuple stats
    -an int tuple base boost
    -an int level
    -a float level growth
    -a Player/Monster instance owner
    """

    def __init__(self, stats, boosts, owner, lvl=1):
        # this is a tuple because a skill should not change
        # it's not a dict because more of the stats will not be used
        self.boostedstats = tuple(stats)
        self.basestats = tuple(boosts)
        # creates the empty stat dict (useless for now)
        # self.stats = {
        #    "str": 0, "dex": 0, "vit": 0,
        #    "int": 0, "wis": 0, "luk": 0,
        # }
        # todo remove if not used
        # transfer the stats and their values in a dict
        # for i, stat in enumerate(boosts):
        #    self.stats[stat] = stats[i]

        self.owner = owner
        self.exp = getexp(lvl)

    def addexp(self, exp):
        """Add exp to the boost"""
        self.unapply()
        self.exp += exp
        self.apply()

    def getlevel(self):
        """Returns the level of the instance"""
        return getlvl(self.exp)

    def getstats(self):
        """
        Generator of the stats and the values under the form of a tuple

        Yields (stat_name, value)
        """
        # todo
        for i, stat in enumerate(self.boostedstats):
            value = self.basestats[i] * (self.getlevel() ** 3)
            yield (stat, value)
        # return self.stats

    def unapply(self):
        """Method to unapply the boosts on the owner"""
        for stat, value in self.getstats():
            value = value * (self.getlevel() ** 3)
            # value *= self.growth
            self.owner.stats[stat] -= value

    def apply(self):
        """Method to apply the boosts on the owner"""
        for stat, value in self.getstats():
            value = value * (self.getlevel() ** 3)
            self.owner.stats[stat] += value
