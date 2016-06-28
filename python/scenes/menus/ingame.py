import pygame as pg
from pygame.locals import *

import pytmx

from scenes.base import Scene
from constants import *

class IngameMenu(Scene):
    "The ingame menu."

    def __init__(self, manager, player):
        super(IngameMenu, self).__init__()
        self.player = player
        self.manager = manager
        self.map = pytmx.load_pygame("resources/maps/ingame_menu.tmx")
        self.cursor = pg.image.load("resources/cursors/slime.png")
        self.choice = 0
        self.choices = [
            ("Resume", self.manager.go_back),
            ("Quit", self.manager.quit),
        ]
        # self.surf = pg.Surface(())

    def update(self, delta):
        pass

    def render(self, screen):
        bg = self.map.get_layer_by_name("Background")
        w, h = CELL_WIDTH, CELL_HEIGHT
        for x, y, img in bg.tiles():
            img = pg.transform.scale(img, (w, h))
            screen.blit(img, (x * w, y * h))

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.manager.cache["back-from-menu"] = True
                    self.manager.go_back()
