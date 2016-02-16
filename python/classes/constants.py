#!/usr/bin/env python
"""
Import constants from upper directory and replace itself with them.

It is used for not replacing the same ugly code in every module
that need a constant.
"""

import os
import sys

# if pythonpath is not main.py, go up until you're at it and register it
directory = os.path.abspath(__file__)
while not directory.endswith("python"):
    directory = os.path.dirname(directory)
sys.path.insert(0, directory)


import constants

sys.modules[__name__] = constants
