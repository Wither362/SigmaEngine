'''
	Module for separating "object" and the "object generators".
'''
import sge.object as obj

def Rectangle(o: obj.Object, x: float, y: float, w: float, h: float, c, zL: int = 0):
	'''
		Sets the shape of the object `o` as a rectangle and sets its attributes.
		It's a great way to not forget want attributes you have to specify in order for SGE to work properly.
	'''
	o.s, o.x, o.y, o.hW, o.hH, o.iC = 1, x, y, w / 2, h / 2, c
	if (zL != 0):
		o.zL = zL
	return o

def Circle(o: obj.Object, x: float, y: float, r: float, c: int, bC: int, zL: int = 0):
	'''
		Sets the shape of the object `o` as a circle and sets its attributes.
		It's a great way to not forget want attributes you have to specify in order for SGE to work properly.
	'''
	o.s, o.x, o.y, o.r, o.iC, o.bC = 0, x, y, r, c, bC
	if (zL != 0):
		o.zL = zL
	return o