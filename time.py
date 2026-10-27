'''
	This is the equivalent of Micropython's way of time.

	DELETE THIS ENTIRE FILE IF ON MICROPYTHON.
'''

import time

def ticks_ms():
	'''
		Returns how many ticks (miliseconds) have passed since the start of the program in miliseconds.
	'''
	return time.perf_counter() / 1000
def ticks(): return time.perf_counter()