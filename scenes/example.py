from sge.scene import Scene
from sge.object import Object
from sge.object_helper import *
import gint
import math
import random as r


# Why is it called "FirstScene"? Because IT NEEDS TO BE LIKE THAT.
class FirstScene(Scene):
	# Called on scene load.
	def Load(self):
		'''
			In case you want to do something before SigmaEngine calls Update().
			Idk what could you do, but however you like.
		'''
		self.rectangles: list[obj.Object] = []
		self.rectanglesD: list[list[int]] = []

		for i in range(r.randint(3, 8)):
			rect = Object(1) # Create a rectangle
			# The short way to setting all the variables is this one:
			rect = Rectangle(rect, 50 * r.uniform(0.3, 2), 50 * r.uniform(0.3, 2), 40 * r.uniform(0.3, 2), 40 * r.uniform(0.3, 2), gint.C_RGB(r.randint(10, 31), r.randint(10, 31), r.randint(10, 31)))
			# if not, you would have to do this:
			# self.big_rectangle.x, self.big_rectangle.y, self.big_rectangle.width, self.big_rectangle.height = 50, 50, 70, 70 # Adjust position and size
			# self.big_rectangle.innerColor = gint.C_BLUE # Adjust color
			self.Add(rect) # Add to this scene.

			xD = r.uniform(1, -1) # short for "X direction"
			yD = r.uniform(1, -1) # short for "Y direction"

			self.rectangles.append(rect) # (the whole for i loop is completely optional, btw)
			self.rectanglesD.append([xD, yD])

		self.circle = Object(0)
		self.circle = Circle(self.circle, gint.DWIDTH - 20, 170, 35, gint.C_RGB(12, 3, 11), gint.C_RGB(7, 2, 6))
		self.circle.zL = 0
		self.Add(self.circle)

		self.circle2 = Object(0)
		self.circle2 = Circle(self.circle2, gint.DWIDTH - 20, 170, 17.5, gint.C_RGB(14, 5, 13), gint.C_RGB(9, 4, 8))
		self.Add(self.circle2)

		self.t = 0

		self.cXD = -1 # short for "circle X direction"
		self.cYD = -1 # short for "circle Y direction"
		
		return super().Load()

	def Update(self, dt: float):
		gint.dclear(gint.C_BLACK)

		self.t += dt * 2

		# Take in count: ONE single object makes it so dt is around 0.016 and 0.043 seconds.
		for i in range(len(self.rectangles)):
			self.rectangles[i].x += dt * 20000 * self.rectanglesD[i][0]
			self.rectangles[i].y += dt * 15000 * self.rectanglesD[i][1]

			if ((self.rectangles[i].x - self.rectangles[i].hW < 0 and self.rectanglesD[i][0] < 0) or (self.rectangles[i].x + self.rectangles[i].hW > gint.DWIDTH and self.rectanglesD[i][0] < 1)):
				self.rectanglesD[i][0] = -self.rectanglesD[i][0]
	
			if ((self.rectangles[i].y - self.rectangles[i].hH < 0 and self.rectanglesD[i][1] < 0) or (self.rectangles[i].y + self.rectangles[i].hH > gint.DHEIGHT and self.rectanglesD[i][1] > 0)):
				self.rectanglesD[i][1] = -self.rectanglesD[i][1]

		self.circle.x += dt * 20000 * self.cXD
		self.circle.y += dt * 17000 * self.cYD
		self.circle.r = 35 * abs(math.cos(self.t * 150))

		if (self.circle.r <= 17.5):
			if (self.circle.zL != 1):
				self.circle.zL = 1
				self.SortObjects()
		elif (self.circle.zL != -1):
			self.circle.zL = -1
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

		return super().Update(dt = dt) # we could return 'newScene = 'nasdaisdais'' if we wanted to change scenes.

	def AfterUpdate(self):
		return super().AfterUpdate()
