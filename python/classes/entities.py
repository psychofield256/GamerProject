import pygame as pg


from constants import CONFIG, EMPTY_EQUIPMENT, BLOCK_TILE_LAYER

from classes.inventory import Inventory
from levels import getexp
from tools.pg.spritesheet import SpriteSheet


DOWN = 0
UP = 1
LEFT = 2
RIGHT = 3


class Entity(pg.sprite.Sprite):
    """Class for Entities."""

    def __init__(self, name, position, stats, equipment, img, lvl=0):
        pg.sprite.Sprite.__init__(self)
        # self.spritesheet = pg.image.load(img)
        self.spritesheet = SpriteSheet(img, (64, 64))
        self._direction = DOWN
        self.moving = False
        self.foot = "left"
        self._step = 0
        self._max_step = 300 # time in ms
        # self.x, self.y = position
        # self.oldx, self.oldy = position
        #self.sprite_switch = {
        #    # 1st line
        #    "down": self.spritesheet.subsurface(0, 0, 32, 16),
        #    "left": self.spritesheet.subsurface(0, 16, 32, 16),
        #    "right": self.spritesheet.subsurface(0, 32, 32, 16),
        #    "up": self.spritesheet.subsurface(0, 48, 32, 16),
        #}
        self.set_sprite()
        # self.rect = self.image.get_rect()
        self.rect = pg.Rect(position, (32, 32))
        # self.oldrect = self.rect.copy()

        self.exp = getexp(lvl)
        self.name = name
        self.stats = stats
        self.points = 0
        self.equipment = dict(EMPTY_EQUIPMENT)
        self.equipment.update(equipment)

        # passive boosts
        self.talents = []
        # monsters can be boosted (or malus-ed), but don't have the necessary AI to use the corresponding active skills
        self.boosts = []
        # active ones are useable in fight
        # passive ones are not, but not useable by monsters
        self.skills = {
            "active": [],
        }

    def set_sprite(self, size=(32, 32)):
        y = self._direction
        if self.foot == "right":
            x = 1
        else:
            x = 0
        # self.image = self.spritesheet.subsurface(x, y, w, h)
        self.image = self.spritesheet.get_sprite(x, y, size)

    def get_image(self, size):
        if self._step > (self._max_step / 2):
            self.foot = "right"
        else:
            self.foot = "left"
        self.set_sprite(size)
        return self.image
        # return pg.transform.scale(self.image, size)

    def forward(self):
        self.oldrect = self.rect.copy()
        if self._direction == UP:
            # self.y -= 1
            self.rect.y -= 1
        elif self._direction == DOWN:
            self.rect.y += 1
        elif self._direction == LEFT:
            self.rect.x -= 1
        elif self._direction == RIGHT:
            self.rect.x += 1
        if self.foot == "right":
            self.foot = "left"
        else:
            self.foot = "right"
        self.moving = False
        self.set_sprite()

    def step(self, s, tmxmap):
        if self._step >= self._max_step:
            self._step = 0
            self.forward()
        else:
            block_layer = tmxmap.get_layer_by_name(BLOCK_TILE_LAYER)
            next_rect = pg.Rect(self.in_front(), (1, 1))
            in_wall = False
            for x, y, gid in block_layer.iter_data():
                if gid and next_rect.collidepoint(x, y):
                    in_wall = True

            if not in_wall:
                self._step += s

    def in_front(self):
        "Return the point just in front of the player (used for collisions)"
        x, y = self.rect.x, self.rect.y
        if self._direction == UP:
            y -= 1
        elif self._direction == DOWN:
            y += 1
        elif self._direction == LEFT:
            x -= 1
        elif self._direction == RIGHT:
            x += 1
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
        x, y = self.rect.x * tw, self.rect.y * th
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

    # def is_up(self):
    #    return self.direction == "up"

    # def is_down(self):
    #    return self.direction == "down"


class Player(Entity):

    def __init__(self, name, pos=(0,0), lvl=0):
        stats = dict(CONFIG.player.new.stats)
        img = CONFIG.player.sprite.path
        equipment = {}
        # img = CONFIG.player.skin
        Entity.__init__(self, name, pos, stats, equipment, img, lvl)
        self.inv = Inventory()
        self.skills["passive"] = [] # skills used out of fights


class Monster(Entity):
    """docstring for Monster"""

    def __init__(self, name, pos, stats, equipment, to_drop, img, lvl=0):
        Entity.__init__(self, name, pos, stats, equipment, img, lvl)
        self.dropped_item = to_drop
