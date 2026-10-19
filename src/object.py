
from pointer import Pointer

class Object(Pointer):
	shape: int
	zLayer: int

	def __init__(self, shape: int):
		'''`shape` needs to be one of these values:
		- `0` = circle
		- `1` = rectangle/square
		- `2` = polygon.'''
		super().__init__()
		self.x = 0.0
		self.y = 0.0
		self.shape = shape
		
