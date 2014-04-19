Setting up wireless on your Raspberry Pi
===========

To setup wireless you require to first connect your Raspberry Pi to a Monitor & Keyboard or if you have a Linux / Mac computer then you can edit the file directly with root privilages.

Once you have connected your Raspberry Pi to a monitor and keyboard boot up the Pi, login and then run the following command: 
``` sudo nano /etc/network/interfaces ``` The result should then look like the following. 
```
auto lo

iface lo inet loopback
iface eth0 inet dhcp


allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
```

You will need to edit it to add auto wlan0 above the allow-hotplug wlan0, your configuration should now look like this:
```
auto lo

iface lo inet loopback
iface eth0 inet dhcp

auto wlan0
allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
```
Then save the configuration by pressing Ctrl-x, y and then enter. This will save and overwrite the old configuration.

Next we want to configure a wireless network, start by typing ```sudo nano /etc/wpa_supplicant/wpa_supplicant.conf``` . The configuration file should look like the following:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
```

To add a Wi-Fi network in is very simple once you have the correct template, Find a template below and then copy it into the configuration file.



WPA_Supplicant Templates
===========

WPA2-PSK
--------
Replace SSID_HERE with your wireless network name and PASSKEY_HERE with your passphrase / wi-fi key.
```
network={
#wpa2
ssid="SSID_HERE"
psk="PASSKEY_HERE"

proto=RSN
key_mgmt=WPA-PSK

pairwise=CCMP TKIP
auth_alg=OPEN

scan_ssid=1
}
```

OPEN / No password
--------
Replace SSID_HERE with your wireless network name.
```
network={
#open
ssid="SSID_HERE"
key_mgmt=NONE
}

```
Note, Open Networks are unsecure, do not transmit any personal data such as passwords or online banking over them without extreme precautions.

WEP
--------
We currently do not have a WEP configuration due to it being unsecure, please contact us if you require it.


Multiple Networks
--------
It is quite simple to add multiple networks at one point, just repeat the same process under another network, here is an example of my network config without passkeys.
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
#wpa2
ssid="rtk"
psk="***"

proto=RSN
key_mgmt=WPA-PSK

pairwise=CCMP TKIP
auth_alg=OPEN

scan_ssid=1
}
network={
#wpa2
ssid="rtk-2"
psk="***"

proto=RSN
key_mgmt=WPA-PSK

pairwise=CCMP TKIP
auth_alg=OPEN

scan_ssid=1
}
network={
#open
ssid="NHC-WiFi"
key_mgmt=NONE
}

``` 

Finishing Configuration
--------
Once you have entered in your wi-fi network or networks save the file by repeating the same exit process of Ctrl-X, Y and then enter. Finally reboot your Raspberry Pi using sudo reboot. The Pi should reboot and the wireless adapter should show a blue light to indicate that it has booted up.

If you encounter any issues then you can contact us on support(AT)ryanteck.ltd.uk if you have ordered one of our robot kits or wi-fi adapters.
