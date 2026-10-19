'''Sigma Engine's main component of everything.'''
import object
import camera

class Scene:
	'''Sigma Engine's main component of everything.'''

	objects: list[object.Object] = []
	'''objects which will be represented on screen'''
	camera: camera.Camera

	def draw():
		'''Draws the objects on screen.'''