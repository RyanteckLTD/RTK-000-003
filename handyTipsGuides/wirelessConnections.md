Template wireless configurations
===========
Here are a collection of templates for different Wi-Fi connections.

```
network={
ssid=""
psk=""

# Protocol type can be: RSN (for WP2) and WPA (for WPA1)
proto=RSN

# Key management type can be: WPA-PSK or WPA-EAP (Pre-Shared or Enterprise)
key_mgmt=WPA-PSK

# Pairwise can be CCMP or TKIP (for WPA2 or WPA1)
pairwise=CCMP TKIP

#Authorization option should be OPEN for both WPA1/WPA2 (in less commonly used are SHARED and LEAP)
auth_alg=OPEN

scan_ssid=1

}
```
