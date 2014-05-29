#Programming the RTK-000-001 / RTK-000-003 using C

In this tutorial we will be showing you how to program your RTK-000-001 Motor Contoller to move around two motors for robots including the RTK-000-003 Budget Robotics Kit

**Install some necessary software**
First make sure your Pi is up to date with the latest versions of Raspbian:

```sudo apt-get update```
```sudo apt-get upgrade```

If you do not have Git installed, then under Raspbian (or any of the Debian releases) you can install it with:

```sudo apt-get install git-core```

**Download and Install wiringPi (the C library for controlling GPIOs)**

First of all, obtain WiringPi using Git:

```git clone git://git.drogon.net/wiringPi```

Now build/install it using this script:

```cd wiringPi```
``` ./build ```

This script will compile and install it all for you.

##Creating the basis
First we will create the basis which will be used throughout. Start by either connecting via SSH or using a screen / VNC (Opening up LX Terminal) and running ```nano robotC.c```

We will be first setting up and configuring the GPIO pins on the Raspberry Pi and then creating 4 functions which we will then be able to use to easily control both motors at the same time.

Start by adding in the following lines.

```
#include <stdio.h>

//import the neccesary mdoule to control GPIOs
#include <wiringPi.h>

//make global variables to store the wiring pi pin numbers for the motors
int m1a = 0;
int m1b = 1;
int m2a = 3;
int m2b = 4;

//main function
int main (void)
{
  //setup the GPIO module
  wiringPiSetup();
  //set the pins up as outputs
  pinMode(m1a, OUTPUT);
  pinMode(m1b, OUTPUT);
  pinMode(m2a, OUTPUT);
  pinMode(m2b, OUTPUT);
  return 0;
}
```

This has now setup the GPIO pins ready for use.

Now we will create a function to turn both motors in the forward direction. Add the following to your code.

```
//make robot go forwards
void forwards()
{
  digitalWrite(m1a, HIGH);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, HIGH);
  digitalWrite(m2b, LOW);
}
```
Next we need to add in a stop function, add this after the code above
```
//all motors off
void stop()
{
  digitalWrite(m1a, LOW);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, LOW);
  digitalWrite(m2b, LOW);
}
```
Finally we want to add in a small loop to make the motors go forwards for half a second and then stop for another.
Do this by changing our 'int main(void)' function to this (replace the old one with this):
```
//main function
int main (void)
{
  //setup the GPIO module
  wiringPiSetup();

  //set the pins up as outputs
  pinMode(m1a, OUTPUT);
  pinMode(m1b, OUTPUT);
  pinMode(m2a, OUTPUT);
  pinMode(m2b, OUTPUT);

  for (;;)
  {
    //Turn motors forward
    printf("forwards");
    forwards();
    delay(500);

    //Stop
    printf("stop");
    stop();
    delay(500);
  }
  return 0;
}
```

Now we can save the code by running the following commands, ```Ctrl + X``` to save, ```y``` to confirm writing and then ```enter``` to confirm to save.

We now want to run our python code, do this by running ```gcc -Wall -o robotC robotC.c -lwiringPi``` to compile and then ```sudo ./robotC``` to run, the motors should move forwards and print forwards and stop each time they start going forwards or stop.

####Troubleshooting direction
It is likely that the first time you run your code the motors will move in oposite directions, this can be easily fixed using either a small code change or swapping a wire over on the board.

#####Code Fix
First identify which motor is going in the wrong direction and follow the cable to the board. If it is M1 then swap m1a to be 1 and m1b to be 0, if it is M2 then change m2a to be 4 and m2b to be 3. Re run the code and you should have them both going the right way.

#####Wire Swap
An easier solution which means all tutorials will be using the same numbers is just to unscrew the motor going the wrong way and plug the wires in the other way round. Both motors should go the same way now.

###Backwards, Left & Right
To add in the other directions in very simple, start by re-opening the python program by running ```nano robotC.c``` and repeat the forwards code 3 more times changing the forwards to backwards, left and right for each function.
Next we need to modify them to move the motors in other directions. 
We need the following outputs for each motor. This assumes Motor 1 will be on the left and Motor 2 on the right

*Backwards, m1b & m2b on. m1a & m2a off.
*Left, m1b & m2a on. m1a & m2b off.
*Right, m1a & m2b on. m1b & m2a off.
Your code should now have the following above the 'int main(void)'
```

void right()
{
  digitalWrite(m1a, LOW);
  digitalWrite(m1b, HIGH);
  digitalWrite(m2a, LOW);
  digitalWrite(m2b, HIGH);
}

void left()
{
  digitalWrite(m1a, HIGH);
  digitalWrite(m1b, LOW);
  digitalWrite(m2a, LOW);
  digitalWrite(m2b, HIGH);
}

Woo! We have now got the basis of our code completed for the next tutorials.

-Written by Zachary Igielman
