#!/usr/bin/env python
# pylint: disable=wrong-import-position,import-self
"""
Import constants from upper directory and replace itself with them.

It is used for not replacing the same ugly code in every module
that need a constant.

Pylint:
wrong-import-position is disabled because I can't import
something before changing pythonpath to specify its location.
import-self is disabled because as the main directory is
at index 0, it will be used before this file.
"""

import os
import sys

# if pythonpath is not main.py, go up until you're at it and register it
MAIN_DIR = os.path.abspath(__file__)

while not MAIN_DIR.endswith("python"):
    MAIN_DIR = os.path.dirname(MAIN_DIR)

sys.path.insert(0, MAIN_DIR)


from constants import *
