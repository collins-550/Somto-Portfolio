# Cisco SOHO Network — Packet Tracer Lab
 
## Overview
A fully configured Small Office/Home Office (SOHO) network built in
Cisco Packet Tracer. Demonstrates practical networking skills including
router configuration, DHCP, DNS, NAT, WiFi security, SSH, and web
server setup.
 
## Tools & Technologies
- Cisco Packet Tracer
- Cisco IOS CLI
 
## Network Topology
```
[Internet Cloud]
       |
   [Router] — NAT/PAT configured
       |
   [Switch]
    /  |  \
[PC1][PC2][Access Point]
              |
          [WiFi Devices]
              |
         [Web Server]
```
 
## Configurations Implemented
 
### Router
- WAN interface with static IP
- LAN interface (192.168.1.1/24)
- NAT/PAT for internet access
- SSH remote access (version 2)
- Static routing
 
### DHCP
- DHCP pool: 192.168.1.100 - 192.168.1.200
- Default gateway: 192.168.1.1
- DNS server: 8.8.8.8
 
### WiFi (Access Point)
- SSID: SOHONetwork
- Security: WPA2-PSK
- Encryption: AES
 
### DNS
- Local DNS resolution configured
- Domain: sohobusiness.local
 
### Web Server
- HTTP server running on 192.168.1.50
- Custom homepage configured
 
## Skills Demonstrated
- Router CLI configuration (Cisco IOS)
- DHCP server setup
- NAT/PAT configuration
- WiFi security (WPA2)
- SSH hardening
- DNS configuration
- Network troubleshooting
- Subnetting (192.168.1.0/24)
 
## Files
- `SOHO_Network.pkt` — Cisco Packet Tracer file (open with Packet Tracer)
 
## Author
Somto Collins | Cybersecurity Student | NOUN | Early Code Institute, Abuja
