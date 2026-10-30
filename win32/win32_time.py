'''
	This is the equivalent of Micropython's way of time.

	DELETE THIS ENTIRE FILE IF ON MICROPYTHON.
'''

from time import perf_counter

def ticks_ms():
	'''
		Returns how many ticks (miliseconds) have passed since the start of the program in miliseconds.
	'''
	return perf_counter()
def ticks(): return perf_counter()
def ticks_diff(tick1, tick2): return tick1 - tick2