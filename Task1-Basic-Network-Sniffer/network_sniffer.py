from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer (IP):
        print("\nPacket Captured")
        print("Source IP:",
packet [IP].src)
        print("Destination IP:",
packet [IP].dst)
        print("Protocol:",
packet [IP].proto)
        print("-" * 50)

print("Starting Network Sniffer...")
sniff(prn=packet_callback, store=False)