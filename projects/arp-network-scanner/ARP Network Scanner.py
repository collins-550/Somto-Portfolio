from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    arp_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    answered, _ = srp(arp_broadcast, timeout=2, verbose=False)
    
    print(f"\n{'IP Address':<20} {'MAC Address'}")
    print("-" * 45)
    
    for sent, received in answered:
        print(f"{received.psrc:<20} {received.hwsrc}")
    
    print("-" * 45)
    print(f"{len(answered)} device(s) found.\n")

scan_network("192.168.87.0/24")