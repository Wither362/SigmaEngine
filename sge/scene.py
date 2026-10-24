'''
	Sigma Engine's main component of everything.
'''

from sge.object import Object
from sge.camera import Camera
from gint import dupdate

class Scene:
	'''
		Sigma Engine's main component of everything.
	'''

	objects: list[Object]
	'''objects which will be represented on screen'''
	camera: Camera

	def __init__(self):
		'''
			Creates a new Scene.
		'''
		self.objects = []

	def Load(self):
		'''
			Called when this scene loads.
		'''

	def Draw(self):
		'''
			Draws the objects on screen.
		'''

		if (len(self.objects) >= 0):
			for obj in self.objects:
				obj.Draw()
		dupdate()

	def Update(self, newScene: str = None):
		'''
			Called every frame **before** drawing the objects to the screen.

			**`super()` Params**:
			- `newScene`: if not `None`, SGE will automatically change the scene to this str.

			**Overwrite Params**:
			- `dt`: the delta time / how many seconds have passed since the last call to Update().

			**Example**:
			```py
			class ExampleScene(Scene):
				# as you should now, it's important that you also add the 'self' part to the function.
				def Update(self, dt):
					global change_scene, is_user_lagging
					change_scene: bool = False
					is_user_lagging = False
					# maybe check user input
					if (user_is_inputting):
						change_scene = True
					if (dt > 0.1):
						is_user_lagging = True
					
					if (change_scene or is_user_lagging):
						return super().Update('SuperAwesomeScene2')
					else: # this 'else' could be deleted ngl
						return super().Update() # don't tell NOTHING.
			```
		'''
		self.Draw()
		return newScene

	def AfterUpdate(self):
		'''
			Called after drawing the objects (Update()).
		'''

	def SortObjects(self):
		'''
			Sorts its objects by their `zLayer`.
			Supposely called when a new object is added or whenever the code feels like it needs to.
			You can call it whenever you want tho.
		'''
		self.objects = sorted(self.objects, key = lambda o: o.zLayer if hasattr(o, 'zLayer') else 0)

	def Add(self, object):
		'''
			Adds `obj` to the list of objects to draw to the scene.
		'''
		self.objects.append(object)
		self.SortObjects()

	







