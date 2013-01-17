#! /usr/bin/python
# -*- coding: utf-8 -*-
try:
	import android
except ImportError:
	android = None
from pygame import init
from pygame import display
from pygame import QUIT, KEYDOWN, K_ESCAPE
from pygame import font


from config import *
from location import *

'''
main class
'''
class General():
	location_index = 0				# index for location list
	def __init__(self):
		print '%s here' % self.__name__()
		if android:
			android.init()
			android.map_key(android.KEYCODE_MENU, K_ESCAPE)

		init()
		display.set_mode((X_MAX, Y_MAX))

		font.init()

		self.location = Location(self.location_index)

	def __name__(self):
		return 'General'

	def next_location(self):
		self.location_index += 1
		self.location = Location(self.location_index)

	def event(self, event):
		if event.type == QUIT:
			exit(0)
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			self.__init__()
		if event.type == KEYDOWN: 
			if event.key == 48:
				self.location = Location(0)
			elif event.key == 49:
				self.location = Location(1)
			elif event.key == 50:
				self.location = Location(2)

