#!/usr/bin/usr python
"""
This module contains the functions to convert items into strings
"""

import os
import sys

try:
    import constants as c
except ImportError:
    MAINDIR = os.path.abspath(__file__)
    while not MAINDIR.endswith("python"):
        MAINDIR = os.path.dirname(MAINDIR)
    sys.path.insert(0, MAINDIR)

    import constants as c

def new_bunch_str(self):
    """
    Function added to bunch.Bunch as a method.

    Equivalent to __str__(self), but added to an existing class.
    This is for not create a class with only
    1 __str__ function and use inheritance.
    """
    var = ""
    for key in c.info_list:
        var += "%s: %s\n" % (key, str(self[key]))
    #var += "name: " + self.["name"] + "\n"
    #var += "lore: " + i["lore"] + "\n"
    #var += "lvl: " + str(i["lvl"]) + "\n"
    #var += "weight: " + str(i["weight"]) + "\n"

    return var
