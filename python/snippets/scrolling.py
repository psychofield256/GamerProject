import pygame as pg
import pyscroll
from pyscroll.group import PyScrollGroup

from pygame.locals import *
from pytmx import load_pygame

HERO_MOVE_SPEED = 200

def load_img(path):
    return pg.image.load(path).convert_alpha()

def init_screen(width, height):
    return pg.display.set_mode((width, height), RESIZABLE)


class Player(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.img = load_img("../resources/sprites/Mage.png")
        self.velocity = (0, 0)
        self._position = (0, 0)
        self._old_position = self.position
        self.rect = self.img.get_rect()
        self.feet = pg.Rect(0, 0, self.rect.width * 0.5, 8) # self.rect.height * 0.5)

    @property
    def position(self):
        return tuple(self._position)

    @position.setter
    def position(self, value):
        self._position = tuple(value)

    def update(self, dt):
        self._old_position = self._position[:]
        self._position[0] += dt * self.velocity[0]
        self._position[1] += dt * self.velocity[1]
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt):
        "If called after an update, the sprite can move back"
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom


class Game(object):
    """Basic game."""
    filename = "../resources/maps/tower_test2.tmx"

    def __init__(self, screen):
        self.running = False
        tmx_data = load_pygame(self.filename)

        self.walls = []
        for obj in tmx_data.objects():
            self.walls.append(pg.Rect(
                obj.x, obj.y,
                obj.width, obj.height
            ))

        map_data = pyscroll.data.TiledMapData(tmx_data)

        self.map_layer = pyscroll.BufferedRenderer(map_data, screen.get_size())
        self.map_layer.zoom = 2

        # 2nd layer for the sprites
        self.group = PyScrollGroup(map_layer=self.map_layer, default_layer=1)
        self.player = Player()

        self.player.position = self.map_layer.map_rect.center

        self.group.add(self.player)

    def draw(self, screen):
        self.group.center(self.player.rect.center)
        self.group.draw()

    def handle_input(self):
        poll = pg.event.poll
        e = poll()

        while e:
            if e.type == QUIT:
                self.running = False
                break

            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.running = False
                    break

                elif e.key == K_EQUALS:
                    self.map_layer.zoom += 0.25

                elif e.key == K_MINUS:
                    value = self.map_layer.zoom - 0.25
                    if value > 0:
                        self.map_layer.zoom = value

                elif e.key == K_UP:
                    self.player.velocity[1] = -HERO_MODE_SPEED
                elif e.key == K_DOWN:
                    self.player.velocity[1] = HERO_MODE_SPEED
                else:
                    self.player.velocity[1] = 0  # là là ici là

            elif e.type == VIDEO_RESIZE:
                init_screen(e.w, e.h)
                self.map_layer.set_size(e.w, e.h)
            e = poll()

        pressed = pg.key.get_pressed()
        



pg.init()
pg.font.init()

screen = pg.set_display((640, 480))
pg.display.set_caption("Scrolling test")
