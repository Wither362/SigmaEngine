import pygame, sys
import desktop.desktop_time as time

def exit():
	pygame.quit()
	sys.exit()

def mainExecution():
	'''A function to make the main.py file easier to read because of micropython and python differences.'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			# pause main execution. ONLY ON WIN32 SGE VERSION
			if event.key == pygame.K_F2:
				lastTitle = pygame.display.get_caption()[0]
				pygame.display.set_caption('PAUSED')
				time.__start_paused_ticks__()
				while True:
					ev = pygame.event.wait()
					# completely exit execution
					if ev.type == pygame.QUIT:
						exit()
					# resume execution
					elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_F2:
						pygame.display.set_caption(lastTitle)
						time.__end_paused_ticks__()
						break
			# elif event.key == ...