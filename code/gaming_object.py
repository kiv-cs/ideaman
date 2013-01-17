#! /usr/bin/python
# -*- coding: utf-8 -*-

from pygame import sprite
from pygame import image
from pygame import Rect
from pygame import transform
from pygame import draw
from pygame import KEYDOWN

from stuff import Animation
from random import choice
from math import sin

from config import *

from a_star import a_star
from catmull_rom import catmull_rom_trajectory

from utils import coord_to_screen as c2s
from utils import screen_to_coord as s2c
from utils import position_to_direction as p2d
from utils import delta as d
from utils import coord_to_rect as c2r
from utils import screen_to_rect as s2r
from utils import write_log, fix_for_borders

class Gaming_Object(sprite.Sprite):
	def __init__(self, description):
		print '%s here' % self.__name__()
		sprite.Sprite.__init__(self)
		self.load(description)

		self.sprite = image.load(self.img_path).convert_alpha()
		self.sprite_rect = self.sprite.get_rect() # sprite rectangle
		self.image_width = self.sprite_rect.w / self.frame_count
		self.image_height = self.sprite_rect.h / self.animation_count
		self.rect = Rect(c2r(self.position), (X_CELL, Y_CELL)) # why?
		self.screen_position = self.rect.center


		self.x, self.y = self.screen_position
		

		self.trajectory = []

		self.__create_animations()

		self.is_visible = True
		self.is_active = True

	def __name__(self):
		return 'Gaming_Object'

	def event(self, event):
		pass



	def update(self, matrix):
		if self.is_active: # it must be mode
			self.screen_position = self.rect.center
			self.position = s2c(self.screen_position)

			# write a good handler
			# print self.goal, len(matrix), len(matrix[0])
			if self.goal and not matrix[self.goal[1]][self.goal[0]]:
				self.goal = None

			#print 'pos %s, goal %s, class %s' % (self.position, self.goal, self.__name__())
				

			self.update_child(matrix)

			if self.position == self.goal:
				self.goal = None

			self.update_trajectory(matrix)



	def update_child(self, matrix):
		pass



	def update_trajectory(self, matrix):
		if ((self.trajectory == []) and self.goal 
						and matrix[fix_for_borders(self.goal)[1]][fix_for_borders(self.goal)[0]]): # refactor?
			# print 'Updating. Name: %s. Position: %s. Goal: %s. Speed: %s' % (self.__name__(), 
			#											self.position, self.goal, self.speed)
			points = a_star(matrix, self.position, self.goal)
			self.is_new_goal = False
			if points:
				trajectory = catmull_rom_trajectory(self.speed, [self.screen_position] + 
											[c2s(point) for point in points[1:3]])
				if trajectory:
					if self.position in trajectory: trajectory.remove(self.position)
					self.trajectory = trajectory[1:]


	def make_step(self, delta):
		self.rect.move_ip(delta)
		try:
			self.animation = self.animations[self.direction]
		except KeyError:
			self.animation = self.animations[STOP]
		self.animation.update(DT)

	def move(self):
		if self.__name__() is 'Hero':
			if self.control_mode is 'arrows':
				self.move_by_arrows()
				return False
		if self.trajectory == []:
			self.default_action()
		else:
			where = self.trajectory.pop(0)

			direction = p2d(self.screen_position, where)
			if direction: self.direction = direction

			self.make_step(d(self.screen_position, where))
		

	def default_action(self):
		pass
		self.direction = STOP


	def say(self):
		pass
	# sector of view
	def see(self):
		pass

	# for another animation times of different anim times (like for crankybot) 
	# rewrite this method for inherit
	def __create_animations(self):
		self.animations = []
		anim_time = ANIMATION_TIME
		for _ in range(self.animation_count):
			anim = []

			offset = self.image_width * _
			for f in range(self.frame_count):
				anim.append(self.sprite.subsurface((self.image_height * f, offset, 
													self.image_width, self.image_height)))
			

			self.animations.append(Animation(anim, anim_time))

		# need make dict beceuse directions is tuples
		self.animations = dict(zip(DIRECTIONS, self.animations))
		# now we have something like {(0,0): <Animation object 0>, (0, 1): <Animation object 1> etc.}

		self.animation = self.animations[STOP]

	def draw(self, window):
		if self.is_visible:
			scaled_object = transform.scale(self.animation.get_sprite(), 
											(int(self.image_width / K), int(self.image_height / K)))
			

			# draw something only in its own rect!
			window.blit(scaled_object, self.rect)




	

