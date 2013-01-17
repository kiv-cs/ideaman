from buildings import *
from units import *
description = {
	'background':	'./images/level0_0.png',
	'hero' : 	{
			'construction': yellow_hero,
			'position':		(14, 10),
			'direction': 	(0, 0),
		},
	'enemies': [

		{
			'construction': red_enemy,
			'position':		(1, 1),
			'direction': 	(1, 0),
			'patrol_points': [(1,1),(14,14),(20,3)],	
		},
		{
			'construction': blue_enemy,
			'position':		(9, 7),
			'direction': 	(1, 0),
			'patrol_points': [(1,1),(14,14),(20,3)],	
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
	'walls': [
		{
			'construction':	small_house,
			'position':		(19, 11),
		},
		{
			'construction':	small_house,
			'position':		(3, 2),
		},
		{
			'construction':	large_house,
			'position':		(15, 7),		
		},
		{
			'construction':	blinking_stone,
			'position':		(24,10),
		},
		{
			'construction':	border_horisontal,
			'position':		(5, 3),
		},
		{
			'construction': border_horisontal,
			'position':		(13, 2)
		},
		{
			'construction':	border_left_up,
			'position':		(12, 2),
		},
		{
			'construction':	border_3_horisontal,
			'position':		(7, 5),
		},
		{
			'construction':	border_3_horisontal,
			'position':		(9, 5),
		},
		{
			'construction':	border_3_horisontal,
			'position':		(11, 5),
		},
		{
			'construction':	border_3_horisontal,
			'position':		(13, 5),
		},
		{
			'construction':	border_3_horisontal,
			'position':		(4, 6),
		},
		{
			'construction': large_house_L_style,
			'position':		(21, 9)

		},
		{
			'construction': border_horisontal,
			'position':		(15, 5)
		},
		{
			'construction': border_left_down,
			'position':		(20, 2)
		},
		{
			'construction': border_right_down,
			'position':		(6, 5)
		},
		{
			'construction': border_right_up,
			'position':		(3, 5)
		},
	]
}