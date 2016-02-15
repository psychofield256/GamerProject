#!/usr/bin/usr python
# pylint: disable=import-error
"""
This module contains the functions on items.

Functions:
item_to_str(item: dict) --> str
socket(item: dict, gem: dict)

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

def stats_to_str(item):
    """Local function, return the stats of the item."""
    var = "stats:\n"
    for stat, value in item["stats"].items():
        var += "%s: %s\n" % (stat, value)
    return var

def item_to_str(item):
    """
    Function used to convert a dict item into an str.

    Equivalent to __str__(self), but a class isn't used.
    This is to avoid making a class with only
    a __str__ function and use inheritance.
    """
    var = ""
    for key in c.item_info_list:
        var += "%s: %s\n" % (key, str(item[key]))

    if item["type"] == "equipment":
        for key in c.equipment_info_list:
            var += "%s: %s\n" % (key, str(item[key]))
        var += stats_to_str(item)
    elif item["type"] == "gem":
        for key in c.gem_info_list:
            var += "%s: %s\n" % (key, str(item[key]))
        var += stats_to_str(item)

    return var