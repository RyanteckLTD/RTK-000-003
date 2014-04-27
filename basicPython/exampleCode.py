#RTK-000-001 Simple SSH Python controller
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014

#We want to be able to sleep but don't need all of time & space, just import sleep
from time import sleep
#We alos need to use RPi.GPIO but we want to use it as GPIO
from RPi.GPIO as GPIO

#Setup the Pi to use BCM mode
GPIO.setmode(GPIO.BCM)
#Output the pins 17,18,22,23

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

#All Pins setup!
