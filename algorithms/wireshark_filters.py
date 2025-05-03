
# Demonstrates various PyShark filters and layer inspections

import pyshark

def load_capture(path, display_filter=None):
    cap = pyshark.FileCapture(path, display_filter=display_filter, only_summaries=False)
    for i, pkt in enumerate(cap):
        print(f"\n=== Packet {i+1} ===")
        print(pkt)
        # show layers present
        print("Layers:", [layer.layer_name for layer in pkt.layers])
        if i >= 4:  # limit output
            break

if __name__ == "__main__":
    pcap = "capture.pcap"
    print("1) Port filtering (TCP port 80):")
    load_capture(pcap, "tcp.port == 80")

    print("\n2) OSI-layer analysis (show Ethernet + IP):")
    load_capture(pcap, "eth or ip")

    print("\n3) TCP packet introspection:")
    load_capture(pcap, "tcp")

    print("\n4) HTTP payload analysis:")
    load_capture(pcap, "http")

    print("\n5) UDP traffic inspection:")
    load_capture(pcap, "udp")

    print("\n6) ARP packet parsing:")
    load_capture(pcap, "arp")

    print("\n7) ICMP filter analysis:")
    load_capture(pcap, "icmp")
