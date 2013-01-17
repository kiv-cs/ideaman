#! /usr/bin/python
# -*- coding: utf-8 -*-

from math import sin, pi, cos



# ============ BASIC SETTINGS =========== #

K = 1.				# size koefficient

X_RESOLUTION = 800
Y_RESOLUTION = 480

MAIN_FONT = './resources/po.ttf'

DT = 30
ANIMATION_TIME = 180
# SPRITE_SIZE = 32

# ============= COORDINATES =============== #
X_MAX = int(X_RESOLUTION / K) 	# current horizontal resolution 
Y_MAX = int(Y_RESOLUTION / K)	# current vertical resolution

X_HALF = int(X_MAX / 2.)
Y_HALF = int(Y_MAX / 2.)

X_CELL_NUM = 25 		# number of cells in X axe 
Y_CELL_NUM = 15 		# number of cells in Y axe

X_CELL = int(X_MAX / float(X_CELL_NUM))	# X cell resolution
Y_CELL = int(Y_MAX / float(Y_CELL_NUM))	# Y cell resolution

CELL_SIZE = (X_CELL, Y_CELL)

# =============== FONTS ======================= #

LARGE_FONT_SIZE = int(X_CELL / 1.)
MEDIUM_FONT_SIZE = int(X_CELL / 2.)
SMALL_FONT_SIZE = int(X_CELL / 4.)

# ============== LEVELS ======================= #
# refact this when will know about modules

import level0_0
import level0_1
import level0_2

LOCATION = [level0_1.description, level0_0.description, level0_2.description]

# ============== DIRECTIONS =================== #
STOP = (0, 0)
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
NORTH_WEST = (-1, -1) # sin(45) ~ 1
SOUTH_EAST = (1, 1)
NORTH_EAST = (1, -1)
SOUTH_WEST = (-1, 1)
# save this order especially for images! (for big sprites from top to bottom - stop sprite, north sprite etc.)
DIRECTIONS = [STOP, NORTH, SOUTH, EAST, WEST, NORTH_WEST, NORTH_EAST, SOUTH_EAST, SOUTH_WEST]

# =============== KEY CODES =================== #
# keycodes for numpad keys
#
K_NUM_DOWN = 258			# 2
K_NUM_DOWN_LEFT = 257		# 1
K_NUM_LEFT = 260			# 4
K_NUM_UP_LEFT = 263			# 7
K_NUM_UP = 264				# 8
K_NUM_UP_RIGHT = 265		# 9
K_NUM_RIGHT = 262			# 6
K_NUM_DOWN_RIGHT = 259		# 3
K_NUM_STOP = 261			# 5
# general keycodes, as in pygame
K_DOWN = 274
K_UP = 273
K_LEFT = 276
K_RIGHT = 275
K_SPACE = 32
# mapping
KEY_DIRECTION_MAP = {
	K_DOWN: 			SOUTH,
	K_NUM_DOWN: 		SOUTH,
	K_UP: 				NORTH,
	K_NUM_UP: 			NORTH,
	K_LEFT: 			WEST,
	K_NUM_LEFT: 		WEST,
	K_RIGHT: 			EAST,
	K_NUM_RIGHT: 		EAST,
	K_NUM_UP_LEFT: 		NORTH_WEST,
	K_NUM_DOWN_RIGHT: 	SOUTH_EAST,
	K_NUM_UP_RIGHT: 	NORTH_EAST,
	K_NUM_DOWN_LEFT: 	SOUTH_WEST,
	K_SPACE: 			STOP,
	K_NUM_STOP: 		STOP,
}

# ============= DIRECTION TO POSITION =========== #
SIN_PI_6 = sin(pi / 6)
SIN_PI_3 = sin(pi / 3)
COS_PI_6 = cos(pi / 6)
MORE_THAN_SIN_PI_3 = 0.95

# ============== FOR VIEW AREA ================== #
TRIGONOMETRY_SUCKS = { 
	NORTH: 		{
				'ort':		[EAST, WEST],
				'rad':		pi / 2,
				'contr':	SOUTH,
				},
	SOUTH: 		{		
				'ort': 		[EAST, WEST],
				'rad':		3 * pi / 2,
				'contr':	NORTH,
				},
	WEST: 		{		
				'ort': 		[NORTH, SOUTH],
				'rad':		pi,
				'contr':	EAST,
				},		
	EAST:		{		
				'ort': 		[NORTH, SOUTH],
				'rad':		0,
				'contr':	WEST,
				},		
	NORTH_EAST: {		
				'ort': 		[NORTH, EAST],
				'rad':		pi / 4,
				'contr':	SOUTH_WEST,
				},		
	SOUTH_WEST:	{		
				'ort': 		[SOUTH, WEST],
				'rad':		5 * pi / 4,
				'contr':	NORTH_EAST,
				},		
	SOUTH_EAST:	{		
				'ort': 		[SOUTH, EAST],
				'rad':		7 * pi / 4,
				'contr':	NORTH_WEST,
				},		
	NORTH_WEST:	{		
				'ort': 		[NORTH, WEST],
				'rad':		3 * pi / 4,
				'contr':	SOUTH_EAST,
				},
	STOP:  		{	# just as south	
				'ort': 		[SOUTH_EAST, SOUTH_WEST],
				'rad':		3 * pi / 2,
				'contr':	NORTH,
				},	
}