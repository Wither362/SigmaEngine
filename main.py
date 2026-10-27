'''
	main.py. The main execution of the SigmaEngine. It's composed of an uncaught exception handler, a loader, and a starter.
'''

# Dependencies for Python 3.13 and all that
import pygame

# Micropython dependencies
from uio import StringIO

# Normal dependencies required on both sides
import sys
import time
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

# Micropython code
def ExceptionPrinter(e):
	s = StringIO()
	sys.print_exception(e, s)
	print(str(s.getvalue()))


def MainExecution():
	'''
		Contains the load of the first scenes,
		and the execution of the infinite and well-known "update" functions.
		Called in `UncaughtExceptionHandler()`.
	'''
	try:
		# load the scene.
		s: Scene = __firstScene__()
		s.Load()

		# short for "last time"
		lt: float = -1.0
		now: float = float()
	 
		# UPDATE indefinitely the scene. (This is the MAIN LOOP)
		while True:
			# check whether the dev wants to close the Pygame loop
			# THIS IS MEANT TO BE DELETED WHEN TRANSFERING TO MMICROPYTHON.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()


			# DONT DELETE THE REST

			now = time.ticks_ms() # change this for time.ticks_ms() for micropython

			# send `dt` as deltaTime as the difference between this and last frame, and divided by 1000 because it's in seconds and not in miliseconds.
			if (s.Update(dt = (now - (lt if lt != -1.0 else now)) / 1000)):
				# `Scene.Update()` can return a str value that represents whether the scene wants to change to another Scene or not. So, we check if that's true.
				# so it wants to change, since we are in this upper side of the conditional if.
				s

			s.AfterUpdate()
			lt = time.ticks_ms()
	except Exception as e:
		# Return the error to the UncaughtExceptionHandler cause he's a very good boy
		raise e


def UncaughtExceptionHandler():
	'''
		Simple yet effective Uncaught Exception Handler.
		In case of the user presses the AC key without knowing or unconsciously.
		Or, if SigmaEngine doesn't work at ALL.
	'''
	try:
		global ns, __firstScene__
		ns = {} # reset ns in case of it not being absolutely destroyed earlier.

		sys.path.insert(0, 'sigma')

		# Load the file. LOAD IT UUUPPP
		exec(open(__firstFile__).read(), ns)

		# The first scene is ALWAYS CALLED `FirstScene`.
		__firstScene__ = ns['FirstScene']

		# Now... it's time to shine.
		MainExecution()

	except KeyboardInterrupt as e: # the player pressed the AC button
		global pressed_AC

		if (pressed_AC): # if the User/Player wants to exit, we exit.
			return

		pressed_AC = True

		UncaughtExceptionHandler() # Just get it on and try again, dumb.

	except Exception as e:
		print('---UNCAUGHT EXCEPTION HANDLER ERROR---')
		print('ERR: ' + str(e))
		ExceptionPrinter(e)
		
		UncaughtExceptionHandler() # Just get it on and try again, dumb.


def StartEngine():
	# okay. Let's try to know what file is the first one (we already know that the first scene is called `FirstScene`, duh.).
	try:
		with open('sigma/scenes/first.py') as f:
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
	print('---FATAL ERROR---')
	print('SigmaEngine needs to be executed again to work!')
	print('------------------')


