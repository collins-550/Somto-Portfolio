# ARP Network Scanner
 
## Overview
A Python network scanner built using the Scapy library that discovers
all active devices on a local network using ARP (Address Resolution Protocol)
requests. Returns IP addresses and MAC addresses of all responding devices.
 
## Tools & Technologies
- Python 3
- Scapy library
- Kali Linux
 
## How It Works
1. Creates an ARP broadcast request targeting the entire subnet
2. Sends the packet to all devices on the network
3. Listens for ARP replies
4. Displays IP and MAC addresses of all responding devices
 
## How to Run
```bash
# Install scapy first
pip install scapy
 
# Run with root privileges (required for raw packet crafting)
sudo python arp_scanner.py
```
 
## Sample Output
```
IP Address           MAC Address
---------------------------------------------
192.168.1.1          00:50:56:c0:00:08
192.168.1.2          00:50:56:e6:4a:1b
192.168.1.128        00:0c:29:e5:6f:cf
---------------------------------------------
3 device(s) found.
```
 
## Skills Demonstrated
- Python scripting
- Network reconnaissance
- ARP protocol understanding
- Packet crafting with Scapy
- Linux/Kali environment
 
## Real-World Application
This is the same technique used by network administrators and
security analysts to discover unauthorized devices on a network,
and by tools like Nmap under the hood.
 
## Author
Somto Collins | Cybersecurity Student | NOUN | Early Code Institute, Abuja
 
