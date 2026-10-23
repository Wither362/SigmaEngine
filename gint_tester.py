'''Just a test file that checks if the copied behaviour of gint works.'''

import sge.object as s
from gint import *


o = s.Object(1)
o.x, o.y = 100, 100
o.width, o.height = 50, 50
o.innerColor = C_BLUE

o.draw()

dupdate()