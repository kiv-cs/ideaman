from buildings import *
from units import *
description = {
	'background':	'./images/level0_1.png',
	'hero' : 	{
			'construction': yellow_hero,
			'position':		(24, 14),
			'direction': 	(0, 0),
		},
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
	'enemies': [

		{
			'construction': red_enemy,
			'position':		(14, 3),
			'direction': 	(0, 0),
			'patrol_points': [(1,1),(14,14),(20,3)],	
		},
		{
			'construction': blue_enemy,
			'position':		(3, 14),
			'direction': 	(0, 0),
			'patrol_points': [(1,1),(14,14),(20,3)],	
		},
	],
	'walls': [
		{
			'construction':	void,
			'position':		(0,0)
		}
		
	]
}