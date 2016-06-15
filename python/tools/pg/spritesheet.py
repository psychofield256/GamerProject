import pygame

pygame.init()

class SpriteSheet(object):
    "Small class used to handle spritesheets in pygame"

    def __init__(self, filename, sprite_size=(16, 16)):
        try:
            self.spritesheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print("unable to load:", filename)
            raise e
        self.width, self.height = self.spritesheet.get_size()
        self.sprite_width, self.sprite_height = sprite_size
        self.xlen = self.width / self.sprite_width
        self.ylen = self.height / self.sprite_height

    def get_sub(self, x, y, w, h):
        "Return a subsurface of the spritesheet."
        return self.spritesheet.subsurface(x, y, w, h)

    def get_sprite(self, x, y, size=None, colorkey=None):
        """
        Return the sprite at coords (x,y).

        args:
         -colorkey: the transparent color used
         -size: the size to give to the sprite
        """
        position = (x * self.sprite_width, y * self.sprite_height)
        sprite_size = (self.sprite_width, self.sprite_height)
        rect = pygame.Rect(position, sprite_size)
        img = self.spritesheet.subsurface(rect)
        if size is not None:
            img = pygame.transform.scale(img, size)
        if colorkey:
            if colorkey == -1:
                colorkey = img.get_at((0, 0))
            img.set_colorkey(colorkey)
        return img
        # return self.spritesheet.subsurface(x, y, self.sprite_width, self.sprite_height)

    def get_frame(self, y, h):
        "Return all the images of an animation in an image"
        return self.spritesheet.subsurface(0, y, self.width, h)

    def get_frames(self, h):
        "Return a list of all the frames (need a height arg)"
        frames = int(self.height / h)
        return [self.get_frame(y, h) for y in range(frames)]
