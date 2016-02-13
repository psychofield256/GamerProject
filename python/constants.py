"""
Constants used in the project.

Imported with import constants (as c)
The constants can be set at every moment, because
import will return an instance, not the module.
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

class Constants(object):
    """Constants of the project."""

    class ConstantError(TypeError): pass

    # def __init__(self):
    # """Create the constants."""
    item_info_list = ["name", "lvl", "lore", "weight"]
    equipment_info_list = ["sockets", "slot"]

    def __setattr__(self, attr, value):
        """Block redefining a constant."""
        # if there is already a constant, raise
        if hasattr(self, attr):
            raise self.ConstantError("A constant cannot be changed.")
        # else, create it
        object.__setattr__(self, attr, value)



# this allows to import the module and get the instance with
# basic constants in it. Other can be added
c = Constants()

import sys
sys.modules[__name__] = c
