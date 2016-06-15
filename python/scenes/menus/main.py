import pygame as pg

from constants import MENU_CURSOR_FILE, COLORS
from scenes.base import Scene
from scenes.menus.newgame import NewNameMenu
from scenes.menus.loadsavefile import LoadSaveFileMenu
from scenes.menus.settings import SettingsMenu

class MainMenu(Scene):
    """First scene"""

    def __init__(self):
        super(MainMenu, self).__init__()
        self.choices = [
            {"msg": "New Game", "next": NewNameMenu},
            {"msg": "Continue", "next": LoadSaveFileMenu},
            {"msg": "Settings", "next": SettingsMenu},
            {"msg": "Quit", "next": None}
        ]
        self.cursor = pg.image.load(MENU_CURSOR_FILE).convert_alpha()

        self.choice = 0 # 0 is the first

    def render(self, screen):
        screen.fill(COLORS["black"])
        title = self.font.render("Gamer Project", True, COLORS["white"])
        screen_w, screen_h = screen.get_size()
        screen_center_w = screen_w / 2
        screen_center_h = screen_h / 2

        title_w, title_h = title.get_size()
        y = screen_h / 4
        x = screen_w / 2
        # blit the center of the text
        pos = (x - title_w / 2, y - title_h / 2)
        # new version
        pos = self.get_title_pos(screen, title)
        screen.blit(title, pos)

        for i, c in enumerate(self.choices):
            txt = self.sfont.render(c["msg"], True, (255,255,255))
            txt_w, txt_h = txt.get_size()
            txt_center_h = txt_h / 2
            txt_center_w = txt_w / 2
            # blit every choice 50 px after the previous one
            # start at the middle of the screen (height), and each line starts at a constant position (-100 because of the size of the text)
            pos = (screen_center_w - 100, screen_center_h - txt_center_h + (50 * i))
            # pos = (150, 300 + center_h + (50 * i))
            screen.blit(txt, pos)
            # blit a cursor at the right if it's the selected choice
            if i == self.choice:
                #                                    + 10 else it'll be on the text
                pos = (screen_center_w - 100 + txt_w + 10, screen_center_h + txt_center_h + 50 * i)
                screen.blit(self.cursor, pos)

    def update(self, delta):
        "The delta arg is the time (in ms) elapsed before the call"
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.manager.quit()

                # handle the choice change
                elif e.key == pg.K_DOWN:
                    # if the last choice is selected
                    if self.choice == len(self.choices)-1:
                        # go to the first
                        self.choice = 0
                    else:
                        self.choice += 1
                elif e.key == pg.K_UP:
                    if self.choice == 0:
                        self.choice = len(self.choices) - 1
                    else:
                        self.choice -= 1

                # handle the selection of a choice
                elif e.key == pg.K_RETURN:
                    # in case it's None (Quit)
                    if self.choices[self.choice]["next"]:
                        self.manager.add(self.choices[self.choice]["next"]())
                    else:
                        self.manager.quit()
