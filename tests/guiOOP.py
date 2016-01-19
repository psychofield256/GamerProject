#!/usr/bin/env python
#made while learning with thepythongamebook.com/en:pygame:step004
#will try http://usingpython.com/python-rpg-game/ to make a random dungeon
#http://gamedevelopment.tutsplus.com/tutorials/create-a-procedurally-generated-dungeon-cave-system--gamedev-10099
#

import pygame

class PygView():
	def __init__(self, width=640, height=480, fps=20):
		"""initialize pygame, window, background, font,..."""
		pygame.init()
		pygame.display.set_caption("Press ESC to Quit")
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
		self.background = pygame.Surface(self.screen.get_size()).convert() #convert for faster rendering
		self.background.fill((255,255,255))
		self.clock = pygame.time.Clock()
		self.fps = fps
		self.font = pygame.font.SysFont('mono', 20, bold=True)
		

	def run(self):
		"""Mainloop"""
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False

			self.clock.tick(self.fps)

			radius = 200 #radius
			color = (200,200,200) #color

			#main circle
			#define some points. google "pentagram tutorial" to understand the positions
			a,b = (320,440), (320,40)
			c,d = (120,240), (520,240)
			o = (320,240) #center
			pygame.draw.circle(self.background, color, o, radius)

			surf = pygame.Surface((320,240))
			surf.set_colorkey((0,0,0))
			pygame.draw.circle(surf, (100,100,100), (150,100), 50)
			surf.convert_alpha()




			#pygame.draw.circle(self.background, (255,192,203), (self.screen.get_size()[0]//2, self.screen.get_size()[1]//2), 200)
			self.screen.blit(self.background, (0,0))
			self.screen.blit(surf, (320,240))


			#pygame.draw.arc(self.background, (0,150,0),(400,10,150,100), 0, 3.14) 
			pygame.display.flip()

		pygame.quit()

	def draw_text(self, text):
		"""center text"""
		fw, fh = self.font.size(text) #fw: fontweight, fh: fontheight
		surface = self.font.render(text, True, (0, 255, 0))
		#print in the middle of the screen
		self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

	def set_title(self, text):
		pygame.display.set_caption(text)

if __name__ == "__main__":
	PygView().run()