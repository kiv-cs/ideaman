from configs.config import *

def coord_to_screen((x, y)):
	return (x * X_CELL + X_CELL / 2, y * Y_CELL + Y_CELL / 2)

def screen_to_coord((x, y)):
	return (int(round((x - X_CELL / 2) / float(X_CELL))), 
		int(round((y - Y_CELL / 2 )/ float(Y_CELL))))

# because pygame.rect position sets as top-left corner position
def coord_to_rect((x, y)):
	return (x * X_CELL, y * Y_CELL)

def screen_to_rect((x, y)):
	return (x - X_CELL / 2, y - Y_CELL / 2)

def delta(from_where, to):
	x0, y0 = from_where
	x1, y1 = to
	return (x1 - x0, y1 - y0)

def sum_tuples(a, b):
	x0, y0 = a
	x1, y1 = b
	return (x0+x1, y0+y1)
	
def mul_tuple(a, mul):
	x, y = a
	return (x * mul, y * mul)

def next_point(point, direction):
	x0, y0 = point
	dx, dy = direction
	return (x0 + dx, y0 + dy)

# check if TEST on line BEGIN-END 
def is_points_on_line(begin, end, test):
	x, y = test
	x0, y0 = begin
	x1, y1 = end
	try:
		return (y - y0) / (y1 - y0) == (x - x0) / (x1 - x0)
	except ZeroDivisionError:
		return test == begin or test == end

def cell_line(start, direction, length):
		return [ next_point(start, mul_tuple(direction, l)) for l in range(length) ]


# position to direction 
# REMEMBER: Y grows SOUTH
def position_to_direction(begin, end):
	if begin == end:
		return False
	x0, y0 = begin
	x1, y1 = end
	is_vertical = False
	try:
		p_sin = float(y1 - y0) / float(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5)
		# print 'from % s to %s' % (begin, end)
		# print 'sin %s / %s = %s' % (y1-y0, float(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), p_sin)
		# print 'sin pi/6 = %s, print sin pi/3 = %s' % (SIN_PI_6, MORE_THAN_SIN_PI_3)
	except ZeroDivisionError:
		is_vertical = True		
	# if right side (from 3pi/2 to pi/2)
	if not is_vertical:
		if x1 > x0:
			if (-SIN_PI_6 <= p_sin) and (p_sin <= SIN_PI_6):
				direction = EAST
			elif (SIN_PI_6 <= p_sin) and (p_sin <= MORE_THAN_SIN_PI_3):
				direction = SOUTH_EAST
			elif (-MORE_THAN_SIN_PI_3 <= p_sin) and (p_sin <= -SIN_PI_6):
				direction = NORTH_EAST
		else:
			if (-SIN_PI_6 <= p_sin) and (p_sin <= SIN_PI_6):
				direction = WEST
			elif (SIN_PI_6 <= p_sin) and (p_sin <= MORE_THAN_SIN_PI_3):
				direction = SOUTH_WEST
			elif (-MORE_THAN_SIN_PI_3 <= p_sin) and (p_sin <= -SIN_PI_6):
				direction = NORTH_WEST
		if p_sin >= MORE_THAN_SIN_PI_3: direction = SOUTH
		if p_sin <= -MORE_THAN_SIN_PI_3: direction = NORTH
	else:
		if y1 <= y0: direction = NORTH
		if y1 > y0: direction = SOUTH	
	return direction

# dict {caption: value}
def write_log(something):
	logfile = open('log.txt', 'a')
	text = ''
	for s in something:
		text += '%s : %s ||' % (s, something[s])
	logfile.write(text + '\n')
	logfile.close()

# form=c => coords
# else screen coords
def fix_for_borders(point, form='c'):
	x, y = point
	x_max, y_max = (X_CELL_NUM, Y_CELL_NUM) if form=='c' else (X_MAX, Y_MAX)
	if x >= x_max:
		x = x_max - 1
	if x < 0:
		x = 0
	if y >= y_max:
		y = y_max - 1
	if y < 0:
		y = 0
	return (x, y)



# print coord_to_screen((0,0)), screen_to_coord((44,34))
# print screen_to_coord((0,0))
# assert coord_to_screen((10, 10)) == (10 * X_CELL + X_CELL / 2, 10 * Y_CELL + Y_CELL / 2)
# assert screen_to_coord((25,25)) == (0,0)

print position_to_direction((247, 379), (260, 347))
print position_to_direction((260, 260), (292, 294))
print coord_to_rect((10, 10))