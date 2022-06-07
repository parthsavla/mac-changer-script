#!/usr/bin/env python

import subprocess
import optparse


argumentsParse = optparse.OptionParser()
argumentsParse.add_option('-i','--interface',dest='interface',help="the interface to change the mac address")
argumentsParse.add_option('-m','--mac',dest='macAddress',help="New MAC address")
(options,arguments) = argumentsParse.parse_args()

subprocess.call("ip link show",shell=True)
print('Select the interface from the above list. (Shows available interfaces)')
interface = options.interface
new_mac = options.macAddress



subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
