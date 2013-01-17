#! /usr/bin/python
# -*- coding: utf-8 -*-
from gaming_object import *

#
# THIS
# IS
# TEMPORARY
#

class Wall(Gaming_Object):

	def __init__(self, description):
		print '%s here' % self.__name__()
		Gaming_Object.__init__(self, description)

	def __name__(self):
		return 'Wall'

	def default_action(self):
		self.direction = STOP


	def load(self, description):
		self.position = description['position']
		self.img_path = description['construction']['image']
		self.animation_count = description['construction']['animation_count']
		self.frame_count = description['construction']['frame_count']

		self.goal = None
		self.patrol_points = None

	def update_trajectory(self, matrix):
		pass