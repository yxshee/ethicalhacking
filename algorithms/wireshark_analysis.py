import pyshark

def main():
    capture = pyshark.FileCapture('capture.pcap', display_filter='ip.src == 192.168.0.1')
    try:
        for pkt in capture:
            print(pkt)
    except KeyboardInterrupt:
        pass
    finally:
        capture.close()

if __name__ == '__main__':
    main()
