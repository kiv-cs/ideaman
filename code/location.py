#! /usr/bin/python
# -*- coding: utf-8 -*-
from pygame import display
from pygame import image
from pygame import draw
from pygame import font
from pygame import mouse
from pygame import KEYDOWN, K_SPACE
from pygame import time, USEREVENT


from config import *

from hero import *
from enemy import *
from wall import *
from citizen import *

from utils import coord_to_screen as c2s
from utils import screen_to_coord as s2c
from utils import delta as d
from utils import fix_for_borders
from utils import next_point, mul_tuple


class Location():
	def __init__(self, index=0):
		print '%s here' % self.__name__()
		self.index = index
		self.window = display.get_surface()
		self.load(LOCATION[index])
		self.is_debug = False

		self.background = image.load(self.bg_path)

		self.hero = Hero(self.hero_description)
		self.enemies = [Enemy(description) for description in self.enemies_description]
		self.enemies_group = sprite.Group()

		self.citizens = [Citizen(description) for description in self.citizens_description]

		self.citizens_group = sprite.Group()
		# refactor this
		for enemy in self.enemies:
			if enemy.target == 'hero': enemy.target = self.hero
			enemy.add(self.enemies_group)

		for citizen in self.citizens:
			citizen.add(self.citizens_group)


		self.walls = [Wall(description) for description in self.walls_description]

		# hero first, than enemies, than walls - will draw in this order
		self.gaming_objects = []
		self.gaming_objects.append(self.hero)
		self.gaming_objects += self.enemies + self.walls + self.citizens

		self.note_font = font.Font("../fonts/ap.ttf", MEDIUM_FONT_SIZE)
		# self.notification_text = ''

	def __name__(self):
		return 'Location'

	def load(self, description):
		self.bg_path = description['background']
		self.hero_description = description['hero']
		self.enemies_description = description['enemies']
		self.citizens_description = description['citizens']
		self.walls_description = description['walls']
		self.__load_matrix()

	def __load_matrix(self):
		self.matrix = [[1 for x in range(X_CELL_NUM)] for y in range(Y_CELL_NUM)]
		self.closed = []
		for wall in self.walls_description:
			x0, y0 = wall['position']
			wall_matrix = wall['construction']['closed_cells']
			for y in range(len(wall_matrix)):
				for x in range(len(wall_matrix[y])):
					# 3rd condition - to not replace 0 from one wall to 1 from another
					# so replace only if new val is 0
					if (y0 + y < X_CELL_NUM) and (x0 + x < X_CELL_NUM) and not wall_matrix[y][x]: 
						self.matrix[y0+y][x0 + x] = wall_matrix[y][x]

	def event(self, event):
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				self.is_debug = not self.is_debug
		if event.type == KEYDOWN:
			print event.key

		
		for obj in self.gaming_objects:
			obj.event(event)

	# updates everything what includes more then one object
	def update(self):
		self.__update_notes()
		for obj in self.gaming_objects:
			if not obj.is_active:
				self.gaming_objects.remove(obj)
				if obj.__name__() is 'Citizen':
					self.citizens_group.remove(obj)
			obj.update(self.matrix)
			obj.move()

		# == collisions mazafaka == #
		hero_enemy_collision = sprite.spritecollideany(self.hero, self.enemies_group)
		hero_citizen_collision = sprite.spritecollideany(self.hero, self.citizens_group)

		if hero_enemy_collision:
			if not self.is_debug:
				self.level_failed()

		if hero_citizen_collision:
			self.hero.talking()
			hero_citizen_collision.hear_hero = True
		# ========================= #

		if not len(self.citizens_group):
			self.level_done()

		


	def __update_notes(self):
		speed = 'Speed: %s' % self.hero.speed
		goal = 'Goal: %s' % str(self.hero.goal)
		notes = [speed, goal]
		# rendered notes
		self.notes = [self.note_font.render(note, 0, (0,255,0)) for note in notes]

	def draw(self):
		self.window.blit(self.background, (0, 0))
		if self.is_debug:
			self.__draw_walls()
			self.__draw_grid()
			for obj in self.gaming_objects:
				self.__draw_trajectory(obj.trajectory)
				if not (obj.__name__() == 'Wall'):
					self.__draw_goal(obj.goal, obj.color)
			for enemy in self.enemies:
				self.__draw_view_area(enemy)
				self.__draw_view_cells(enemy)
			# self.notes contains rendered strings
			dy = 0
			for note in self.notes:
				self.window.blit(note, (0, 0 + dy))
				dy += int(Y_CELL * 0.6)

		for obj in self.gaming_objects:
			obj.draw(self.window)

		
	def level_failed(self):
		self.__init__(self.index)

	def level_done(self):
		
		try:
			self.__init__(self.index + 1)
		except IndexError:
			print 'WIN'

		

	# ==== self.is_debug only ========= #
	def __draw_grid(self):
		for _ in range(0, X_CELL_NUM):
			draw.line(self.window, (50, 50, 50), (X_CELL * _, 0), (X_CELL * _, Y_MAX))
		for _ in range(0, Y_CELL_NUM):
			draw.line(self.window, (50, 50, 50), (0, Y_CELL * _), (X_MAX, Y_CELL * _))

	def __draw_walls(self):
		closed = [(x,y) for y in range(len(self.matrix)) for x in range(len(self.matrix[0])) 
						if not self.matrix[y][x]]

		for c in closed:
			x, y = c2r(c)
			draw.polygon(self.window, (100, 50, 50), 
				[(x,y), (x + X_CELL, y), (x + X_CELL, y + Y_CELL), (x, y + Y_CELL)])

	def __draw_trajectory(self, trajectory):
		if trajectory:
			for point in trajectory:
				draw.circle(self.window, (0,0,255), point, 3)

	def __draw_goal(self, goal, color):
		if goal:
			draw.circle(self.window, color, c2s(goal), 3)

	def __draw_view_cells(self, obj):
		color = obj.color
		if obj.mode is 'hunting':
			color = (255, obj.color[1], obj.color[2])

		for point in obj.view_cells:
			tl = c2r(point)
			tr = tl[0] + X_CELL, tl[1]
			br = tr[0], tr[1] + Y_CELL
			bl = br[0] - X_CELL, br[1]

			draw.polygon(self.window, color, (tl, tr, br, bl), 1)


	def __draw_view_area(self, obj):
		color = obj.color
		if obj.mode is 'hunting':
			color = (255, obj.color[1], obj.color[2])



		draw.line(self.window, color, obj.screen_position, obj.view_area[0])
		draw.line(self.window, color, obj.screen_position, obj.view_area[1])
		#draw.circle(self.window, obj.color, obj.screen_position, obj.view_area_radius, 1)

		r = obj.view_area_radius * X_CELL
		a = obj.view_area_angle

		draw.arc(self.window, color, 
				(d((r, r), obj.screen_position), 
							(r * 2, r * 2)),
				TRIGONOMETRY_SUCKS[obj.direction]['rad'] - a, 
							TRIGONOMETRY_SUCKS[obj.direction]['rad'] + a)






