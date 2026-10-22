'''
main.py. The main execution of the SigmaEngine. It's composed of an uncaught exception handler, a loader, and a starter.
'''

import sys
import pygame
from src.scene import Scene


__firstFile__: str = str()
'''
	The NAME of the first FILE that will load up.
	Defined in scenes/first_file.txt.
'''

# do NOT CONFUSE THESE TWO. THEY ARE COMPLETELY DIFFERENT, but related.

__firstScene__: Scene = None
'''
	The ACTUAL first scene that will load up. (THIS is a SCENE OBJECT)
	Defined as FirstScene in the file which name is inside scenes/first_file.txt.
'''


# Shorter for "namespace"
ns = {}
'''
	Encapsulator for being able to open a file and blah blah blah.
	I know what I got!
'''

pressed_AC: bool = False


def mainExecution():
	'''
		Contains the load of the first scenes,
		and the execution of the infinite and well-known "update" functions…
		Called in UncaughtExceptionHandler()
	'''
	print("loading up.")
	# load the scene.
	s: Scene = __firstScene__()
	s.load()

	# update indefinitely the scene.
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		# check in case of the user wanting to close the Pygame loop
		s.update()
		s.afterUpdate()


def uncaughtExceptionHandler():
	'''
		Simple yet effective uncaught Exception Handler.
		In case of the user presses the AC key without knowing or inconsciouslly.
		Or, if SigmaEngine doesn't work at ALL.
	'''
	try:
		global ns, __firstScene__
		ns = {} # reset ns in case of it not being absolutely destroyed earlier.

		sys.path.insert(0, 'src')

		# Load the file. LOAD IT UUUPPP
		exec(open(__firstFile__).read(), ns)

		# The first scene is ALWAYS CALLED FirstScene.
		__firstScene__ = ns['FirstScene']

		# Now... it's time to shine.
		mainExecution()
	except Exception as e:
		global pressed_AC
		print('ERR: ' + str(e))
		if (pressed_AC): # if the user doesn't want to, we don't.
			return
		
		# This system does it so the user has to press 3 times the AC button for SigmaEngine to exit.
		pressed_AC = True
		
		uncaughtExceptionHandler() # Just get it on and try again, dumb.


def startEngine():
	# okay. Let's try to know what file is the first one (we already know that the first scene is called FirstScene, duh.).
	try:
		with open('scenes/first_file.txt', 'r', encoding='utf-8') as f:
			global __firstFile__
			__firstFile__ = f.read().strip()
			f.close()

		return True
	except Exception as e:
		print("ERROR: Could NOT load the first scene!: " + str(e))
		return False

# Load it up!
if (startEngine()):
	print('INFO: Loading SigmaEngine...')
	uncaughtExceptionHandler()
else:
	print('FATAL ERROR: Could NOT load the first scene AT ALL.')
	print('SigmaEngine needs to be executed again to work!')


