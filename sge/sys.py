'''
	File system module.
'''

import sys
from io import StringIO

# IF NOT IN MICROPYTHON
if (sys.platform == 'linux' or sys.platform == 'darwin' or sys.platform == 'win32'):
	from desktop.desktop_file_system import open


def ExceptionPrinter(e):
	s = StringIO()
	sys.print_exception(e, s)
	print(str(s.getvalue()))
	del(s)


def save(d: dict):
	'''
		Saves `d` (which is a dictionary) in the normal save path for SGE.

		Returns if True if the operation was successful, returns False if not.
	'''
	try:
		with open('sigma/saves/data.py', 'w') as f:
			f.write(repr(d))
			return True

	except Exception as e:
		print('ERROR: Error saving data:')
		ExceptionPrinter(e)
	return False

def load():
	'''
		Loads data from the normal save path for SGE.
	'''
	try:
		with open('sigma/saves/data.py') as f:
			return eval(f.read())

	except Exception as e:
		print('ERROR: Error loading saved data:')
		ExceptionPrinter(e)
	return None

