#! /usr/bin/python
# -*- coding: utf-8 -*-

from classes.general import *

from pygame import time
from pygame import event as pgevent

try:
	import android
except ImportError:
	android = None

from configs.config import *


general = General()
clock = time.Clock()

pause = False

while True:

	if android:
		if android.check_pause():
			android.wait_for_resume()

	for event in pgevent.get():
		
		if event.type is KEYDOWN and event.key is 13:
			if pause:
				pause = False
			elif not pause:
				pause = True
				continue

		general.event(event)
		general.location.event(event)

	if pause: continue

	general.location.update()
	general.location.draw()

	display.flip()
	clock.tick(DT)