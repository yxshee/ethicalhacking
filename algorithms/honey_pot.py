# Simple Honeypot Implementation
import socket

HOST = '0.0.0.0'
PORT = 2222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Honeypot listening on {HOST}:{PORT}')
    while True:
        conn, addr = s.accept()
        print(f'Connection attempt from {addr}')
        conn.send(b'Unauthorized access detected. Disconnecting.')
        conn.close()
