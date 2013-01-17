#
# This file contains descriptions of units
# Level description could import units just by name
# units is enemies, citizens and hero
#
# REMEMBER: image path must be the same as for level.py

yellow_hero = {
		'image':	'./resources/images/units/hero.png',
		'speed':			5,
		'animation_count':	9,
		'frame_count':	3,
		'color':		(255,255,0),
		'goal':			None
}

# ============== ENEMIES ======================== #
blue_enemy = {
		'image':	'./resources/images/units/ghost_dotted.png',
		'speed':			3,
		'animation_count':	9,
		'frame_count':	4,
		'color':		(0,0,255),
		'goal':			None,
		'target':		'hero',
		
		'style':		'blinky',
		'mode':			'patrol',
}

red_enemy = {
		'image':	'./resources/images/units/ghost1.png',
		'speed':			3,
		'animation_count':	9,
		'frame_count':	4,
		'color':		(255,0,0),
		'goal':			None,
		'target':		'hero',
	
		'style':		'pinky',
		'mode':			'patrol',
}

# ================ CITIZENS ======================= #
green_citizen = {
		'image':	'./resources/images/units/white_robot.png',
		'speed':			2,
		'animation_count':	9,
		'frame_count':	4,
		'color':		(0,255,0),
		'goal':			None,
	
		'style':		'simple',
		'mode':			'patrol',	


}