'''
	Sigma Engine's main component of everything.
'''

from sge.math import truncate
from sge.object import Object, on_screen, R, C, C
from sge.camera import Camera
from gint import dupdate, dtext, drect_border, dcircle, C_WHITE

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

	def Load(self, args = None):
		'''
			Called when this scene loads.\n

			**Params**:
			- `args`: optional arguments in form of a `dict` that get defined when changing scene, for transferring data and such.
		'''

	def Draw(self, dt: float):
		'''
			Draws the objects on screen.
		'''

		if (len(self.objects) >= 0):
			for o in self.objects:
				if (not on_screen(o)):
					continue

				if (o.s == C):
					dcircle(int(o.x), int(o.y), int(o.r), o.iC, o.bC)
				elif (o.s == R):
					drect_border(int(o.x - o.hW), int(o.y - o.hH), int(o.x + o.hW), int(o.y + o.hH), o.iC, o.bS, o.bC)


		# Add a little text at the top left corcer of the screen
		# which tells at how many fps the game is running
		if (dt > 0):
			dtext(0, 0, C_WHITE, "FPS " + str(truncate(1 / dt, 1)))
		dupdate()

	def Update(self, sMN: str = None, sN: str = None, dt: float = -1):
		'''
			Called every frame **before** drawing the objects to the screen.
			This DOES NOT CALL 'gint.dclear'.

			**Overwrite Params**:
			- `dt`: the delta time / how many seconds have passed since the last call to Update().

			**`super()` Params** in case you want to change scenes:
			- `sMN`: shorter for `Scene Module Name`, which is the `filename` of the file where the new scene is in.
			- `sN`: shorter for `Scene Name`, which is the name of the `scene class` you want to change to.

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
				  # the **class** `SuperAwesomeScene` is inside the file `super_awesome.py`
				  return super().Update(sMN = 'super_awesome', sN = 'SuperAwesomeScene')
				else: # this 'else' could be deleted ngl
				  return super().Update() # don't tell NOTHING.
			```
		'''
		self.Draw(dt)
		return sMN, sN

	def AfterUpdate(self, dt: float):
		'''
			Called after drawing the objects (Update()).
		'''

	def Destroy(self, args: dict = None):
		'''
			Called when scene is being destroyed.
			Used for deleting large lists and performance eaters.
			And used to return parameters for the next scene.
		'''
		return args

	def SortObjects(self):
		'''
			Sorts its objects by their `zL` attribute.
			Supposely called when a new object is added or whenever the code feels like it needs to.
			You can call it whenever you want tho, **but** it's a quite laggy function if the scene has a lot of objects,
			as the code needs to go through all of the scene.objects and then sort them according to their `zL` attribute
			(which will be `0` in case that attribute doesn't exist.)
		'''
		self.objects = sorted(self.objects, key = lambda o: o.zL if hasattr(o, 'zL') else 0)

	def Add(self, object):
		'''
			Adds `obj` to the list of objects to draw to the scene.
		'''
		self.objects.append(object)
		self.SortObjects()

