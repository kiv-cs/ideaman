#! /usr/bin/python
# -*- coding: utf-8 -*-
from gaming_object import *
from utilities.utils import next_point
from utilities.utils import sum_tuples, mul_tuple, fix_for_borders
from utilities.utils import position_to_direction as p2d
from utilities.utils import is_points_on_line, cell_line
from configs.config import *
from math import sin, cos, sqrt



class Citizen(Gaming_Object):
	def __init__(self, description):
		print '%s here' % self.__name__()
		Gaming_Object.__init__(self, description)

		self.is_new_goal = True if self.goal else False
		if not self.patrol_points:
			self.patrol_points = [(0,0), (X_CELL_NUM-1, Y_CELL_NUM - 1)]
		self.iter_patrol_path = iter(self.patrol_points)

		self.hear_hero = False


	def __name__(self):
		return 'Citizen'

		

	def load(self, description):
		self.position = description['position']
		self.direction = description['direction']


		self.img_path = description['construction']['image']
		self.speed = description['construction']['speed']
		self.animation_count = description['construction']['animation_count'] # number of animated situations
		self.frame_count = description['construction']['frame_count'] # change __create_animation for another values
		self.color = description['construction']['color']

		self.goal = description['construction']['goal']
		self.patrol_points = description['patrol_points']
		self.style = description['construction']['style']
		self.mode = description['construction']['mode']

		self.home = description['home']

	def update_child(self, matrix):

		if self.mode is 'patrol':
			self.__update_patrol_mode()
		if self.mode is 'hearing':
			self.__update_hearing_mode()
		if self.mode is 'running':
			self.__update_running_mode()

		if self.hear_hero:
			if self.style is 'simple' and self.mode is not 'running':
				self.__set_hearing_mode()

	def __set_running_mode(self):
		self.mode = 'running'
		self.goal = self.home
		self.speed += 6

	def __update_running_mode(self):
		if self.goal == self.position:
			self.is_active = False

	def __set_protecting_mode(self):
		self.mode = 'protecting'
		
	def __set_hearing_mode(self):
		self.mode = 'hearing'
		self.goal = None
		self.trajectory = []
		self.direction = STOP

	def __update_hearing_mode(self):
		if self.style is 'simple':
			self.__set_running_mode()

	def __set_patrol_mode(self):
		self.mode = 'patrol'
		print self.group

	def __update_patrol_mode(self):
		if not self.goal:
			try:
				self.goal = self.iter_patrol_path.next()
				self.is_new_goal = True
			except StopIteration:
				self.iter_patrol_path = iter(self.patrol_points)

