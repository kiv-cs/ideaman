class Animation:
	def __init__(self, sprites=None, time=100):
		self.sprites = sprites
		self.time = time
		self.work_time = 0
		self.skip_frame = 0
		self.frame = 0
		if type(time) == list:
			self.__update = self.__update_any_time
		else:
			self.__update = self.__update_const_time

	def update(self, dt):
		self.work_time += dt
		self.__update(dt)

	def __update_const_time(self, dt):
		self.skip_frame = self.work_time / self.time
		if self.skip_frame > 0:
			self.work_time = self.work_time % self.time
			self.frame += self.skip_frame
			if self.frame >= len(self.sprites):
				self.frame = 0

	def __update_any_time(self, dt):
		while self.work_time - self.time[self.frame] > 0:
			self.work_time -= self.time[self.frame]
			self.frame += 1
			if self.frame >= len(self.sprites):
				self.frame = 0

	def get_sprite(self):
		return self.sprites[self.frame]