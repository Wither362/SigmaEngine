'''SigmaEngine's form of displaying the scenes to the screen.'''

from pointer import Pointer

class Camera(Pointer):
	width: float
	height: float
	rotationZ: float