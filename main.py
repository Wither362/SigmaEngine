'''
	main.py. The main execution of the SigmaEngine. It's composed of an uncaught exception handler, a loader, and a starter.
'''

import sys
import time
import pygame
from sge.scene import Scene


__firstFile__: str = str()
'''
	The NAME of the first FILE that will load up.
	Defined in `scenes/first_file.txt`.
'''

# do NOT CONFUSE THESE TWO. THEY ARE COMPLETELY DIFFERENT, but related.

__firstScene__: Scene = None
'''
	The ACTUAL first SCENE that will load up. (THIS is a SCENE OBJECT)
	Defined as `FirstScene` in the file whose name is inside `scenes/first_file.txt`.
'''


# Shorter for "namespace"
ns = {}
'''
	Encapsulator for being able to open a file and blah blah blah.
	I know what I got!
'''

pressed_AC: bool = False


def MainExecution():
	'''
		Contains the load of the first scenes,
		and the execution of the infinite and well-known "update" functions…
		Called in `UncaughtExceptionHandler()`.
	'''
	print("loading up.")
	# load the scene.
	s: Scene = __firstScene__()
	s.Load()

	# short for "last time"
	lt: float = float()
	now: float = float()


	# this is SUCH A MESS OF A CODE, but it's meant to be COMPATIBLE BETWEEN PYTHON AND MICROPYTHON
	if hasattr(time, 'perf_counter'): # python
		def _now(): return time.perf_counter()
		def _diff(a, b): return (b - a) * 1000
	else: # micropython
		def _now(): return time.ticks_ms()
		def _diff(a, b): return time.ticks_diff(b, a)



	# update indefinitely the scene.
	while True:
		# check whether the dev wants to close the Pygame loop
		# THIS IS MEANT TO BE DELETED WHEN TRANSFERING TO MMICROPYTHON.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		# DONT DELETE THE REST

		now = _now() # change this for time.ticks_ms() for micropython

		# send `dt` as deltaTime as the difference between this and last frame, and divided by 1000 because it's in seconds and not in miliseconds.
		if (s.Update(dt = (now - (lt if lt else now)) / 1000)):
			# `Scene.Update()` can return a str value that represents whether the scene wants to change to another Scene or not. So, we check if that's true.
			# so it wants to change, since we are in this upper side of the conditional if.
			s

		s.AfterUpdate()
		lt = _now()


def UncaughtExceptionHandler():
	'''
		Simple yet effective Uncaught Exception Handler.
		In case of the user presses the AC key without knowing or unconsciously.
		Or, if SigmaEngine doesn't work at ALL.
	'''
	try:
		global ns, __firstScene__
		ns = {} # reset ns in case of it not being absolutely destroyed earlier.

		sys.path.insert(0, 'src')

		# Load the file. LOAD IT UUUPPP
		exec(open(__firstFile__).read(), ns)

		# The first scene is ALWAYS CALLED `FirstScene`.
		__firstScene__ = ns['FirstScene']

		# Now... it's time to shine.
		MainExecution()
	except Exception as e:
		global pressed_AC
		print('ERR: ' + str(e))
		if (pressed_AC): # if the User/Player wants to exit, we exit.
			return
		
		# This system does it so the user has to press 3 times the AC button for SigmaEngine to exit.
		pressed_AC = True
		
		UncaughtExceptionHandler() # Just get it on and try again, dumb.


def StartEngine():
	# okay. Let's try to know what file is the first one (we already know that the first scene is called `FirstScene`, duh.).
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
if (StartEngine()):
	print('INFO: Loading SigmaEngine...')
	UncaughtExceptionHandler()
else:
	print('FATAL ERROR: Could NOT load the first scene AT ALL.')
	print('SigmaEngine needs to be executed again to work!')




