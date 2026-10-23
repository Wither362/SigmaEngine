from src.scene import Scene
from src.object import Object
import gint

# Why is it called "FirstScene"? Because IT NEEDS TO BE LIKE THAT.
class FirstScene(Scene):
	def Update(self):
		return super().Update()

	# Called on scene load.
	def Load(self):
		'''
			In case you want to do something before SigmaEngine calls Update().
			Idk what could you do, but however you like.
		'''
		big_rectangle = Object(1) # Create a rectangle
		big_rectangle.x, big_rectangle.y, big_rectangle.width, big_rectangle.height = 50, 50, 70, 70 # Adjust position and size
		big_rectangle.innerColor = gint.C_BLUE # Adjust color
		self.Add(big_rectangle) # Add to this scene.
		
		return super().Load()

