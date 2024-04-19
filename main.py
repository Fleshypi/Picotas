from machine import Pin
import time

count = 0
freq = 100

while True:
    if Pin(2, Pin.IN, Pin.PULL_DOWN).value():
        count += 1
		Pin(1).toggle()
  	  time.sleep(1/freq/2)
    if count > (1/freq/2):
        Pin(1).toggle()
        time.sleep(1)
        count = 0
