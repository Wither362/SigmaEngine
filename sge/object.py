'''
	A SigmaEngine component that has a graphic (optional) and a position in a Scene.
'''

from gint import drect_border, dcircle, C_NONE

class Object:
	'''
		A SigmaEngine component that has a graphic and a position.\n
		All of its possible attributes have been stripped down to just one or two letters for memory optimizations.\n
		Take it in mind.
	'''

	x: float
	'''X position of the object'''
	y: float
	'''Y position of the object'''

	s: int
	'''Shorter for `shape`, since in Micropython, size is important.'''
	zL: int
	'''Shorter for `Z axis Layer`.'''
	iC: int
	'''Shorter for `innerColor`.'''
	bC: int = C_NONE
	'''Shorter for `borderColor`.'''
	bS: int = -1
	'''Shorter for `borderSize`.'''

	# Circle
	r: float
	'''Shorter for `radius`.'''

	# Rectangle
	hW: float
	'''Shorter for `halfWidth`, since gint has a different drawing system than height and width and origin.'''
	hH: float
	'''Shorter for `halfHeight`, since gint has a different drawing system than height and width and origin.'''

	# Polygon
	v: int
	'''Shorter for `vertices`.'''

	def __init__(self, shape: int):
		'''
			Creates a new Object.\n
			`object` needs to be one of these values:
			- `0` = circle
			- `1` = rectangle/square
			- `2` = polygon
		'''
		super().__init__()
		self.x = 0.0
		self.y = 0.0
		self.s = shape

		# Circle
		if (shape == 0):
			self.r = -1
		# Rectangle
		elif (shape == 1):
			self.hW = -1 # half width
			self.hH = -1 # half height
		# Polygon
		elif (shape == 2):
			self.v = -1
		# If shape isn't any of the values before, then this Object will NOT have a graphic.

	def Draw(self):
		if (self.s == 0):
			dcircle(int(self.x), int(self.y), int(self.r), self.iC, self.bC)
		elif (self.s == 1):
			drect_border(int(self.x - self.hW), int(self.y - self.hH), int(self.x + self.hW), int(self.y + self.hH), self.iC, self.bS, self.bC)
