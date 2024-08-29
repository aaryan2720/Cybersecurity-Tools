from scapy.all import sniff, Ether

interface = "Wi-Fi"

def packet_handler(packet):
    if Ether in packet:
        print(packet[Ether].summary())

try:
    sniff(iface=interface, prn=packet_handler, store=0)
except KeyboardInterrupt:
    pass
