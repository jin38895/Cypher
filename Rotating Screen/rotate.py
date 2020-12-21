import rotatescreen as rs
import keyboard as kd
import time

angle = [0,90,180,270]
screen = rs.get_primary_display()
while True:
	for i in angle:
		if kd.is_pressed('s'):
			screen.rotate_to(0)
			exit()
		elif kd.is_pressed('esc'):
			exit()
		else:
			screen.rotate_to(i)
			time.sleep(1)