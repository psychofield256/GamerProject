import pygame as pg

from pygame.locals import *
# from pytmx import load_pygame
import pytmx

from scenes.base import Scene
from tools.pg.rects import multiply
# from scenes.menus.main import MainMenu

class TowerFloor1(Scene):
    "Tower in which the player starts playing (floor 1)"

    def __init__(self, player, position=(3, 3)):
        super(TowerFloor1, self).__init__()
        self.tmxdata = pytmx.load_pygame("resources/maps/tower_test2.tmx")
        self.player = player
        self.player.x, self.player.y = position
        self.playermovkeyon = False

    def update(self, delta):
        if self.playermovkeyon:
            if self.player.moving:
                self.player.step(delta, self.tmxdata)
            else:
                self.player.moving = True
        else:
            if self.player.moving:
                if self.player.exact_cell():
                    self.player.moving = False
                else:
                    self.player.step(delta, self.tmxdata)
        self.player.update(delta, self.tmxdata)

        # handle the map change
        # get the stairs
        stairs = self.tmxdata.get_object_by_name("DownStairs")
        # get its rect
        stairs = pg.Rect((stairs.x, stairs.y), (stairs.width, stairs.height))
        # rescale it
        multiply(stairs)
        # test the collision
        if self.player.rect.colliderect(stairs):
            # for now, they just lead to the menu
            self.manager.go_back()

    def render(self, screen):
        # size_w, size_h = screen.get_size()
        # w, h = self.tmxdata.width, self.tmxdata.height
        # wanted_w, wanted_h = (int(size_w / w), int(size_h / h))
        # print(wanted_w, wanted_h)
        wanted_w, wanted_h = 32, 32
        if self.tmxdata.background_color:
            screen.fill(pygame.Color(self.tmxdata.background_color))

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    image = pg.transform.scale(image, (wanted_w, wanted_h))
                    screen.blit(image, (x * wanted_w, y * wanted_h))
        ppos = self.player.get_pixel_pos((32, 32))
        screen.blit(self.player.get_image((32, 32)), ppos)

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if self.player.exact_cell():
                    if e.key == K_UP:
                        self.player.move_up()
                        self.playermovkeyon = True
                    elif e.key == K_DOWN:
                        self.player.move_down()
                        self.playermovkeyon = True
                    elif e.key == K_LEFT:
                        self.player.move_left()
                        self.playermovkeyon = True
                    elif e.key == K_RIGHT:
                        self.player.move_right()
                        self.playermovkeyon = True
            elif e.type == KEYUP:
                if e.key == K_UP and self.player.direction == "up":
                    self.playermovkeyon = False
                elif e.key == K_DOWN and self.player.direction == "down":
                    self.playermovkeyon = False
                elif e.key == K_LEFT and self.player.direction == "left":
                    self.playermovkeyon = False
                elif e.key == K_RIGHT and self.player.direction == "right":
                    self.playermovkeyon = False
