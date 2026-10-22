'''Sigma Engine's main component of everything.'''

from src.object import Object
from src.camera import Camera
from gint import dupdate

class Scene:
	'''Sigma Engine's main component of everything.'''

	objects: list[Object]
	'''objects which will be represented on screen'''
	camera: Camera

	def __init__(self):
		'''Creates a new Scene Object. This is NEEDED in the first scene.
		After that... Not really.'''
		self.objects = []

	def load(self):
		'''Called on Scene Load.'''

	def draw(self):
		'''Draws the objects on screen.'''

		if (len(self.objects) >= 0):
			for obj in self.objects:
				obj.draw()
		dupdate()

	def update(self):
		'''Updates this Scene and draws the objects. Called every frame.'''
		self.draw()

	def afterUpdate(self):
		'''Called after update().'''

	def add(self, object):
		'''Adds `obj` to the list of objects to draw to the scene.'''
		self.objects.append(object)
