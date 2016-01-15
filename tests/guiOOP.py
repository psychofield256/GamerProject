#!/usr/bin/env python


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
		self.clock = pygame.time.Clock()
		self.fps = fps
		self.playtime = 0.0
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

			miliseconds = self.clock.tick(self.fps)
			self.playtime += miliseconds / 1000.0
			self.draw_text("FPS : {0:.3f} PLAYTIME : {0:.3f} SECONDS".format(
				self.clock.get_fps(), self.playtime))

			pygame.display.flip()
			self.screen.blit(self.background, (0,0))

		pygame.quit()

	def draw_text(self, text):
		"""center text"""
		fw, fh = self.font.size(text) #fw: fontweight, fh: fontheight
		surface = self.font.render(text, True, (0, 255, 0))
		self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))


if __name__ == "__main__":
	PygView().run()