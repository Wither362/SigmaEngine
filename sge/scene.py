'''
	Sigma Engine's main component of everything.
'''

from sge.math import truncate
from sge.object import Object
from sge.camera import Camera
from gint import dclear, dupdate, dtext, C_WHITE, C_BLACK

class Scene:
	'''
		Sigma Engine's main component of everything.
		
		There may only be one single Scene at a time.
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

	def Draw(self, dt: float):
		'''
			Draws the objects on screen.
		'''

		if (len(self.objects) >= 0):
			for obj in self.objects:
				obj.Draw()

		# Add a little text at the top left corcer of the screen
		# which tells at how many fps the game is running
		if (dt > 0):
			dtext(0, 0, C_WHITE, "FPS " + str(truncate(1 / dt, 1)))
		dupdate()

	def Update(self, newScene: str = None, dt: float = -1):
		'''
			Called every frame **before** drawing the objects to the screen.
			This DOES NOT CALL 'gint.dclear'.

			**Overwrite Params**:
			- `dt`: the delta time / how many seconds have passed since the last call to Update().
			
			**`super()` Params**:
			- `newScene`: if not `None`, SGE will automatically change the scene to this str.
			
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
			      # Return a super cool and awesome str to make SigmaEngine change scenes.
			      return super().Update('SuperAwesomeScene2')
			    else: # this 'else' could be deleted ngl
			      return super().Update() # don't tell NOTHING.
			```
		'''
		self.Draw(dt)
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
		self.objects = sorted(self.objects, key = lambda o: o.zL if hasattr(o, 'zL') else 0)

	def Add(self, object):
		'''
			Adds `obj` to the list of objects to draw to the scene.
		'''
		self.objects.append(object)
		self.SortObjects()

	







