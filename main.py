'''
	main.py. The main execution of the SigmaEngine. It's composed of an uncaught exception handler, a loader, and a starter.
'''

# Normal dependencies required on both sides
import sys
from sge.scene import Scene
from io import StringIO

# Micropython dependencies
if (sys.platform != 'linux' and sys.platform != 'darwin' and sys.platform != 'win32'):
	import time

# Dependencies for Python 3.13 and all that. Delete this if in micropython.
if (sys.platform == 'linux' or sys.platform == 'darwin' or sys.platform == 'win32'):
	from desktop.desktop_file_system import open
	import desktop.desktop_time as time
	import desktop.desktop_py_events as pyevents


__firstModule__: str = ''
'''
	The NAME of the first MODULE (so it needs to be in a format like `scene`, or `folderInsideScenes.scene`) that will load up.
	Defined in `scenes/first.py`.
'''


pressed_AC: bool = False


# Micropython code
def ExceptionPrinter(e):
	 # Delete this 'if' if you are doing this in micropython, BUT NOT THE CODE BELOw.
	if (sys.platform != 'linux' and sys.platform != 'darwin' and sys.platform != 'win32'):
		# DO NOT DELETE THE CODE BELOW
		s = StringIO()
		sys.print_exception(e, s)
		print(str(s.getvalue()))
		del(s)
	# THIS ONE YEES, DELETE THIS.
	else:
		print('ERR: ' + str(e))
	# stop deleting.


def ChangeScene(sMN: str, sN: str):
	'''
	`sMN` is `scene module name`, `sN` is `scene name`.\n
	Returns the `Scene` inside the module `sMN` 
	'''
	return getattr(__import__('scenes.' + sMN, fromlist=[""]), sN)


def MainExecution(fS):
	'''
		`fS` is shorter for `first scene`, which is `Scene` class.\n
		Contains the load of the first scenes, and the execution of the infinite and well-known "update" functions.\n
		Called in `UncaughtExceptionHandler()`.
	'''
	try:
		# load the scene.
		s: Scene = fS()
		s.Load()

		# short for "last time"
		lt: float = -1.0
		now: float
	
		# UPDATE indefinitely the scene. (This is the MAIN LOOP)
		while True:
			now = time.ticks_ms()

			# check pygame events
			# THIS IS MEANT TO BE DELETED WHEN TRANSFERING TO MMICROPYTHON.
			pyevents.mainExecution()
			# DONT DELETE THE REST

			# send `dt` as deltaTime. You should already now what deltatime is.
			sMN, sN = s.Update(dt = (time.ticks_diff(now, lt if lt != -1.0 else now) / 1000.0))
			# sMN is the shorter form of `scene module name`, and sN of `scene name`.

			# If those two aren't `None`, then the Scene wants to change places with a new Scene.
			if (not sMN and not sN):
				s.AfterUpdate()
			else: # change scene.
				s = ChangeScene(sMN, sN)

			lt = now

	except Exception as e:
		# Return the error to the UncaughtExceptionHandler cause he's a very good boy
		raise e

def UncaughtExceptionHandler():
	'''
		Simple yet NOT-effective Uncaught Exception Handler.
		In case of the user presses the AC key without knowing or unconsciously.
		Or, if SigmaEngine doesn't work at ALL.
	'''
	try:
		# Now... it's time to shine.
		MainExecution(ChangeScene(__firstModule__, 'FirstScene')) # the first scene is ALWAYS CALLED FirstScene

	except KeyboardInterrupt as e: # the player pressed the AC button
		global pressed_AC

		if (pressed_AC): # if the User/Player wants to exit, we exit.
			return

		pressed_AC = True

		UncaughtExceptionHandler() # Just get it on and try again, dumb.

	except Exception as e: # All the other exceptions
		print('---UNCAUGHT EXCEPTION HANDLER ERROR---')
		ExceptionPrinter(e)
		
		# UncaughtExceptionHandler() # Just get it on and try again, dumb.


def StartEngine():
	# okay. Let's try to know what file is the first one (we already know that the first scene is called `FirstScene`, duh.).
	try:
		with open('sigma/scenes/firstModule.py', "r") as f:
			global __firstModule__
			__firstModule__ = f.read().strip()
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


