#!/usr/bin/env python
import subprocess
import optparse


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("mac address for " + interface + " is " + new_mac)


def get_arguments():
    argumentsParse = optparse.OptionParser()
    argumentsParse.add_option('-i', '--interface', dest='interface', help="the interface to change the mac address")
    argumentsParse.add_option('-m', '--mac', dest='macAddress', help="New MAC address")
    (options, arguments) = argumentsParse.parse_args()
    if not options.interface:
        argumentsParse.error("[-] please specify a interface,use --help for more info")
    if not options.macAddress:
        argumentsParse.error("[-] please specify a mac address, use --help for more info")
    return options


subprocess.call("ip link show", shell=True)
print('Select the interface from the above list. (Shows available interfaces)')

options = get_arguments()
change_mac(options.interface, options.macAddress)
