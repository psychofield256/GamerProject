#!usr/bin/env python

import pygame
from game_states import State
# import pytmx

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello world")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

loop = True
playtime = 0

game = State("game")


def write(surface, pos, txt):
    color = (0, 0, 0)
    txt_surf = font.render(txt, False, color)
    surface.blit(txt_surf, (pos))


def write_mid(surface, txt):
    width, height = font.size(txt)
    size_x, size_y = surface.get_size()
    pos = ((size_x - width) / 2, (size_y - height) / 2)
    write(surface, pos, txt)

state = State("menu")

while loop:
    dt = clock.tick(10)

    if state.name == "menu":
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                loop = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    loop = False
                elif e.key == pygame.K_RETURN:
                    state = State("game", state)
        print("in menu")
    elif state.name == "game":
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                loop = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    state.end()
                    print(state)
        print("in game")
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    background = background.convert()

    screen.blit(background, (0, 0))

    pygame.display.flip()

    playtime += dt
