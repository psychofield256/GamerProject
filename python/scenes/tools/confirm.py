import pygame as pg

from scenes.base import Scene

from constants import COLORS, MENU_CURSOR_FILE
from debug_tools.time import timeit

pg.font.init()

class ConfirmPrompt(Scene):

    def __init__(self, msg):
        self.confirm = False
        # self.sfont = pg.font.SysFont("Arial", 32)
        self.cursor = pg.image.load(MENU_CURSOR_FILE).convert()
        # prepare field surfaces
        self.question = self.sfont.render(msg, True, COLORS["white"])
        # self.question = self.surround_with_rect(self.question)
        self.yes = self.sfont.render("Yes", True, COLORS["white"])
        # self.yes = self.surround_with_rect(self.yes)
        self.no = self.sfont.render("No", True, COLORS["white"])
        # self.no = self.surround_with_rect(self.no)

        # a bug will probably happen if the question is shorter than yes/no
        qx, qy = self.question.get_size()
        yx, yy = self.yes.get_size()
        nx = self.no.get_size()[0]
        total_x = qx
        # yes and no have the same height
        total_y = yy + 50 + qy
        # 20 are the borders (for the rectangle)
        self.window = pg.Surface((total_x + 20, total_y + 20))
        
    def update(self, delta):
        pass
    def render(self, screen):
        self.manager.render_old(screen, 2)

        qx, qy = self.question.get_size()
        yx, yy = self.yes.get_size()
        nx, ny = self.no.get_size()

        self.window.fill(COLORS["black"])
        # activate transparency
        # self.window.set_colorkey(COLORS["black"])
        pg.draw.rect(self.window, COLORS["white"], self.window.get_rect(), 5)
        self.window.blit(self.question, (10,10))

        x, y = self.window.get_size()
        # 30 px under the question
        ybx = x / 4 # yes blit x
        yby = 10 + qy + 30 # yes blit y
        nbx = x / 2 + 50 # no blit x
        nby =  10 + qy + 30 # no blit y
        self.window.blit(self.yes, (ybx, yby))
        if self.confirm:
            self.window.blit(self.cursor, (ybx + yx + 10, yby + 20))
        else:
            self.window.blit(self.cursor, (nbx + nx + 10, nby + 20))
        self.window.blit(self.no, (nbx, nby))

        x, y = self.get_mid_surf_pos(screen, self.window)
        screen.blit(self.window, (x, y))

    def handle_events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT or e.key == pg.K_RIGHT:
                    if self.confirm:
                        self.confirm = False
                    else:
                        self.confirm = True
                elif e.key == pg.K_RETURN:
                    if self.confirm:
                        self.manager.go_back(2)
                    else:
                        self.manager.go_back()
