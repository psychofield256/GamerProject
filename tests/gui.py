#!/usr/bin/env python
import pygame as pg

pg.init()

screen = pg.display.set_mode((640, 480)) #creates the window

background = pg.Surface(screen.get_size()) #creates empty pg surface

background.fill((255,255,255)) #fill background in white

background = background.convert() #accelerates blitting

screen.blit(background, (0,0))
#creates a clock object
clock = pg.time.Clock()

FPS = 20
playtime = 0.0

mainloop = True
while mainloop:
	miliseconds = clock.tick(FPS) #lock the framerate and saves the time
	playtime += miliseconds / 1000 #in seconds

	for event in pg.event.get():
		#pg window closed by user
		if event.type == pg.QUIT:
			mainloop = False
		elif event.type == pg.KEYDOWN:
			#escape key
			if event.key == pg.K_ESCAPE:
				mainloop = False

	title = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
	#set the title
	pg.display.set_caption(title)

	#print the screen
	pg.display.flip()
	

print(playtime)