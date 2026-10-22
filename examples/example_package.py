from src.scene import Scene
from src.object import Object
import gint

# Why is it called "FirstScene"? Because IT NEEDS TO BE LIKE THAT.
class FirstScene(Scene):
	def update(self):
		return super().update()

	# Called on scene load.
	def load(self):
		'''In case you want to do something before SigmaEngine calls update().
		Idk what could you do, but however you like.'''
		big_rectangle = Object(1)
		big_rectangle.x, big_rectangle.y, big_rectangle.width, big_rectangle.height = 50, 50, 70, 70
		big_rectangle.innerColor = gint.C_BLUE
		self.add(big_rectangle)
		
		return super().load()

