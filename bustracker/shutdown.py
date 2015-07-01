# http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
# link includes wiring diagram for two tactile switches

import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def restartNow(channel):
	#print("Button 1 pressed!")
	#print("Note how the bouncetime affects the button press")
	os.system("sudo shutdown -r now")
	time.sleep(.02)	
	
def shutdownNow(channel):
	#print("Button 1 pressed!")
	#print("Note how the bouncetime affects the button press")
	os.system("sudo shutdown -r now")
	time.sleep(.02)		

GPIO.add_event_detect(23, GPIO.RISING, callback=restartNow, bouncetime=300)
GPIO.add_event_detect(24, GPIO.FALLING, callback=shutdownNow, bouncetime=300)

while True:
	time.sleep(1)

GPIO.cleanup()