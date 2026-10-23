from sge.scene import Scene
from sge.object import Object
import gint

# Why is it called "FirstScene"? Because IT NEEDS TO BE LIKE THAT.
class FirstScene(Scene):
	# Called on scene load.
	def Load(self):
		'''
			In case you want to do something before SigmaEngine calls Update().
			Idk what could you do, but however you like.
		'''

		self.big_rectangle = Object(1) # Create a rectangle
		self.big_rectangle.x, self.big_rectangle.y, self.big_rectangle.width, self.big_rectangle.height = 50, 50, 70, 70 # Adjust position and size
		self.big_rectangle.innerColor = gint.C_BLUE # Adjust color
		self.Add(self.big_rectangle) # Add to this scene.
		
		return super().Load()

	def Update(self):
			gint.dclear(gint.C_NONE)		
			self.big_rectangle.x += 0.1
	
			return super().Update()

