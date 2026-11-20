from sge.scene import Scene, R
from sge.object import RObj, CObj
from sge.object_helper import Rect, Circ
import gint
import random as r


# Why is it called "FirstScene"? Because IT NEEDS TO BE LIKE THAT.
class FirstScene(Scene):
	# Called on scene load.
	def Load(self, args = None):
		'''
			In case you want to do something before SigmaEngine calls Update().
			Idk what could you do, but however you like.
		'''

		for _ in range(50):
			rect = RObj() # Create a rectangle
			# The short way to setting all the variables is this one:
			rect = Rect(rect, 50 * r.uniform(0.3, 2), 50 * r.uniform(0.3, 2), 40 * r.uniform(0.3, 2), 40 * r.uniform(0.3, 2), gint.C_RGB(r.randint(10, 31), r.randint(10, 31), r.randint(10, 31)), zL = 1) # you may delete the zL parameter if you don't care about layers and just want it to work.
			# if not, you would have to do this:
			# self.big_rectangle.x, self.big_rectangle.y, self.big_rectangle.width, self.big_rectangle.height = 50, 50, 70, 70 # Adjust position and size
			# self.big_rectangle.innerColor = gint.C_BLUE # to adjust color
			rect.dx = r.uniform(1, -1) # short for "X direction"
			rect.dy = r.uniform(1, -1) # short for "Y direction"
			self.Add(rect) # Add to this scene.

		self.circle = CObj()
		self.circle = Circ(self.circle, gint.DWIDTH - 20, 170, 35, gint.C_RGB(12, 3, 11), gint.C_RGB(7, 2, 6))
		self.circle.zL = 0
		self.Add(self.circle)

		self.circle2 = CObj()
		self.circle2 = Circ(self.circle2, gint.DWIDTH - 20, 170, 17.5, gint.C_RGB(14, 5, 13), gint.C_RGB(9, 4, 8), zL = 3)
		self.Add(self.circle2)

		self.t = 0

		self.cXD = -1 # short for "circle X direction"
		self.cYD = -1 # short for "circle Y direction"
		
		return super().Load()

	def Update(self, dt: float):
		gint.dclear(gint.C_BLACK)

		self.t += dt

		# Take in count: ONE single object makes it so dt is around 0.016 and 0.043 seconds.
		for o in self.objs:
			if o.s != R: continue # Skip non-rectangles
			
			o.x += dt * 12 * o.dx
			o.y += dt * 12 * o.dy
			
			# Bounce logic
			if o.x < o.hW or o.x > gint.DWIDTH - o.hW:
				o.dx *= -1
			if o.y < o.hH or o.y > gint.DHEIGHT - o.hH:
				o.dy *= -1

		self.circle.x += dt * self.cXD * 12
		self.circle.y += dt * self.cYD * 12
		self.circle.r = (self.t % 4) * 8.75 # cos() implementation

		if (self.circle.r <= 17.5):
			if (self.circle.zL != 4): # only execute SortObjects ONCE, NOT EVERY FRAME
				self.circle.zL = 4
				self.SortObjects()
		elif (self.circle.zL != 2):
			self.circle.zL = 2
			self.SortObjects()

		self.circle2.x = self.circle.x
		self.circle2.y = self.circle.y

		if (self.circle.x - max(self.circle.r, self.circle2.r) < 0 and self.cXD == -1):
			self.cXD = 1
		elif (self.circle.x + max(self.circle.r, self.circle2.r) > gint.DWIDTH and self.cXD == 1):
			self.cXD = -1

		if (self.circle.y - max(self.circle.r, self.circle2.r) < 0 and self.cYD == -1):
			self.cYD = 1
		elif (self.circle.y + max(self.circle.r, self.circle2.r) > gint.DHEIGHT and self.cYD == 1):
			self.cYD = -1

		if (self.t > 10):
			self.objs.clear()
			return super().Update(sMN= 'example2', sN='Example2', dt = dt)
		return super().Update(dt = dt) # we could return sMN = 'scene2_file' and sN = 'Scene2' if we wanted to change the scene to Scene2 which is supposely inside scene2.py.
