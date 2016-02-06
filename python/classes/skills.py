# pylint: disable=invalid-name,import-error
"""Module for passive and active skills"""

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


class PassiveSkill(object):
    """class for PassiveSkill.

    Takes:
    -an str tuple stats
    -an int tuple base boost
    -an int level"""

    def __init__(self, boosts, stats, lvl):
        # super(PassiveSkill, self).__init__()
        # this is a tuple because a skill should not change
        # self.boostedstats = tuple(boosts)
        # self.basestats = tuple(stats)
        # creates the empty stat dict
        self.stats = {
            "str": 0, "dex": 0, "vit": 0,
            "int": 0, "wis": 0, "luk": 0,
        }
        # transfer the stats and their values in a dict
        for i, stat in enumerate(boosts):
            self.stats[stat] = stats[i]
        self.exp = getexp(lvl)

    def addexp(self, exp):
        """Add exp to the skill"""
        self.exp += exp

    def getlevel(self):
        """Returns the level of the instance"""
        return getlvl(self.exp)

    def getstats(self):
        """Returns the stats under the form of a dict"""
        # todo
        return self.stats
