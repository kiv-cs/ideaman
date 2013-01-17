from configs.buildings import *
from configs.units import *
from configs.config import *

LOCATION_PERIMETER = [(0,0), (X_CELL_NUM-1, 0), (X_CELL_NUM-1, Y_CELL_NUM-1), (0,Y_CELL_NUM-1)]

description = {
	'background':	'./resources/images/level0_0.png',
	'hero' : 	{
			'construction': yellow_hero,
			'position':		(14, 14),
			'direction': 	(0, 0),
		},
	'enemies': [

		{
			'construction': blue_enemy,
			'position':		(14, 3),
			'direction': 	(0, 0),
			'patrol_points': [(0,3), (24,4), (10,0)],
		},
		{
			'construction': blue_enemy,
			'position':		(0, 0),
			'direction': 	(0, 0),
			'patrol_points': LOCATION_PERIMETER,
		},
		{
			'construction': red_enemy,
			'position':		(3, 14),
			'direction': 	(0, 0),
			'patrol_points': [(0,9), (7,14), (24,10), (10,7)],
		},
	],
	'citizens': [

		{
			'construction': green_citizen,
			'position':		(6,6),
			'direction': 	(0, 0),
			'home': 	(20, 4),
			'patrol_points': [(6,6), (11,7)],
		},
		{
			'construction': green_citizen,
			'position':		(6,6),
			'direction': 	(0, 0),
			'home': 	(20, 4),
			'patrol_points': [(1,13), (2,13)],
		},
		{
			'construction': green_citizen,
			'position':		(6,6),
			'direction': 	(0, 0),
			'home': 	(20, 4),
			'patrol_points': [(16,0), (19,0)],
		},
	],
	'walls': 

		[{'construction': border_3_horisontal, 'position': (x,2)}
		for x in range(2, 16, 2)] + 
		[{'construction': border_3_horisontal, 'position': (x,5)}
		for x in range(8, 22, 2)] +
		[{'construction': border_3_horisontal, 'position': (x,8)}
		for x in range(2, 16, 2)] +
		[{'construction': border_3_horisontal, 'position': (x,11)}
		for x in range(8, 22, 2)] +
		[{'construction': border_3_vertical, 'position': (4,y)}
		for y in range(2, 6, 2)] +
		[{'construction': border_3_vertical, 'position': (4,y)}
		for y in range(8, 12, 2)] +


		[
			{'construction': small_house,
			 'position': (20, 2)
			},

		]
		
}