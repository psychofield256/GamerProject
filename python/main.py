#!usr/bin/env python

"""
Game made by psychofield.

Its objectives are to adapt the manga "The Gamer" as a real rpg.
"""

import pygame as pg
import pytmx
from ruamel import yaml
from easydict import EasyDict as edict

from scenes.manager import SceneManager

from items import shops, item_to_str
from classes.entities import Player
from constants import *

pg.init()
font = pg.font.Font(None, 24)
with open(CONFIG_FILE) as f:
    config = yaml.safe_load(f)
config = edict(config)
print(config)
width, height = config.window.values()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("The Gamer Project")

back = pg.Surface(screen.get_size()).convert()
clock = pg.time.Clock()
scenemanager = SceneManager()


def write(surf, text, pos, color=COLORS["white"]):
    rendered = font.render(text, 1, color)
    surf.blit(rendered, pos)


def get_mid(surf):
    width, height = surf.get_size()
    return (width/2, height/2)

while not scenemanager.ended:
    time = clock.tick(60)
    if pg.event.get(pg.QUIT):
        scenemanager.quit()
    else:
        scenemanager.scene.handle_events(pg.event.get())
        scenemanager.scene.update(time)
        scenemanager.scene.render(screen)
    # background = pg.Surface(screen.get_size())
    # screen.blit(back, (0, 0))
    pg.display.flip()

"""
for item in shops["items"]:
    print(item_to_str(item))

print("-----------")
print("-----------")
"""
"""
for weapon in shops["weapons"]:
    inv.add(weapon)

for armor in shops["armors"]:
    inv.add(armor)

for gem in shops["gems"]:
    # print(item_to_str(gem))
    inv.add(gem)

inv.equip(0)

for equip in inv.equipments:
    print(item_to_str(equip))

print("-----------")
print("-----------")

for slot, equip in inv.equipment.items():
    print("%s:\n%s" % (slot, item_to_str(equip)))
"""
