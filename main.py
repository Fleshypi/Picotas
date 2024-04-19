from machine import Pin
import time

## Frame rate ##

framerate = 60
frame = 1/framerate
count = 0


tas = ["up","down","up","down","left","right","left","right","b","a","start","select"]

while count <= len(tas):
	Pin(tas[count]).toggle()
	count += 1
	time.sleep(frame)
