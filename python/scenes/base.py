import os
import pickle

import pygame as pg

from constants import COLORS

pg.font.init()

class Scene(object):
    """
    Base class for every scene.

    Contains some functions and constants to help other scenes.
    """

    # ordinary characters (used in name input for character creation)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    font = pg.font.SysFont("Arial", 56)
    sfont = pg.font.SysFont("Arial", 32)

    def __init__(self, manager):
        self.manager = manager

    def render(self, screen):
        raise NotImplementedError

    def update(self, delta):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

    def onleave(self):
        "Used for scenes which need to do something before leaving"
        pass

    def get_mid(self, surf):
        "return the middle of a surface"
        w, h = surf.get_size()
        w, h = w/2, h/2
        return (w, h)

    def get_title_pos(self, surf, title):
        "Return the place of the title, at the top of the screen"
        sc_x, sc_y = surf.get_size()
        ttl_x, ttl_y = title.get_size()
        # ttl_x, ttl_y = ttl_x / 2, ttl_y / 2
        return (sc_x / 2 - ttl_x / 2, sc_y / 5 - ttl_y / 2)

    def get_midtxt_pos(self, surf, txt):
        """Return the position to blit the text with its center.
        Works with any surface"""
        sc_x, sc_y = surf.get_size()
        txt_x, txt_y = txt.get_size()
        return (sc_x / 2 - txt_x / 2, sc_y / 2 - txt_y / 2)

    get_mid_surf_pos = get_midtxt_pos # get_midtxt_pos will be erased after

    def surround_with_rect(self, surf):
        "Return a new surface, 20 px larger, with a 5px rectangle"
        x, y = surf.get_size()
        new_surf = pg.Surface((x + 20, y + 20))
        pg.draw.rect(new_surf, COLORS["white"], new_surf.get_rect(), 5)
        new_surf.blit(surf, (10, 10))
        return new_surf

    def write_mid(self, screen, txt, color=COLORS["white"]):
        txt = self.sfont.render(txt, True, color)
        sx, sy = screen.get_size()
        tx, ty = txt.get_size()
        x, y = (sx/2 - tx/2, sy/2 - ty/2)
        screen.blit(txt, (x, y))

    def save(self, player, filename):
        with open(os.path.join("saves", filename), "wb") as f:
            pickle.dump(player, f, protocol=pickle.HIGHEST_PROTOCOL)

    """
    def rescale_map(self, tmxmap):
        tmxmap.tilewidth = 32
        tmxmap.tileheight = 32
        gids = set()
        for layer in tmxmap.layers:
            for x, y, gid in layer.iter_data():
                gids.update([gid])
        for gid in gids:
            print(gid)
            print(tmxmap.get_tile_properties_by_gid(gid))
    """
