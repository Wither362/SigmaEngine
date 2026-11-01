'''
	This is the equivalent of Micropython's way of time.

	DELETE THE ENTIRE `\desktop\` FOLDER IF ON MICROPYTHON.
'''

import time


paused_timer = 0
'''stores the time that has passed when the game's paused (only on sge desktop edition)'''
paused_timer_start = 0
'''stores the time that IS being skipped if the game's paused.'''


def ticks_ms():
	'''
		Returns how many ticks (miliseconds) have passed since the start of the program in miliseconds.
	'''
	if (paused_timer > 0):
		return time.ticks_ms() - paused_timer
	return time.ticks_ms()
def ticks():
	return ticks_ms() / 1000
def ticks_diff(tick1, tick2): return tick1 - tick2

def __start_paused_ticks__():
	global paused_timer_start
	paused_timer_start = ticks_ms()

def __end_paused_ticks__():
	global paused_timer
	paused_timer += ticks_ms() - paused_timer_start
