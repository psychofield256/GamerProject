import pygame

pygame.init()

class SpriteSheet(object):
    "Small class used to handle spritesheets in pygame"

    def __init__(self, filename, sprite_width=16, directions="dlru"):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print('unable to load:', filename)
            raise e
        self.totw, self.toth = self.sheet.get_size()
        self.sprw = sprite_width
        self.sprh = self.toth // len(directions)
        self.xlen = self.totw / self.sprw
        self.ylen = self.toth / self.sprh

        frames = {}
        for i, d in enumerate(directions):
            frames[d] = self.sheet.subsurface(0, i * self.sprh,
                                              self.totw, self.sprh)
        self.frames = frames

    def get_sub(self, x, y, w, h):
        "Return a subsurface of the spritesheet."
        return self.spritesheet.subsurface(x, y, w, h)

    def get_sprite(self, x, d, size=None, colorkey=None):
        """
        return the sprite number x at the frame of the direction d.

        args:
         -colorkey: the transparent color used
         -size: the size to give to the sprite
        """
        sprsize = (self.sprw, self.sprh)
        frame = self.frames[d]
        # size[0] if we want to count with a custom size from
        # the start of the frame
        # if not, it should be self.sprw
        spr = frame.subsurface(x * self.sprw, 0, self.sprw, self.sprh)
        if size is not None:
            spr = pygame.transform.scale(spr, size)
        if colorkey:
            if colorkey == -1:
                colorkey = spr.get_at((0, 0))
            spr.set_colorkey(colorkey)
        return spr
