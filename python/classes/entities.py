import os.path
import math
import pygame as pg

from constants import (CONFIG, EMPTY_EQUIPMENT, BLOCK_TILE_LAYER, TILE_WIDTH, TILE_HEIGHT)

from classes.inventory import Inventory
from levels import getexp
from tools.pg.spritesheet import SpriteSheet

from parsedconf import conf

# TODO
# remove the foot attr
# remove the rect (use properties to optimize the cpu)
# really depend of the config for sprite width.height

DOWN = 0
UP = 1
LEFT = 2
RIGHT = 3


class Entity(pg.sprite.Sprite):
    """Class for Entities."""

    def __init__(self, name, position, stats, equipment, img, size, lvl=0):
        pg.sprite.Sprite.__init__(self)
        self.swidth, self.sheight = size
        # self.
        self.spritesheet = SpriteSheet(img, (self.swidth, self.sheight))
        self._direction = DOWN
        self.moving = False
        self._step = 0
        self._max_step = 300 # time in ms
        self.x, self.y = position
        self.set_sprite()

        self.exp = getexp(lvl)
        self.name = name
        self.stats = stats
        self.points = 0
        self.equipment = dict(EMPTY_EQUIPMENT)
        self.equipment.update(equipment)

        # permanent passive boosts (out of and infights)
        self.talents = []
        # temporary active boosts or malus (out of and in fights)
        self.boosts = []
        # all the permanent fight skills
        self.skills = {
            "active": [],
            "passive": [],
        }
        skills = {
            "fight": {
                "active": [],
                "passive": [],
            },
            "out": {
                "active": [],
                "passive": [],
            },
        }

    def set_sprite(self, size=(32, 32)):
        y = self._direction
        # take the right foot if the player has walked more than half the cell
        # take the frame corresponding to the step
        x = int(self.spritesheet.xlen * (self._step / self._max_step))
        # in case the entity is at the end of the move
        if x >= self.spritesheet.xlen:
            x = 0
        self.image = self.spritesheet.get_sprite(x, y, size)

    def get_image(self, size):
        self.set_sprite(size)
        return self.image
        # return pg.transform.scale(self.image, size)

    def forward(self):
        if self._direction == UP:
            self.y -= 1
        elif self._direction == DOWN:
            self.y += 1
        elif self._direction == LEFT:
            self.x -= 1
        elif self._direction == RIGHT:
            self.x += 1
        self.moving = False
        self.set_sprite()

    def step(self, s, tmxmap):
        """s is the number of steps (should be used for delta)."""
        if self._step >= self._max_step:
            self._step = 0
            self.forward()
        else:
            block_layer = tmxmap.get_layer_by_name(BLOCK_TILE_LAYER)
            # I use a rect, but it doesn't actually represent a tile.
            # It's because when I iter tiles, I get x and y in coords, not
            # in pixels
            next_rect = pg.Rect(self.in_front(), (1, 1))
            in_wall = False
            for x, y, gid in block_layer.iter_data():
                if gid and next_rect.collidepoint(x, y):
                    in_wall = True
                    break

            if not in_wall:
                self._step += s

    def in_front(self, in_pixels=False):
        """Return the point just in front of the player (used in collisions).
        The in_pixels argument is never used in the code, but it didn't
        cost anything to keep it after realizing i didn't need it."""
        x, y = self.x, self.y
        if self._direction == UP:
            y -= 1
        elif self._direction == DOWN:
            y += 1
        elif self._direction == LEFT:
            x -= 1
        elif self._direction == RIGHT:
            x += 1

        if in_pixels:
            return (x * TILE_WIDTH, y * TILE_HEIGHT)
        return (x, y)

    def exact_cell(self):
        return self._step == 0

    @property
    def direction(self):
        if self._direction == UP:
            return "up"
        elif self._direction == DOWN:
            return "down"
        elif self._direction == LEFT:
            return "left"
        elif self._direction == RIGHT:
            return "right"

    def move_up(self):
        self._direction = UP
        self.set_sprite()

    def move_down(self):
        self._direction = DOWN
        self.set_sprite()

    def move_left(self):
        self._direction = LEFT
        self.set_sprite()

    def move_right(self):
        self._direction = RIGHT
        self.set_sprite()

    def update(self, delta, tilemap):
        pass

    def get_pixel_pos(self, tile_size):
        "Return the position with the step, in a pixel accurate way."
        tw, th = tile_size
        x, y = self.x * tw, self.y * th
        step = (self._step / self._max_step)
        if self._direction == UP:
            y -= step * th
        elif self._direction == DOWN:
            y += step * th
        elif self._direction == LEFT:
            x -= step * tw
        elif self._direction == RIGHT:
            x += step * tw
        return (x, y)

    @property
    def rect(self):
        return pg.Rect(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)


class Player(Entity):

    def __init__(self, name, pos=(0,0), lvl=0):
        stats = dict(conf.entities.player.stats) # rebuild the dict
        img = conf.entities.player.sprite.path
        size = (conf.entities.player.sprite.width,
                conf.entities.player.sprite.height)
        equipment = {}
        # img = CONFIG.player.skin
        Entity.__init__(self, name, pos, stats,
                        equipment, img, size, lvl)
        self.inv = Inventory()
        self.skills["passive"] = [] # skills used out of fights


class Monster(Entity):
    """docstring for Monster"""

    def __init__(self, name, pos, stats, equipment, to_drop, img, lvl=0):
        Entity.__init__(self, name, pos, stats, equipment, img, lvl)
        self.dropped_item = to_drop
