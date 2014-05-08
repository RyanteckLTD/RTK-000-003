#RTK-000-001 Bash / CLI Controller
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley
import time
import curses
from sys import exit
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

def forwards():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,1)
        GPIO.output(23,0)

def backwards():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,0)
        GPIO.output(23,1)

def turn_left():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,1)
        GPIO.output(23,0)

def turn_right():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,1)

def stop():
        GPIO.output(17,0)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,0)

shell = curses.initscr()
shell.nodelay(False)

while True:
    key = shell.getch()

    if key == 119:
        print("Forward")
        forwards()
	#time.sleep(0.1)
    elif key == 115:
        print ("Backward")
        backwards()    
	#time.sleep(0.1)    

    elif key == 97:
        print ("Left")
        turn_left()
	#time.sleep(0.1)

    elif key == 100:
        print ("Right")
        turn_right()
	#time.sleep(0.1)

      
    if key == 24:
        curses.endwin()
        exit(0)
    time.sleep(0.03)
    stop()

