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
			Called every frame before drawing the objects.
		'''
		self.Draw()
		return newScene

	def AfterUpdate(self):
		'''
			Called after drawing the objects (Update()).
		'''

	def Add(self, object):
		'''
			Adds `obj` to the list of objects to draw to the scene.
		'''
		self.objects.append(object)







