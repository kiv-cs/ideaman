#! /usr/bin/python
# -*- coding: utf-8 -*-
from gaming_object import *
from utils import next_point
from utils import sum_tuples, mul_tuple, fix_for_borders
from utils import position_to_direction as p2d
from utils import is_points_on_line, cell_line
from config import *
from math import sin, cos, sqrt



class Enemy(Gaming_Object):
	def __init__(self, description):
		print '%s here' % self.__name__()
		Gaming_Object.__init__(self, description)

		self.is_new_goal = True if self.goal else False

		if not self.patrol_points:
			self.patrol_points = [(0,0), (X_CELL_NUM-1, Y_CELL_NUM - 1)]

		self.iter_patrol_path = iter(self.patrol_points)
		


	def __name__(self):
		return 'Enemy'

	def load(self, description):
		self.position = description['position']
		self.direction = description['direction']


		self.img_path = description['construction']['image']
		self.speed = description['construction']['speed']
		self.animation_count = description['construction']['animation_count'] # number of animated situations
		self.frame_count = description['construction']['frame_count'] # change __create_animation for another values
		self.color = description['construction']['color']

		self.goal = description['construction']['goal']
		self.target = description['construction']['target']
		self.patrol_points = description['patrol_points']
		self.style = description['construction']['style']
		self.mode = description['construction']['mode']

		self.view_area_radius = 4
		self.view_area_angle = pi / 4 # half of real angle!
		self.view_area_width = 5
		self.view_area_height = 5



	def update_child(self, matrix):
		self.__update_view_area(matrix)
		self.__update_view_cells(matrix)
		self.is_see_target = False
		if self.target and self.see(self.target.position, matrix):
			self.is_see_target = True
			


		if self.mode is 'patrol' and self.is_see_target:
			self.__set_hunting_mode()
		elif self.mode is 'search' and self.is_see_target:
			self.__set_patrol_mode() # to disable superspeed etc
			self.__set_hunting_mode()
		elif self.mode is 'hunting' and not self.is_see_target:
			self.__set_search_mode()
			
		if self.mode is 'hunting':
			self.__update_hunting_mode()
		elif self.mode is 'patrol':
			self.__update_patrol_mode()
		elif self.mode is 'search':
			self.__update_search_mode()

		# updating trajectory if and ONLY if new goal

	def __set_search_mode(self):
		self.mode = 'search'
		self.iter_search_points = iter([next_point(self.position, direction) 
									for direction in [self.target.direction] + 
														TRIGONOMETRY_SUCKS[self.target.direction]['ort']
														] 
														)

	def __update_search_mode(self):
		if not self.goal:
			try:
				self.goal = fix_for_borders(self.iter_search_points.next())
				self.is_new_goal = True
			except StopIteration:
				self.__set_patrol_mode()

	def __set_hunting_mode(self):
		self.mode = 'hunting'
		self.view_area_angle -= 0
		self.view_area_radius += 3

		# self.view_area_height += 5
		# self.view_area_width += 5
		self.speed += 1


	def __update_hunting_mode(self):
		# goal is hero position
		if self.style is 'blinky':
			self.goal = self.target.position
		# goal is hero position + 3 cells more
		if self.style is 'pinky':
			self.goal = fix_for_borders(next_point(self.target.position, 
													mul_tuple(self.target.direction, 3)))
			self.is_new_goal = True
		if self.style is 'inky':
			pass
		if self.style is 'clyde':
			pass

	def __set_patrol_mode(self):
		self.mode = 'patrol'



		self.view_area_angle += 0
		self.view_area_radius -= 3

		# self.view_area_height -= 5
		# self.view_area_width -= 5
		self.speed -= 1

	# write handler in case of there is no way to the goal (but it not a wall) 
	def __update_patrol_mode(self):
		if not self.goal:
			try:
				self.goal = self.iter_patrol_path.next()
				self.is_new_goal = True
			except StopIteration:
				self.iter_patrol_path = iter(self.patrol_points)


	def __update_view_area_cells(self, matrix):
		width = self.view_area_width
		height = self.view_area_height
		direction = self.direction if not self.direction == STOP else SOUTH

		start_points = [(next_point(self.position, mul_tuple(ort, i)), height-i) 
						for i in range(0, width / 2 + 1) 
						for ort in TRIGONOMETRY_SUCKS[direction]['ort']]

		all_points = []
		
		for start in start_points:
			for i in range(start[1]):		
				point = next_point(start[0], mul_tuple(direction, i))
				all_points.append(point)

		fixed_all_points = [fix_for_borders(p) for p in all_points]

		wall_in_view = [ point for point in fixed_all_points if not matrix[point[1]][point[0]] ]	
			
		result = [p for p in all_points for w in wall_in_view if not is_points_on_line(self.position, w, p)]
			
		self.view_area = all_points

	def __update_view_area_FAK(self, matrix):
		width = self.view_area_width
		height = self.view_area_height
		direction = self.direction if not self.direction == STOP else SOUTH

		levels = []
		level_count = height-1
		orts = TRIGONOMETRY_SUCKS[direction]['ort']
		
		# for w in range(width):
		#	
		for h in range(height):
			center = next_point(self.position, mul_tuple(direction, h))
			level = [center]
			for w in range((width - level_count) / 2 ):
				left_right = [next_point(center, mul_tuple(ort, w + 1)) for ort in orts]
				level += left_right
			level_count -= 1
			levels.append(level)

			


		if levels:
			self.view_area = reduce(lambda a, b: a + b, levels)

	def __update_view_area(self, matrix):

		alpha = self.view_area_angle
		radius = self.view_area_radius * X_CELL
		x0, y0 = self.screen_position
		direction = self.direction if not self.direction == STOP else SOUTH

		omega = TRIGONOMETRY_SUCKS[direction]['rad'] + alpha

		cos_omega = cos(omega)
		sin_omega = sin(omega)

		if direction in [NORTH, SOUTH]:
			self.view_area = [(x0 + radius * cos_omega, y0 - radius * sin_omega), 
							(x0 + -radius * cos_omega, y0 - radius * sin_omega)]
		elif direction in [EAST, WEST]:
			self.view_area = [(x0 + radius * cos_omega, y0 + radius * sin_omega), 
							(x0 + radius * cos_omega, y0 + -radius * sin_omega)]
		elif direction in [NORTH_EAST, SOUTH_WEST]: 
			self.view_area = [(x0 + radius * sin_omega, y0 - radius * cos_omega), 
							(x0 + radius * cos_omega, y0 - radius * sin_omega)]
		elif direction in [NORTH_WEST, SOUTH_EAST]:
			self.view_area = [(x0 - radius * sin_omega, y0 + radius * cos_omega), 
							(x0 + radius * cos_omega, y0 - radius * sin_omega)]

	def __update_view_cells(self, matrix):
		result = []
		for x in range(25):
			for y in range(15):
				if self.see((x,y), matrix):
					result.append((x,y))
		self.view_cells = result

	def __update_view_area_FAAAK(self, matrix):
		radius = self.view_area_radius
		x0, y0 = self.position
		direction = self.direction if not self.direction == STOP else SOUTH
		position = self.position
		orts = TRIGONOMETRY_SUCKS[direction]['ort']

		all_points = []
		# all points in view area
		far_point = next_point(self.position, mul_tuple(direction, radius))
		start_line = cell_line(far_point,  orts[0], radius / 2 + 1)
		start_line += cell_line(far_point,  orts[1], radius / 2 + 1)
		for start in start_line:
			all_points += cell_line(start, TRIGONOMETRY_SUCKS[direction]['contr'], radius + 1)

		# walls in view area
		walls = [ p for p in all_points if not matrix[fix_for_borders(p)[1]][fix_for_borders(p)[0]] ]

		for p in all_points:
			if p in walls:
				all_points.remove(p)
		
		
		self.view_area = all_points
	

	def see_cell(self, what):
		return True if what in self.view_area else False

	def see(self, what, matrix):
		if self.position == what:
			return True
		x0, y0 = self.screen_position
		x1, y1 = c2s(what)

		radius = self.view_area_radius * X_CELL
		distantion = int(sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2))

		first = distantion < radius
		self.line_between = cell_line(self.position, p2d(self.position, what),3)

		
		second = p2d(self.screen_position, c2s(what)) is self.direction

		return first