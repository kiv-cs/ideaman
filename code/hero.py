#! /usr/bin/python
# -*- coding: utf-8 -*-
from gaming_object import *
from pygame import KEYDOWN, MOUSEBUTTONDOWN
from config import *
from pygame import mouse
from utils import screen_to_coord as s2c
from utils import mul_tuple, next_point

class Hero(Gaming_Object):
	def __init__(self, description):
		print '%s here' % self.__name__()
		Gaming_Object.__init__(self, description)

		self.is_new_goal = True if self.goal else False
		self.control_mode = 'mouse'

		self.rect.width = X_CELL / 4
		self.rect.height = Y_CELL / 4
		#self.rect.move(self.position)


	def __name__(self):
		return 'Hero'

	def event(self, event):
		# self.direction = STOP
		# create STOP event to make it work
		if event.type == KEYDOWN:
			self.control_mode = 'arrows'
			self.__update_direction(event.key)
			if event.key == 280: # PgUp
				self.speed += 1
			elif event.key == 281: # PgDown
				self.speed -=1
		if event.type == MOUSEBUTTONDOWN:
			self.control_mode = 'mouse'
			self.goal = s2c(mouse.get_pos())
			self.screen_goal = mouse.get_pos()
			self.is_new_goal = True
			print 'mouse %s %s' % (self.position, self.goal)

	def update_child(self,matrix):
		next_step = mul_tuple(self.direction, self.speed)
		next_screen_position = next_point(self.screen_position, next_step)
		x, y = s2c(next_screen_position)
		if x >= X_CELL_NUM or x < 0 or y >= Y_CELL_NUM or y < 0 or not matrix[y][x]:
			# self.direction = STOP
			self.direction = TRIGONOMETRY_SUCKS[self.direction]['contr']
		


	def __update_direction(self, key=None):
		try:
			self.direction = KEY_DIRECTION_MAP[key]
		except KeyError:
			self.direction = STOP


	def move_by_arrows(self):
		next_step = mul_tuple(self.direction, self.speed)
		self.make_step(next_step)

	def load(self, description):
		self.position = description['position']
		self.direction = description['direction']

		self.img_path = description['construction']['image']
		self.speed = description['construction']['speed']
		self.animation_count = description['construction']['animation_count'] # number of animated situations
		self.frame_count = description['construction']['frame_count'] # change __create_animation for another values
		self.color = description['construction']['color']

		self.goal = description['construction']['goal']

		self.patrol_points = None

	def talking(self):
		print 'BLABLA'


