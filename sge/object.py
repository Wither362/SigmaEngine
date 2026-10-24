'''
	A SigmaEngine component that has a graphic (optional) and a position in a Scene.
'''

from sge.pointer import Pointer
from gint import drect, dcircle

class Object(Pointer):
	'''
		A SigmaEngine component that has a graphic and a position.
	'''

	shape: int
	zLayer: int
	innerColor: int
	borderColor: None
	borderSize: int

	def __init__(self, shape: int):
		'''
			Creates a new Object.\n
			`object` needs to be one of these values:
			- `0` = circle
			- `1` = rectangle/square
			- `2` = polygon.
		'''
		super().__init__()
		self.x = 0.0
		self.y = 0.0
		self.shape = shape

		# Circle
		if (shape == 0):
			self.radius = -1
		# Rectangle
		elif (shape == 1):
			self.width = -1
			self.height = -1
		# Polygon
		elif (shape == 2):
			self.vertices = -1
		# If shape isn't any of the values before, then this Object will NOT have a graphic.
		elif (not shape):
			del(self.shape)

	def Rectangle(self, x, y, width, height, color):
		'''
			Sets the shape of tis object as a rectangle and sets its attributes.
			It's a great way to not forget want attributes you have to specify in order for SGE to work properly.
		'''
		self.shape = 1
		self.x, self.y = x, y
		self.width, self.height = width, height
		self.innerColor = color
		return self

	def Draw(self):
		if(not self.shape):
			return
		
		if (self.shape == 0):
			dcircle()
		elif (self.shape == 1):
			drect(float(self.x - (self.width // 2)), float(self.y - (self.height // 2)), float(self.x + (self.width // 2)), float(self.y + (self.height // 2)), self.innerColor)





