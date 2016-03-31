#!usr/bin/env python
"""
Module for testing new snippets and new implementations.
"""

import pygame
import pytmx


pygame.init()

screen = pygame.display.set_mode((640, 480))
screenrect = screen.get_rect()

clock = pygame.time.Clock()
mainloop = True
FPS = 20
playtime = 0
radus = 50
dr = 1

background = pygame.Surface(screen.get_size())
background.fill((255, 155, 155))
background = background.convert()
screen.blit(background, (0, 0))

ball_surf = pygame.Surface((50, 50))
ball_surf.set_colorkey((0, 0, 0))
pygame.draw.circle(ball_surf, (100, 175, 81), (25, 25), 25)

ball_surf = ball_surf.convert_alpha()

ball_rect = ball_surf.get_rect()

ballx, bally = 550, 240

dx = 10
dy = 0


x1 = 50
y1 = 200

dx1, dy1 = 7, 0
