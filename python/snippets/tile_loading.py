import pygame as pg
import configparser


def load_tile_table(filename, width, height):
    img = pg.image.load(filename).convert()
    img_width, img_height = img.get_size()
    tile_table = []
    for tile_x in range(0, int(img_width / width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(img_height / height)):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(img.subsurface(rect))
    return tile_table

    class Level(object):
        """docstring for Level"""

        def load_file(self, filename="level.map"):
            self.map = []
            self.key = {}
            parser = configparser.ConfigParser()
            parser.read(filename)
            self.tileset = parser.get("level", "tileset")
            self.map = parser.get("level", "map").split("\n")
            for section in parser.sections():
                if len(section) == 1:
                    desc = dict(parser.items(section))
                    self.key[section] = desc
            self.width = len(self.map[0])
            self.height = len(self.map)

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((640, 480))
    screen.fill((255, 255, 255))
    table = load_tile_table("ground.png", 24, 16)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*24, y*16))
    pg.display.flip()
    while pg.event.wait().type != pg.QUIT:
        pass
