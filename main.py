#!/usr/bin/env python

import subprocess
subprocess.call("ip link show",shell=True)
print('Select the interface from the above list. (Shows available interfaces)')
interface = input("Select the interface > ")
new_mac = input("the new mac address > ")

print("Changing make address for interface " + interface + " to " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)