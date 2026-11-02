'''
	A SigmaEngine component that has a graphic (optional) and a position in a Scene.
'''

from gint import C_NONE, DWIDTH, DHEIGHT


def on_screen(obj):
    x, y, w, h = obj.get_bbox()
    
    if x + w < 0 or x > DWIDTH or y + h < 0 or y > DHEIGHT:
        return False
    
    return True

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
	'''Shorter for `Z axis Layer`. For object ordering from back to the front.'''
	iC: int
	'''Shorter for `innerColor`.'''
	bC: int
	'''Shorter for `borderColor`.'''
	bS: int
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

	def get_bbox(obj, ):
		'''
		Returns the bounding box of the object `obj`
		'''

	def __screen__(obj, sW, sH):
		'''
		Returns True if the object's bounding box is at least partially on screen.
    	Returns False if the object is completely off-screen.
		'''

class CircObj:
	'''
		A SigmaEngine component that has a graphic and a position.\n
		All of its possible attributes have been stripped down to just one or two letters for memory optimizations.\n
		Take it in mind.
	'''

	s: int = 0
	'''
	Shorter for `shape`.
	- `0` = circle
	- `1` = rectangle/square
	- `2` = polygon
	'''

	x: float
	'''X position of the object'''
	y: float
	'''Y position of the object'''
	r: float
	'''Shorter for `radius`.'''

	zL: int
	'''Shorter for `Z axis Layer`. For object ordering from back to the front.'''
	iC: int
	'''Shorter for `innerColor`.'''
	bC: int = C_NONE
	'''Shorter for `borderColor`.'''

	def get_bbox(self):
		'''Returns the bounding box of this object'''
		r = self.r
		return (self.x - r, self.y - r, r * 2, r * 2)


class RectObj:
	'''
		A SigmaEngine component that has a graphic and a position.\n
		All of its possible attributes have been stripped down to just one or two letters for memory optimizations.\n
		Take it in mind.
	'''

	s: int = 1
	'''
	Shorter for `shape`.
	- `0` = circle
	- `1` = rectangle/square
	- `2` = polygon
	'''

	x: float
	'''X position of the object'''
	y: float
	'''Y position of the object'''
	hW: float
	'''Shorter for `halfWidth`, since gint has a different drawing system than height and width and origin.'''
	hH: float
	'''Shorter for `halfHeight`, since gint has a different drawing system than height and width and origin.'''
	
	zL: int
	'''Shorter for `Z axis Layer`. For object ordering from back to the front.'''
	iC: int
	'''Shorter for `innerColor`.'''
	bC: int = C_NONE
	'''Shorter for `borderColor`.'''
	bS: int = -1
	'''Shorter for `borderSize`.'''

	def get_bbox(self):
		'''Returns the bounding box of this object'''
		return (self.x, self.y, self.hW * 2, self.hH * 2)

class PolyObj:
	'''
		A SigmaEngine component that has a graphic and a position.\n
		All of its possible attributes have been stripped down to just one or two letters for memory optimizations.\n
		Take it in mind.
	'''

	s: int = 2
	'''
	Shorter for `shape`.
	- `0` = circle
	- `1` = rectangle/square
	- `2` = polygon
	'''

	x: float
	'''X position of the object'''
	y: float
	'''Y position of the object'''
	v: tuple[tuple[int]] #= ((0, 0), (10, 10), (15, 15))
	'''Shorter for `vertices`.'''

	zL: int
	'''Shorter for `Z axis Layer`. For object ordering from back to the front.'''
	iC: int
	'''Shorter for `innerColor`.'''
	bC: int = C_NONE
	'''Shorter for `borderColor`.'''