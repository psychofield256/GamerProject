#!/usr/bin/env python
"""
This module parses the json files in config/items.

Json files are parsed, and the module is replaced by a dict.
The dict contains the "items", "weapons" and "armors" keys.
The values are lists of item dicts.
"""

import json
import sys

items = []
weapons = []
armors = []
