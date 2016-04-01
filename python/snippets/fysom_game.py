#!usr/bin/env python
"""
Attempt to make a stated script with fysom.
"""

import pygame
from fysom import Fysom

fsm = Fysom({
    'initial': 'main-menu',
    'final': 'leaving',
    'events': [
        {'name': 'leave', 'src': '*', 'dst': 'leaving'},
        {'name': 'cont', 'src': 'main-menu', 'dst': "select-file"},
    ]})

run = 1
while run:
    if fsm.current == "main-menu":
        print("You are in the main menu. You can:")
        print("1-leave")
        print("2-continue")
        i = input("\nWhat do you want ? ")
        if i == "1":
            fsm.leave()
        elif i == "2":
            fsm.cont()
    elif fsm.current == "select-file":
        print("Not implemented, come after")
        fsm.leave()
    elif fsm.current == "leaving":
        print("goodbye!")
        run = False
