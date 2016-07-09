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
        # bg = self.map.get_layer_by_name("Background")
        # w, h = CELL_WIDTH, CELL_HEIGHT
        # for x, y, img in bg.tiles():
            # img = pg.transform.scale(img, (w, h))
            # screen.blit(img, (x * w, y * h))
        w, h = screen.get_size()
        w = int(w / 3)
        h = int(h / 1.2)

        menu = pg.Surface((w, h))

        menu.fill(COLORS['blue'])

        height_pos = 20

        for i, choice in enumerate(self.choices):
            txt = self.sfont.render(choice[0], True, COLORS['white'])
            menu.blit(txt, (20, height_pos))
            if self.choice == i:
                menu.blit(self.cursor, (30 + txt.get_width(), height_pos))
            height_pos += 20 + txt.get_height()


        screen.blit(menu, (0,0))

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.manager.cache["back-from-menu"] = True
                    self.manager.go_back()
