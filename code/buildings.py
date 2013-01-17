#
# This file contains descriptions of buildings (image path and matrix of closed cells)
# Level description could import buildings just by name
#

# REMEMBER: image path must be the same as for level.py
void = {	
	'image': 			'./images/buildings/border_horisontal.png',
	'animation_count': 	1,
	'frame_count':		1,
	'closed_cells':		[
							[1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,],
							[1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,],
							[1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,],
							[1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,],
							[1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,],
							[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
							[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
						]
}

border_horisontal = {
	'image': 			'./images/buildings/border_horisontal.png',
	'animation_count': 	1,
	'frame_count':		1,
	'closed_cells':		[
							[1,0,0,0,0,0,0,0],
						]

}

border_left_up = {
	'image':			'./images/buildings/border_left_up.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[1,0],
							[0,0]
						]
}

border_left_down = {
	'image':			'./images/buildings/border_left_down.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[0,0],
							[1,0]
						]
}

border_right_down = {
	'image':			'./images/buildings/border_right_down.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[0,0],
							[0,1]
						]
}

border_right_up = {
	'image':			'./images/buildings/border_right_up.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[0,1],
							[0,0]
						]
}


small_house = {
	'image':			'./images/buildings/small_house.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[1,1,1],
							[0,0,1]
						]
}

large_house = {
	'image':			'./images/buildings/large_house.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[1,1,1,1,1,1,1],
							[1,1,1,1,1,1,1],
							[1,1,1,1,1,1,1],
							[1,1,1,1,1,1,1],
							[1,1,0,0,0,0,0],
							[1,0,0,0,0,0,1]
						]
}

large_house_L_style = {
	'image':			'./images/buildings/large_house_L_style.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[1,1,1,1,1,1,1],
							[1,1,1,1,1,1,1],
							[1,1,0,0,1,1,1],
							[1,0,0,0,0,1,1]
						]
}

blinking_stone = {
	'image':			'./images/buildings/blinking_stone.png',
	'animation_count':	1,
	'frame_count':		3,
	'closed_cells':		[
							[0]
						]
}

border_3_horisontal = {
	'image':			'./images/buildings/border_3_horisontal.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[1, 0, 0]
						]
}

border_3_vertical = {
	'image':			'./images/buildings/border_3_vertical.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[0],
							[0],
							[0]
						]
}

border_3_cross = {
	'image':			'./images/buildings/border_3_cross.png',
	'animation_count':	1,
	'frame_count':		1,
	'closed_cells':		[
							[0,1,0],
							[1,0,1],
							[0,1,0]
						]
}