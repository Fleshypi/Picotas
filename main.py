from machine import Pin
import time
import config
## Frame rate ##

framerate = 60
frame = 1/framerate
count = 0



while count <= len(tas):
	Pin(tas[count]).toggle()
	count += 1
	time.sleep(frame)
