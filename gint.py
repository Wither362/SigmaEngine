# This is just a silly library for coders who don't want to transfer the code from their computer to their calculator
# AGAIN AND AGAIN AND AGAIN.

import pygame as pg


# --- GINT VARIABLES ---
# Screen, specifically, the CG50's resolution specs
DWIDTH = 384
DHEIGHT = 216

# Colors (These values are NOT the ones that are used in gint)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_DARK = (50, 50, 50)
C_LIGHT = (170, 170, 170)
C_BLUE = (0, 0, 255)

C_NONE = "C_NONE"


# Key Events Types
KEYEV_NONE = KEYEV_DOWN = KEYEV_HOLD = 0

# Keys
KEY_XOT = KEY_LOG = KEY_LN = KEY_SIN = KEY_COS = KEY_TAN = KEY_FRAC = KEY_FD = KEY_LEFTP = KEY_RIGHTP = KEY_COMMA = KEY_ARROW = KEY_MUL = KEY_DIV = KEY_ADD = KEY_SUB = KEY_DOT = KEY_EXP = KEY_NEG = KEY_SQUARE = KEY_POWER = 0
KEY_MENU = KEY_F5 = KEY_UP = KEY_DOWN = KEY_RIGHT = KEY_LEFT = KEY_EXE = KEY_F1 = KEY_F2 = KEY_F3 = KEY_F4 = KEY_EXIT = KEY_DEL = KEY_0 = KEY_1 = KEY_2 = KEY_3 = KEY_4 = KEY_5 = KEY_6 = KEY_7 = KEY_8 = KEY_9 = 0

# Text utils
DTEXT_TOP = DTEXT_MIDDLE = DTEXT_BOTTOM = 0
DTEXT_LEFT = DTEXT_CENTER = DTEXT_RIGHT = 0

# --- END OF GINT VARIABLES


# Sooo... This part of this silly ahh library uses the pg library to replicate gint's behaviour.

pg.init()


pg_screen = pg.display.set_mode((DWIDTH, DHEIGHT))
PG_CLOCK = pg.time.Clock()


def pg_convert_gint_color_to_pg_color(color_16bit):
	r5 = (color_16bit >> 11) & 0x1F
	g6 = (color_16bit >> 5) & 0x3F
	b5 = color_16bit & 0x1F

	red = (r5 * 255) // 31
	green = (g6 * 255) // 63
	blue = (b5 * 255) // 31
	del(r5, g6, b5, color_16bit)
	return (red, green, blue)

def pg_color(color):
	'''
		Returns the color in pygame color code.
	'''
	if(isinstance(color, str)):
		color = (0, 0, 0)
	if (not isinstance(color, tuple)):
		color = pg_convert_gint_color_to_pg_color(color)

	return color

def read() -> str:
	return
def write(self, string : str):
	return
def close():
	return
def drect(x1: int, y1: int, x2: int, y2: int, c):
	'''
		Draws a rect from (x1, y1) to (x2, y2), with color `c`.
	'''
	x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
	c = pg_color(c)
	
	pg.draw.rect(pg_screen, c, pg.Rect(x1, y1, abs(x2 - x1), abs(y2 - y1)))
	
	return
def drect_border(x1: int, y1, x2, y2, fill_color, border_width, border_color):
	return
def dclear(newBackgroundColor):
	'''
		Adds a rectangle on screen that covers the whole view with the specified color.
	'''
	newBackgroundColor = pg_color(newBackgroundColor)
	pg_screen.fill(newBackgroundColor)
	return
def dtext(x: int, y: int, color, text: str):
	'''
		Adds a simple text to the screen with position (`x`, `y`), color `color`, and string `text`.
	'''
	return
def dcircle(x: int, y: int, r: int, c):
	'''
		Adds a circle to the screen with center position (`x`, `y`), radius `r` and color `c`.
	'''
	x, y, r = int(x), int(y), int(r)
	c = pg_color(c)
	pg.draw.circle(pg_screen, c, (x, y), r)
	return
def dtext_opt(x: int, y: int, foreground_color, background_color, horizontal_alignment, vertical_alignment, string: str, size: int = -1) -> None:
	"""	
	:param x: Description
	:type x: int
	:param y: Description
	:type y: int
	:param foreground_color: Description
	:param background_color: Description
	:param horizontal_alignment: DTEXT_LEFT, DTEXT_CENTER, DTEXT_RIGHT
	:param vertical_alignment: DTEXT_TOP, DTEXT_MIDDLE, DTEXT_BOTTOM
	:param string: Description
	:type string: str
	:param size: Description
	:type size: int
	"""
	return
def dsize(str, font = None, w = None, h = None):
	return
def dupdate():
	'''
		Updates the screen.
	'''
	pg.display.flip()
	PG_CLOCK.tick(60)
	return
def C_RGB(r, b, g):
	''' Returns '''
	return int()
def keycode_digit(keycode: int):
	return int()

def pollevent():
	return
