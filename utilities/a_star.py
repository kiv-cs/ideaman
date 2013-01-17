#! /usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt

DELTA = [
		[-1, 0],
		[0, -1],
		[1, 0],
		[0, 1],
		[1, 1],
		[-1, -1],
		[1, -1],
		[-1, 1]
	]

# TODO: update to deikstera: h = [0]
# matrix - is a level map with 0 (no way here) and 1 (ok go)
# start, goal - tuples (x,y)
# return path [(x1,y1), (x2,y2) etc] - base points (need smoothing)
def a_star(matrix, start, goal):
	path = []
	heuristic = __heuristic_func(matrix, goal)
	g = 0
	x_start, y_start = start
	h = heuristic[y_start][x_start]
	f = h + g
	opened = [{'f':f, 'g':g, 'h':h, 'coords':start, 'parent':start}]
	closed = []
	found = False

	cost_straight = 10
	cost_diagonal = 14

	while opened:
		opened.sort(key=lambda l: l['f'], reverse=True)
		current = opened.pop()
		closed.append(current)
		x_current, y_current = current['coords']
		# take every cells around
		for x, y in [(x_current + d[0], y_current + d[1]) for d in DELTA]:
			# ignore if
			if     ((x < 0) 
				or (x > len(matrix[0]) - 1) 
				or (y < 0) 
				or (y > len(matrix) - 1)
				or not matrix[y][x] # it is wall
				or ((x, y) in [i['coords'] for i in closed])): #it is in closed
				continue
			
			cost = cost_straight if x == x_current or y == y_current else cost_diagonal # differen cost for directions
			g = current['g'] + cost
			h = heuristic[y][x]
			f = g + h
			
			# stupid thing: check if point with this coords is opened
			in_opened = [i for i in opened if i['coords'] == (x,y)]
			
			if not in_opened:		
				opened.append({'f':f, 'g':g, 'h':h, 'coords':(x, y), 'parent':current['coords']})
			else:
				# if in opened and g1 > g: remove, cause our point better
				if in_opened[0]['g'] > g:
					opened.remove(in_opened[0])
					opened.append({'f':f, 'g':g, 'h':h, 'coords':(x, y), 'parent':current['coords']})

			if (x, y) == goal:
				found = True

				# need goal in closed cause start cleaning from it
				closed.append({'f':f, 'g':g, 'h':h, 'coords':(x, y), 'parent':current['coords']})
				return __clear_path(closed, goal, start)

	return False
#
# just simple heuristic 
#
def __heuristic_func(matrix, goal):
	x, y = goal
	h = [[(abs(x - x_i) + abs(y - y_i)) * 10 
			for x_i in range(len(matrix[0]))] 
			for y_i in range(len(matrix))]
	return h

#
# take closed list, find chain of parent-child, return path
#
def __clear_path(path, current, start):
	clear_path = [current] # first current is goal
	next_p = 0
	while not next_p == start:
		next_p = [i['parent'] for i in path if i['coords'] == current]
		if next_p:
			next_p = next_p[0]
		else:
			break
		clear_path.append(next_p)
		current = next_p
	clear_path.reverse()
	return clear_path