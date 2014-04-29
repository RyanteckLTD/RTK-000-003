//RTK-000-001 Simple SSH Python controller
//Licensed under the GNU GPL V3 License
//(C) Ryanteck LTD. 2014
//Written by Zachary Igielman

//inmport the module to control GPIOs
#include <wiringPi.h>

int main(void)
{
    //set the apropriate pins as outputs using wiringpi numbering
    wiringPiSetup();
    pinMode(0,OUTPUT); //BCM:17
    pinMode(1,OUTPUT); //BCM:18
    pinMode(3,OUTPUT); //BCM:22
    pinMode(4,OUTPUT); //BCM:23
    
    //Now lets make the robot spin for 1 second left
    digitalWrite(0, HIGH);
    digitalWrite(4, HIGH);
    delay(1000);
    digitalWrite(0, LOW);
    digitalWrite(4, LOW);
    
    //Now lets make the robot spin for 1 second right
    digitalWrite(1, HIGH);
    digitalWrite(3, HIGH);
    delay(1000);
    digitalWrite(1, LOW);
    digitalWrite(3, LOW);
    
    return 0;
}