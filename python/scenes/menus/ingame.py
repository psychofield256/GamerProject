import pygame as pg
from pygame.locals import *

import pytmx

from scenes.base import Scene
from scenes.tools.confirm import ConfirmPrompt
from constants import *

class IngameMenu(Scene):
    "The ingame menu."

    def __init__(self, manager, player):
        super(IngameMenu, self).__init__(manager)
        self.player = player
        self.map = pytmx.load_pygame("resources/maps/ingame_menu.tmx")
        self.cursor = pg.image.load("resources/cursors/slime.png")
        self.choice = 0
        self.choices = [
            ("Resume", self.manager.go_back),
            ("Quit", self.quit),
        ]
        self.to_blit = []
        height_pos = 20
        self.maxw = 0
        for choice in self.choices:
            surf = self.sfont.render(choice[0], True, COLORS['white'])
            self.to_blit.append((surf, (20, height_pos)))
            self.maxw = max(self.maxw, (20 + surf.get_width() + 20 + \
                                        self.cursor.get_width() + 10))
            height_pos += 20 + surf.get_height()
        self.maxh = height_pos  # 20 px at top and at bottom
            
        # self.surf = pg.Surface(())

    def quit(self):
        self.manager.add(ConfirmPrompt("Are you sure ? The \
changes won't be saved",
                                       self.manager))

    def update(self, delta):
        pass

    def render(self, screen):
        if not self.manager.cache.get('in-confirm-prompt', False):
            self.manager.render_old(screen)
        bg = self.map.get_layer_by_name("Background")
        # w, h = CELL_WIDTH, CELL_HEIGHT
        w, h = self.maxw // 16, self.maxh // 16
        for x, y, img in bg.tiles():
            img = pg.transform.scale(img, (w, h))
            screen.blit(img, (x * w, y * h))
        # w, h = screen.get_size()
        # w = int(w / 3)
        # h = int(h / 1.2)

        for i, (txt, coords) in enumerate(self.to_blit):
            screen.blit(txt, coords)
            if self.choice == i:
                screen.blit(self.cursor,
                          (coords[0] + txt.get_width() + 10,
                           coords[1] + 20))

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.manager.go_back()
                elif e.key == K_DOWN:
                    if self.choice == len(self.choices) - 1:
                        self.choice = 0
                    else:
                        self.choice += 1
                elif e.key == K_UP:
                    if self.choice == 0:
                        self.choice = len(self.choices) - 1
                    else:
                        self.choice -= 1
                elif e.key == K_RETURN:
                    # call the function
                    self.choices[self.choice][1]()
