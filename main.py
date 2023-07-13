# Module to launch and scan every flaw on a network

import time
import os

print("I pledged myself to your teachings, to the way of the Sith.\n")
print("Waiting to be plugged on a network...")

connectionStatus = ""

while(connectionStatus == ""):
    connectionStatus = os.system("ip a show eth0 | grep UP")                # checking if the interface has an IP
    time.sleep(1)

print("Connected.\n")

print("They shall feel the hatred of the Dark Side.\n")

print("Your IP Address is :")
ipAddress = os.system("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'")             # show its IP

print("gathering hosts...")             # scanning the network to get a list of all machines
os.system("sudo arp-scan --interface=eth0 --localnet --quiet --plain --format='${ip}' >> hostlist.txt")

hosts_Array = []
with open('hostlist.txt') as my_file:
    for line in my_file:
        hosts_Array.append(line)


print("scanning port of hosts...")



for x in hosts_Array:
    os.system("nmap {} >> scanresult.txt".format(x))

