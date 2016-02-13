#!/usr/bin/usr python
# pylint: disable=import-error
"""
This module contains the functions to convert items into strings.

(pylint) import error is disabled because pylint doesn't recognize
the use of pythonpath to make imports work when it's a standalone or not.
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

def item_print(self):
    """
    Function used to convert a dict item into an str.

    Equivalent to __str__(self), but a class isn't used.
    This is to avoid making a class with only
    a __str__ function and use inheritance.
    """
    var = ""
    for key in c.info_list:
        var += "%s: %s\n" % (key, str(self[key]))
    #var += "name: " + self.["name"] + "\n"
    #var += "lore: " + i["lore"] + "\n"
    #var += "lvl: " + str(i["lvl"]) + "\n"
    #var += "weight: " + str(i["weight"]) + "\n"

    return var
