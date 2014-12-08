#!/bin/bash
echo "Now installing VNC"
sudo apt-get install tightvncserver -y
echo "Please now type in the password you will install VNC with"
tightvncserver
echo "VNC Server is setup, now configuring auto boot"
cd /tmp/
wget http://goo.gl/FlrtAW --no-check-certificate --trust-server-names
echo "Downloaded config file"
sudo mv tightvncserver-init.txt /etc/init.d/tightvncserver
sudo chown root:root /etc/init.d/tightvncserver
sudo chmod 755 /etc/init.d/tightvncserver
sudo update-rc.d tightvncserver defaults
echo "All installed, please now type 'sudo reboot' to reboot your Raspberry Pi"
