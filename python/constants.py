"""
Constants used in the project.

Imported with import constants (as c)
The constants can be set at every moment, because
import will return an instance, not the module.
"""

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

class Constants(object):
    """Constants of the project."""

    class ConstantError(TypeError): pass

    # def __init__(self):
    # """Create the constants."""
    item_info_list = ["name", "lvl", "lore", "weight"]
    equipment_info_list = ["sockets", "slot"]
    empty_equipment_dict = {
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

import sys
sys.modules[__name__] = c
