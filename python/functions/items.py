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
    """Local function, return the stats of the item in a str."""
    var = "stats:\n"
    # sort basic and added stats in tuples
    basic_stats = []
    added_stats = []
    for stat, value in item["stats"].items():
        if stat in c.basic_stats:
            basic_stats.append((stat, value))
        else:
            added_stats.append((stat, value))

    # add them in the good order
    for stat, value in basic_stats:
        var += "\t%s: %s\n" % (stat, value)
    var += "\n"
    for stat, value in added_stats:
        var += "\t%s: %s\n" % (stat, value)
    return var

def gem_names(item):
    """Local function, return the names of the gems in a str."""
    var = "gems:\n"
    for gem in item["gems"]:
        var += "\t%s: %s\n" % (gem["name"])
    return var

def item_to_str(item):
    """
    Function used to convert a dict item into an str.

    Equivalent to __str__(self), but a class isn't used.
    This is to avoid making a class with only
    a __str__ function and use inheritance.
    """
    var = ""
    first_values = []
    second_values = []

    if item is None:
        return var

    for key, value in item.items():
        if key in c.item_info_list:
            first_values.append((key, value))
        else:
            second_values.append((key, value))
    for key, value in first_values:
        var += "%s: %s\n" % (key, str(value))
    for key, value in second_values:
        var += "%s: %s\n" % (key, str(value))

    if item["type"] == "equipment":
        for key in c.equipment_info_list:
            var += "%s: %s\n" % (key, str(item[key]))
        var += stats_to_str(item)
        if item["gems"] != []:
            var += gem_names(item)
    elif item["type"] == "gem":
        var += stats_to_str(item)

    return var
