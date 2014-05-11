#RTK-000-001 Python Basis
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley, Michael Horne
import time
import RPi.GPIO as GPIO
#Import spacebrew library
from spacebrew import Spacebrew

#Setup GPIO
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

def left():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,1)
        GPIO.output(23,0)

def right():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,1)

def stop():
        GPIO.output(17,0)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,0)

#setup Spacebrew
name = "Cake"
robotName = "RTK-000-003: "+ name
brew = Spacebrew(robotName, server="sandbox.spacebrew.cc")

brew.addSubscriber("forward", "boolean")
brew.addSubscriber("backward", "boolean")
brew.addSubscriber("left", "boolean")
brew.addSubscriber("right", "boolean")

def fwd_hndl(value):
    # do something with the value received
    forwards()
    time.sleep(0.03)
    stop()
def bk_hndl(value):
    backwards()
    time.sleep(0.03)
    stop()
def lt_hndl(value):
    left()
    time.sleep(0.03)
    stop()
def rt_hndl(value):
    right()
    time.sleep(0.03)
    stop()

brew.subscribe("forward", fwd_hndl)
brew.subscribe("backward", bk_hndl)
brew.subscribe("left", lt_hndl)
brew.subscribe("right", rt_hndl)

try:
    brew.start()
    while True:
        pass
finally:
    brew.stop()
