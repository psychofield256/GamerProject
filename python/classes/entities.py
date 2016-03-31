from classes.inventory import Inventory
from levels import getexp
from constants import *


class Entity(object):
    """docstring for Entity"""

    def __init__(self, name, stats, equipment, lvl=0):
        self.exp = getexp(lvl)
        self.name = name
        self.stats = stats
        self.points = 0
        self.equipment = EMPTY_EQUIPMENT
        self.equipment.update(equipment)

        self.masteries = []
        self.skills = []


class Player(Entity):

    def __init__(self, name, stats, equipment, lvl=0):
        Entity.__init__(self, name, stats, equipment, lvl)
        self.boosts = []
        self.inv = Inventory()


class Monster(Entity):
    """docstring for Monster"""

    def __init__(self, name, stats, equipment, to_drop, lvl=0):
        Entity.__init__(self, name, stats, equipment, lvl)
        self.dropped_item = to_drop
