from sge.scene import Scene
from sge.object import CObj
from sge.object_helper import Circ
import gint
import random as r
from micropython import const # type: ignore

PLAYER_INITIAL_X = const(360)
PLAYER_R = const(5)
PLAYER_SPEED_X = const(68)
PLAYER_SPEED_Y = const(40)
PLAYER_DRAG = const(25)
PLAYER_DRAG_INV = const(67)
PLAYER_INV_TIMER = const(3000) # in miliseconds
PLAYER_ICOL = const(0b00000_000000_11111) # blue
PLAYER_BCOL = const(0x528a)
PLAYER_LIFES = const(2)

WIDTH = const(384)
HEIGHT = const(216)
LVL_LATE_X = const(-1536) # -WIDTH * 4


class FirstScene(Scene):
	'''RushCircles'''
	def Load(self, args = None):
		for i in range(100):
			circ = Circ(CObj(), int(r.uniform(LVL_LATE_X, 0)), int(r.uniform(0, gint.DHEIGHT)), int(r.uniform(4, 7)), gint.C_WHITE, gint.C_LIGHT)
			circ.vel = r.uniform(1, 1.5)
			self.Add(circ)

		circ = Circ(CObj(), PLAYER_INITIAL_X, gint.DHEIGHT // 2, PLAYER_R, PLAYER_ICOL, PLAYER_BCOL)
		self.player = circ
		self.Add(self.player)
		del(circ)

		self.dy = int(0)
		self.dx = int(0)
		self.invincible = False
		self.invTimer = int(0000)
		self.lifes = PLAYER_LIFES
		self.WIN = False

		return super().Load()

	def hit(self):
		self.invTimer = PLAYER_INV_TIMER
		self.player.iC = gint.C_DARK
		self.player.bC = gint.C_LIGHT
		self.lifes -= 1
		if (self.lifes <= 0):
			self.objs.clear()
			gint.dclear(gint.C_RED)
			gint.dtext(gint.DWIDTH // 2, gint.DHEIGHT // 2, gint.C_WHITE, "DEATH.", gint.DTEXT_CENTER, gint.DTEXT_MIDDLE)

	def Update(self, dt):
		if self.lifes <= 0:
			if self.draw:
				self.draw = False
			return super().Update(dt = dt)
		elif (self.WIN):
			if self.draw:
				self.draw = False
			return super().Update(dt = dt)

		gint.dclear(gint.C_BLACK)
		if (self.invTimer > 0):
			self.invTimer -= int(dt * 1000)
			if (self.invTimer < 0):
				self.player.iC = PLAYER_ICOL
				self.player.bC = PLAYER_BCOL

		self.player.y += self.dy * dt
		self.player.x += self.dx * dt
		if self.invTimer <= 0: self.player.x += dt * PLAYER_DRAG
		else: self.player.x += dt * PLAYER_DRAG_INV
		self.dx = self.dy = 0
		if (self.player.y < 0): self.player.y = gint.DHEIGHT
		if (self.player.y > gint.DHEIGHT): self.player.y = 0
		if (self.player.x > gint.DWIDTH - PLAYER_R): self.player.x = gint.DWIDTH - PLAYER_R

		for o in self.objs:
			if (o != self.player):
				o.x += 70 * dt * o.vel
				if (self.invTimer <= 0):
					if (o.x - self.player.x)**2 + (o.y - self.player.y)**2 <= (o.r + PLAYER_R)**2:
						self.hit()
				if (o.x - o.r > gint.DWIDTH):
					o.x = LVL_LATE_X

		if (self.player.x <= 0):
			self.objs.clear()
			gint.dclear(gint.C_GREEN)
			gint.dtext(gint.DWIDTH // 2, gint.DHEIGHT // 2, gint.C_DARK, "YOU WON!", gint.DTEXT_CENTER, gint.DTEXT_MIDDLE)
			self.WIN = True

		return super().Update(dt = dt)

	def AfterUpdate(self, dt: float):
		gint.pollevent()
		if (self.lifes <= 0 or self.WIN and not self.draw):
			gint.getkey()

			return super().AfterUpdate(dt = dt)

		if gint.keydown(gint.KEY_RIGHT):
			self.dx = PLAYER_SPEED_X
		elif gint.keydown(gint.KEY_LEFT):
			self.dx = -PLAYER_SPEED_X
		if gint.keydown(gint.KEY_UP):
			self.dy = -PLAYER_SPEED_Y
		elif gint.keydown(gint.KEY_DOWN):
			self.dy = PLAYER_SPEED_Y

		gint.clearevents()
		gint.cleareventflips()

		# gint.clearevents()
		return super().AfterUpdate(dt = dt)