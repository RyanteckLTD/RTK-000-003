#Programming the RTK-000-001 / RTK-000-003 using python

In this tutorial we will be showing you how to program your RTK-000-001 Motor Contoller to move around two motors for robots including the RTK-000-003 Budget Robotics Kit

##Creating the basis
First we will create the basis which will be used throughout. Start by either connecting via SSH or using a screen / VNC (Opening up LX Terminal) and running ```nano robotPython.py```

We will be first setting up and configuring the GPIO pins on the Raspberry Pi and then creating 4 functions which we will then be able to use to easily control both motors at the same time.

Start by adding in the following lines. You require to copy the code but not the comments indicated with the # symbol.

```
#
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)



```

