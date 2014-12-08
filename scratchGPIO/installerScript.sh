#!/bin/bash
echo "Scratch & VNC Setup for RTK-000-003"
echo "This script will install Scratch GPIO and then a VNC Server"
echo "This installer requires some inpit and should only last around 5 minutes"
sleep 1
echo "Now downloading Scratch GPIO"
cd /tmp/
wget http://goo.gl/Pthh62 -O isgh5.sh
echo "Scratch GPIO downloaded, now installing"
sudo bash isgh5.sh
echo "Scratch GPIO installer has completed. 
echo "\n"
sleep 1
echo "Now installing VNC"
sudo apt-get install tightvncserver -y
echo "Now configuring VNC"
echo "Please now type in the password you will connect to VNC with"
tightvncserver
echo "VNC Server is setup, now configuring auto boot"
sleep 1
wget http://goo.gl/FlrtAW --no-check-certificate --trust-server-names
echo "Downloaded config file"
sleep 1
sudo mv tightvncserver-init.txt /etc/init.d/tightvncserver
sudo chown root:root /etc/init.d/tightvncserver
sudo chmod 755 /etc/init.d/tightvncserver
sudo update-rc.d tightvncserver defaults
echo "All installed, please now type 'sudo reboot' to reboot your Raspberry Pi"
