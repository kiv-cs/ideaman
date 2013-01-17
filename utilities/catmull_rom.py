#! /usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt

def catmull_rom_trajectory(speed, points):
	if not speed:
		return None
	trajectory = []
	t_num = 10
	points = [points[0]] + points + [points[-1]]
	while len(points) > 3:
		# len = sqrt(x^2 + y^2)
		segment_len = sqrt((points[1][0] - points[2][0]) ** 2 + 
							(points[1][1] - points[2][1]) ** 2)
		t_num = segment_len / speed
		trajectory += catmull_rom_segment(t_num, points[:4])
		points = points[1:]
	return trajectory+[points[-1]]

def catmull_rom_segment(t_num, points):
	p0, p1, p2, p3 = points
	return [catmull_rom(t / float(t_num), p0, p1, p2, p3) 
								for t in range(int(t_num))]

def catmull_rom(t, p0, p1, p2, p3):
	x0, y0 = p0
	x1, y1 = p1
	x2, y2 = p2
	x3, y3 = p3
	x = .5 * ( (2 * x1) + ( - x0 + x2 ) * t + 
				( 2 * x0 - 5 * x1 + 4 * x2 - x3 ) * t ** 2 + 
				( - x0 + 3 * x1 - 3 * x2 + x3) * t ** 3)
	y = .5 * ( (2 * y1) + ( - y0 + y2 ) * t + 
				( 2 * y0 - 5 * y1 + 4 * y2 - y3 ) * t ** 2 + 
				( - y0 + 3 * y1 - 3 * y2 + y3) * t ** 3) 
	return int(x), int(y)