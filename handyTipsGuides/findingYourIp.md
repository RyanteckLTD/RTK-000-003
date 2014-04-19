How to find your Raspberry Pi's IP Address
===========
We found the easiest way to find an IP address of your Raspberry Pi is using a handy tool called Fing.

Windows
-------
Coming soon...

Ubuntu 
-----
Tested on Ubuntu 14.04 and 13.10
First download Fing from Overlook's website, for ubuntu and other debian based operating systems select the DEB and the architecture you are using (This is likely 64-bit on a modern computer).

After it has downloaded click on the icon and then the Ubuntu Software Centre should Load, then click the install button and then fing should be installed.
Then open up a terminal window and then run the command ```sudo fing``` and fing will run and display a list of all the IP addresses. and their devices. You are looking for the IP address of the device that shows up as Shenzhen Ogemray Technology.

<img src="imageResources/fingUbuntu.png"/>


Linux (DEB) Command Line 
-----
Tested on Ubuntu 14.04 and 13.10, should be compatible with Debian as well.
First download Fing by running the following command, change the lx64 to lx32 if you are running a 32 bit version of Linux.
```wget "http://www.overlooksoft.com/packages/download?plat=lx64&ext=deb" -O fing.deb```
next you can install it by typing ``` sudo dpkg -i fing.deb ```

It should now be installed.

Next run the command ```sudo fing``` and fing will run and display a list of all the IP addresses. and their devices. You are looking for the IP address of the device that shows up as Shenzhen Ogemray Technology.
A picture of the output can be found above in the ubuntu section.

Linux (RPM)
-----
Coming soonn..

Android
-------
First you will have to install an application called Fing onto your Android device, to do this you can either look in the app store for "Fing" or click the following link and click the install button. https://play.google.com/store/apps/details?id=com.overlook.android.fing

After the application has installed it is as simple as launching it and then clicking the refresh icon in the top right of the application. You should see all of the devices on the network appear.

<img src="imageResources/fingAndroid.png"/>

A Raspberry Pi connected via the ethernet cable will show as Raspberry Pi Foundation, the Wi-Fi adapters we provide identify as Shenzhen Ogemray Technology which is the IP address we want.
Make a note of this IP address and you are done!, You can also assign icons to each device by pressing down the button and clicking change icon. At the bottom there is one for Raspberry Pi.



Mac
---
We can't actually do this one as I have no mac equipment, if somebody can for me then it would be appreciated.


iOS
---
We can't actually do this one as I have no apples, if somebody can for me then it would be appreciated.
