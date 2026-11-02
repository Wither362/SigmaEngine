from sge.scene import Scene
from sge.object import RectObj, CircObj
from sge.object_helper import *
import gint, math
import random as r


# Why is it called "FirstScene"? Because IT NEEDS TO BE LIKE THAT.
class Example2(Scene):
	# Called on scene load.
	def Load(self, args = None):
		'''
			In case you want to do something before SigmaEngine calls Update().
			Idk what could you do, but however you like.
		'''
		self.rectangles: list[object] = []
		self.rectanglesD: list[list[int]] = []

		for _ in range(200):
			rect = RectObj() # Create a rectangle
			# The short way to setting all the variables is this one:
			rect = Rectangle(rect, 50 * r.uniform(0.3, 2), 50 * r.uniform(0.3, 2), 40 * r.uniform(0.3, 2), 40 * r.uniform(0.3, 2), gint.C_RGB(r.randint(10, 31), r.randint(10, 31), r.randint(10, 31)), zL = 1) # you may delete the zL parameter if you don't care about layers and just want it to work.
			# if not, you would have to do this:
			# self.big_rectangle.x, self.big_rectangle.y, self.big_rectangle.width, self.big_rectangle.height = 50, 50, 70, 70 # Adjust position and size
			# self.big_rectangle.innerColor = gint.C_BLUE # Adjust color
			self.Add(rect) # Add to this scene.

			xD = r.uniform(1, -1) # short for "X direction"
			yD = r.uniform(1, -1) # short for "Y direction"

			self.rectangles.append(rect) # (the whole for i loop is completely optional, btw)
			self.rectanglesD.append([xD, yD])

		self.circle = CircObj()
		self.circle = Circle(self.circle, gint.DWIDTH - 20, 170, 35, gint.C_RGB(12, 3, 11), gint.C_RGB(7, 2, 6))
		self.circle.zL = 0
		self.Add(self.circle)

		self.circle2 = CircObj()
		self.circle2 = Circle(self.circle2, gint.DWIDTH - 20, 170, 17.5, gint.C_RGB(14, 5, 13), gint.C_RGB(9, 4, 8), zL = 3)
		self.Add(self.circle2)

		self.t = 0

		self.cXD = -1 # short for "circle X direction"
		self.cYD = -1 # short for "circle Y direction"
		
		return super().Load()

	def Update(self, dt: float):
		gint.dclear(gint.C_BLACK)

		self.t += dt

		# Take in count: ONE single object makes it so dt is around 0.016 and 0.043 seconds.
		for i in range(len(self.rectangles)):
			self.rectangles[i].x += dt * 12 * self.rectanglesD[i][0]
			self.rectangles[i].y += dt * 12 * self.rectanglesD[i][1]

			if ((self.rectangles[i].x - self.rectangles[i].hW < 0 and self.rectanglesD[i][0] < 0) or (self.rectangles[i].x + self.rectangles[i].hW > gint.DWIDTH and self.rectanglesD[i][0] < 1)):
				self.rectanglesD[i][0] = -self.rectanglesD[i][0]
	
			if ((self.rectangles[i].y - self.rectangles[i].hH < 0 and self.rectanglesD[i][1] < 0) or (self.rectangles[i].y + self.rectangles[i].hH > gint.DHEIGHT and self.rectanglesD[i][1] > 0)):
				self.rectanglesD[i][1] = -self.rectanglesD[i][1]

		self.circle.x += dt * self.cXD * 12
		self.circle.y += dt * self.cYD * 12
		self.circle.r = abs(math.cos(self.t / 2)) * 35

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
			del(self.rectangles, self.rectanglesD)
			return super().Update(sMN= 'example', sN='FirstScene', dt = dt)
		return super().Update(dt = dt)
