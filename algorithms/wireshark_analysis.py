# Wireshark (PyShark) packet capture analysis
import pyshark

capture = pyshark.FileCapture('capture.pcap')

# IP filtering
ip_filter = capture.set_display_filter('ip.src == 192.168.0.1')

# Iterate and print basic info
for pkt in capture:
    print(pkt)
