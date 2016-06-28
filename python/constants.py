"""
Constants used in the project.

Imported with import constants (as c)
The constants can be set at every moment, because
import will return an instance, not the module.
"""

import sys
# from pathlib import Path
from os import path

from ruamel import yaml
from easydict import EasyDict as edict

# this docstring is a comment
"""
STATLIST = ["str", "dex", "vit", "int", "wis", "luk"]

# the item's generals informations
GENERALS = ["name", "lore", "weight", "lvl"]

# the equipment's general informations
EQUIPGENERALS = ["slot", "type", "empty_slots"]

emptystats = {
    "str": 0, "dex": 0, "vit": 0,
    "int": 0, "wis": 0, "luk": 0,
}
"""

# "ruamel.yaml" or "pyaml"
YAML_PARSING_LIB = "ruamel.yaml"

BLOCK_TILE_LAYER = "ColliderBlocks"
EVENT_TILE_LAYER = "Events"

TILE_WIDTH = 32
TILE_HEIGHT = 32
CELL_WIDTH = 32
CELL_HEIGHT = 32

with open("config/settings.yml") as f:
    CONFIG = edict(yaml.safe_load(f))

COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
}
MENU_CURSOR_FILE = "resources/cursors/slime.png"
CONFIG_FILE = "config/settings.yml"
ARMOR_FILE = "config/armors.yml"


BASIC_STATS = ["str", "dex", "vit", "int", "wis", "luk"]
ADDED_STATS = ["pres", "mres", "pdam", "mdam", "dodg",
               "miss", "crit", "hmax", "mmax", "hreg",
               "mreg"]
ITEM_INFOS = ["name", "lvl", "lore", "weight"]
EQUIPMENT_INFOS = ["sockets", "slot"]
EMPTY_EQUIPMENT = {
    "weapon": None,
    "helmet": None,
    "chestplate": None,
    "leggings": None,
    "boots": None,
    "pendant": None,
    "ring": None,
    "mantle": None
}

p = "config/items"
ITEMLISTS_PATHS = {
    "armors": path.join(p, "armors.json"),
    "consumables": path.join(p, "consumables.json"),
    "gems": path.join(p, "gems.json"),
    "items": path.join(p, "items.json"),
    "weapons": path.join(p, "weapons.json"),
}

p = "config/town/shop"
SHOP_PATHS = {
    "armors": path.join(p, "armors.json"),
    "consumables": path.join(p, "consumables.json"),
    "gems": path.join(p, "gems.json"),
    "items": path.join(p, "items.json"),
    "weapons": path.join(p, "weapons.json"),
}

# to remove, it's a bad practice because it's too memory-heavy for simple
# constants and not practical

class Constants(object):
    """Constants of the project."""

    class ConstantError(TypeError):
        pass

    # def __init__(self):
    # """Create the constants."""
    basic_stats = ["str", "dex", "vit", "int", "wis", "luk"]

    added_stats = ["pres", "mres", "pdam", "mdam", "dodg",
                   "miss", "crit", "hmax", "mmax", "hreg", "mreg"]

    # todo
    # exp_cases = ["fight-end", ""]

    item_infos = ["name", "lvl", "lore", "weight"]

    equipment_infos = ["sockets", "slot"]

    empty_equipment = {
        "weapon": None,
        "helmet": None,
        "chestplate": None,
        "leggings": None,
        "boots": None,
        "pendant": None,
        "ring": None,
        "mantle": None
    }

    def __setattr__(self, attr, value):
        """Method to block redefining a constant."""
        if hasattr(self, attr):
            raise self.ConstantError("A constant cannot be changed.")
        else:
            object.__setattr__(self, attr, value)


# this allows to import the module and get the instance with
# constants in it. Other can be added after import, but other
# imported instances won't be changed
c = Constants()

# sys.modules[__name__] = c
