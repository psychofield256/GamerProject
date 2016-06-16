import pygame as pg

from pygame.locals import *
# from pytmx import load_pygame
import pytmx

from scenes.base import Scene

class TowerFloor1(Scene):
    "Tower in which the player starts playing (floor 1)"

    def __init__(self, player, position=(3, 3)):
        super(TowerFloor1, self).__init__()
        self.tmxdata = pytmx.load_pygame("resources/maps/tower_test2.tmx")
        self.player = player
        self.player.rect.x, self.player.rect.y = position
        self.playermovkeyon = False

    def update(self, delta):
        if self.playermovkeyon:
            if self.player.moving:
                self.player.step(delta, self.tmxdata)
            else:
                #if self.tmxdata
                self.player.moving = True
        else:
            if self.player.moving:
                if self.player.exact_cell():
                    self.player.moving = False
                else:
                    self.player.step(delta, self.tmxdata)
        self.player.update(delta, self.tmxdata)

        # handle the map change

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
        #  self.player.render(screen, self.tmxdata)
        ppos = self.player.get_pixel_pos((32, 32))
        screen.blit(self.player.get_image((32, 32)), ppos)

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if self.player.exact_cell():
                    if e.key == K_UP:
                        self.player.move_up()
                        self.playermovkeyon = True
                        #self.player.moving = True
                    elif e.key == K_DOWN:
                        self.player.move_down()
                        self.playermovkeyon = True
                        #self.player.moving = True
                    elif e.key == K_LEFT:
                        self.player.move_left()
                        self.playermovkeyon = True
                        #self.player.moving = True
                    elif e.key == K_RIGHT:
                        self.player.move_right()
                        self.playermovkeyon = True
                        # self.player.moving = True
            elif e.type == KEYUP:
                if e.key == K_UP and self.player.direction == "up":
                    # if self.player.move_complete():
                    self.playermovkeyon = False
                elif e.key == K_DOWN and self.player.direction == "down":
                    # if self.player.move_complete():
                    self.playermovkeyon = False
                elif e.key == K_LEFT and self.player.direction == "left":
                    # if self.player.move_complete():
                    self.playermovkeyon = False
                elif e.key == K_RIGHT and self.player.direction == "right":
                    # if self.player.move_complete():
                    self.playermovkeyon = False
