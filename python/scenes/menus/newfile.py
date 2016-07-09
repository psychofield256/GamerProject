import pygame as pg

# from constants import 
from classes.entities import Player
from scenes.base import Scene
from scenes.game.beginning import TowerFloor1

class NewFileMenu(Scene):
    """Menu for choosing the save file."""

    def __init__(self, name, manager):
        super(NewFileMenu, self).__init__(manager)
        self.name = name
        self.filename = []
        self.is_clearing = False
        self.clearing_time = 0
        self.title = self.font.render("Gamer Project", True, (255,255,255))

    def render(self, screen):
        screen.fill((0,0,0))
        pos = self.get_title_pos(screen, self.title)
        screen.blit(self.title, pos)
        field = self.sfont.render("Save file: %s" % "".join(self.filename), True, (255,255,255))
        field = self.surround_with_rect(field)
        pos = self.get_mid_surf_pos(screen, field)
        screen.blit(field, pos)

    def update(self, delta):
        if self.is_clearing:
            self.clearing_time += delta
        # "unpack" all the clearing time
        while self.clearing_time > 500:
            if len(self.filename):
                self.filename.pop()
                self.clearing_time -= 100
            else:
                self.clearing_time = 0

    def handle_events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.manager.go_back()
                elif e.unicode in self.chars:
                    self.filename.append(e.unicode)
                elif e.key == pg.K_BACKSPACE:
                    if len(self.filename):
                        self.filename.pop()
                    self.is_clearing = True
                elif e.key == pg.K_RETURN:
                    player = Player(self.name)
                    self.save(player, "".join(self.filename))
                    self.manager.go_to(TowerFloor1(self.manager, player))
            elif e.type == pg.KEYUP:
                if e.key == pg.K_BACKSPACE:
                    self.is_clearing = False
                    self.clearing_time = 0
