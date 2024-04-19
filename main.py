from machine import Pin
import time
import config

frame = 1/config.framerate
count = 0

while count <= len(tas):
	Pin(config.tas[count]).toggle()
	count += 1
	time.sleep(frame)
