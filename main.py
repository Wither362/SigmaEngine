'''
	main.py. The main execution of the SigmaEngine. It's composed of an uncaught exception handler, a loader, and a starter.
'''

# Normal dependencies required on both sides
from sge.scene import Scene
from sge.sys import ExceptionPrinter


import sys # delete also if in micropython

# Micropython dependencies
if (sys.platform != 'linux' and sys.platform != 'darwin' and sys.platform != 'win32'):
	import time

# Dependencies for Python 3.13 and all that. Delete this if in micropython.
if (sys.platform == 'linux' or sys.platform == 'darwin' or sys.platform == 'win32'):
	from desktop.desktop_file_system import open
	import desktop.desktop_time as time
	import desktop.desktop_py_events as pyevents

fM: str = ''
'''
	The NAME of the first MODULE (so it needs to be in a format like `scene`, or `folderInsideScenes.scene`) that will load up.
	Defined in `scenes/first.py`.
'''


pAC: bool = None


def ChangeScene(sMN: str, sN: str):
	'''
	`sMN` is `scene module name`, `sN` is `scene name`.\n
	Returns the `Scene` inside the module `sMN` 
	'''
	return getattr(__import__('scenes.' + sMN, None, None, [sN], 0), sN)


def UncaughtExceptionHandler():
	'''
		Simple yet half-effective Uncaught Exception Handler.
		In case of the user presses the AC key without knowing or unconsciously.
		Or, if SigmaEngine doesn't work at ALL.
	'''
	try:
		# the first scene is ALWAYS CALLED FirstScene
		m, n, a = fM, 'FirstScene', None

		while True: # Main load, update and destroy code.
			# load the scene.
			s: Scene = ChangeScene(m, n)()
			s.Load(a)
	
			lt: int = -1
			now: int
	
			# UPDATE indefinitely the scene. (This is the MAIN LOOP)
			while True:
				now = time.ticks_ms()
	
				# THIS IS MEANT TO BE DELETED WHEN TRANSFERING TO MICROPYTHON.
				pyevents.mainExecution()
	
				# send `dt` as deltaTime. You should already now what deltatime is.
				sM, sN = s.Update(dt = (time.ticks_diff(now, lt if lt != -1 else now) / 1000.0))
	
				# If those two aren't `None`, then the Scene wants to change places with a new Scene.
				if (not sM and not sN):
					s.AfterUpdate(dt = (time.ticks_diff(now, lt if lt != -1 else now) / 1000.0))
				else: # change scene.
					m, n, a = sM, sN, s.Destroy() # scene.Destroy can return a dict with data
	
				lt = now
	except KeyboardInterrupt as e:
		global pAC

		if (pAC == None):
			pAC = False
		elif (not pAC):
			pAC = True
		elif (pAC):
			return

		UncaughtExceptionHandler()

	except Exception as e: # All the other exceptions
		print('---UNCAUGHT EXCEPTION HANDLER ERROR---')
		ExceptionPrinter(e)


def StartEngine():
	try:
		with open('sigma/scenes/firstModule.py', "r") as f:
			global fM
			fM = f.read().strip()
			f.close()

		return True
	except Exception as e:
		# this doesn't go through the ExceptionPrinter to have two different systems for printing exceptions
		print("ERROR: Could NOT load the first scene!")
		return False


# Load it up!
if (StartEngine()):
	print('INFO: Loading SigmaEngine...')
	UncaughtExceptionHandler()
else:
	print('---FATAL ERROR---')
	print('SigmaEngine needs to be executed again to work!')
	print('------------------')


