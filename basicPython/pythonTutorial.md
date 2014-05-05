#Programming the RTK-000-001 / RTK-000-003 using python

In this tutorial we will be showing you how to program your RTK-000-001 Motor Contoller to move around two motors for robots including the RTK-000-003 Budget Robotics Kit

##Creating the basis
First we will create the basis which will be used throughout. Start by either connecting via SSH or using a screen / VNC (Opening up LX Terminal) and running ```nano robotPython.py```

We will be first setting up and configuring the GPIO pins on the Raspberry Pi and then creating 4 functions which we will then be able to use to easily control both motors at the same time.

Start by adding in the following lines. You require to copy the code but not the comments indicated with the # symbol.

```
#RTK-000-001 Basis
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley, Michael Horne
from time import sleep #We will need to sleep the code at points
import RPi.GPIO as GPIO #Import the GPIO library as GPIO

#Setup GPIO
GPIO.setmode(GPIO.BCM) # Set the numbers to Broadcom Mode
GPIO.setwarnings(False) # Ignore any errors

GPIO.setup(17,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(18,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(22,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(23,GPIO.OUT) #Set 23 as output (Motor 2 B)

```
This has now setup the GPIO pins ready for use.

Now we will make a function to turn both motors forward, add the following now to your code.

```
#Make both motors go forwards
def forwards():
        GPIO.output(17,1) # Motor 1 Forwards turn off
        GPIO.output(18,0) # Motor 1 Backwards turn off
        GPIO.output(22,1) # Motor 2 Forwards turn on
        GPIO.output(23,0) # Motor 2 Backwards turn off
```
Next we need to add in a stop function, add this after the code above
```
##All off
def stop():
        GPIO.output(17,0) # Motor 1 Forwards turn off
        GPIO.output(18,0) # Motor 1 Backwards turn off
        GPIO.output(22,0) # Motor 2 Forwards turn off
        GPIO.output(23,0) # Motor 2 Backwards turn off
```
Finally we want to add in a small loop to make the motors go forwards for one second and then stop for another.
Do this by adding the following
```
#Forever
while True:
    #Turn motors forward
    forwards()
    #sleep for 1 second
    sleep(1)
    #Stop
    stop()
    #sleep 1 second
    sleep(1)
```

Now we can save the code by running the following commands, ```Ctrl + X``` to save, ```y``` to confirm writing and then ```enter``` to confirm to save.

We now want to run our python code
