import pygame as pg

from constants import COLORS
from scenes.base import Scene
from scenes.menus.newfile import NewFileMenu

class NewNameMenu(Scene):
    """Menu of player parameters before creating and playing the created game."""

    def __init__(self):
        super(NewNameMenu, self).__init__()
        self.name = []
        self.is_clearing = False  # when backspace is down
        self.clearing_time = 0

    def render(self, screen):
        screen.fill(COLORS["black"])
        title = self.font.render("Gamer Project", True, COLORS["white"])
        pos = self.get_title_pos(screen, title)
        screen.blit(title, pos)
        field = self.sfont.render("Name: %s" % "".join(self.name), True, (255,255,255))
        field = self.surround_with_rect(field)
        pos = self.get_mid_surf_pos(screen, field)
        screen.blit(field, pos)

    def update(self, delta):
        seconds = int(delta / 1000)
        if self.is_clearing:
            self.clearing_time += delta
        # if backspace was pressed for more than 0.5 second
        while self.clearing_time > 500:
            # clear one char if there is, every 0.1 second
            if len(self.name):
                self.name.pop()
                self.clearing_time -= 100
            else:
                self.clearing_time = 0

    def handle_events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN:
                # come back to the MainMenu
                if e.key == pg.K_ESCAPE:
                    self.manager.go_back()
                # add the character typed to the name
                elif e.unicode in self.chars:
                    self.name.append(e.unicode)
                elif e.key == pg.K_BACKSPACE:
                    if len(self.name):
                        self.name.pop()
                    self.is_clearing = True
                elif e.key == pg.K_RETURN:
                    # new_player = Player(self.name)
                    self.manager.go_to(NewFileMenu(self.name))
            elif e.type == pg.KEYUP:
                if e.key == pg.K_BACKSPACE:
                    self.is_clearing = False
                    self.clearing_time = 0
