import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
import subprocess
import threading
import socket

try:
    from Crypto.Cipher import DES, AES, PKCS1_OAEP
    from Crypto.PublicKey import RSA
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    try:
        from Cryptodome.Cipher import DES, AES, PKCS1_OAEP
        from Cryptodome.PublicKey import RSA
        from Cryptodome.Util.Padding import pad, unpad
    except ImportError:
        raise ImportError(
            "Missing Crypto library. "
            "Install dependencies via:\n  pip install -r requirements.txt"
        )

import pyshark
import requests

# --- Encryption Setup ---
des_key = b'8bytekey'
des_cipher = DES.new(des_key, DES.MODE_ECB)

aes_key = b'16byteaeskey1234'

rsa_key = RSA.generate(2048)
private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()
rsa_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

# --- GUI Application ---
class EthicalHackingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ethical Hacking Toolkit")
        self.geometry("800x600")
        self.create_tabs()

    def create_tabs(self):
        tab_control = ttk.Notebook(self)
        tabs = {
            "Nmap Scans": self.nmap_tab,
            "hping3 Scans": self.hping_tab,
            "Packet Analysis": self.pcap_tab,
            "DDoS Simulation": self.ddos_tab,
            "Honeypot": self.honeypot_tab,
            "DES Demo": self.des_tab,
            "RSA Demo": self.rsa_tab,
            "AES Demo": self.aes_tab,
            "IP Auth Test": self.ipauth_tab,
        }
        for name, func in tabs.items():
            frame = ttk.Frame(tab_control)
            func(frame)
            tab_control.add(frame, text=name)
        tab_control.pack(expand=1, fill="both")

    def _run_command(self, cmd, output_widget):
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output = e.output
        output_widget.delete(1.0, tk.END)
        output_widget.insert(tk.END, output)

    def nmap_tab(self, frame):
        ttk.Label(frame, text="Target IP/Host:").pack(pady=5)
        target_entry = ttk.Entry(frame)
        target_entry.pack()
        output = scrolledtext.ScrolledText(frame, height=15)
        output.pack(expand=1, fill="both")
        ttk.Button(frame, text="Run Quick Scan", command=lambda: threading.Thread(target=self._run_command, args=(f"nmap -F {target_entry.get()}", output)).start()).pack(pady=5)

    def hping_tab(self, frame):
        ttk.Label(frame, text="Target IP/Host:").pack(pady=5)
        target_entry = ttk.Entry(frame)
        target_entry.pack()
        output = scrolledtext.ScrolledText(frame, height=15)
        output.pack(expand=1, fill="both")
        ttk.Button(frame, text="Run SYN Scan", command=lambda: threading.Thread(target=self._run_command, args=(f"hping3 -S {target_entry.get()} -p 80 -c 10", output)).start()).pack(pady=5)

    def pcap_tab(self, frame):
        ttk.Label(frame, text="PCAP File Path:").pack(pady=5)
        path_entry = ttk.Entry(frame)
        path_entry.pack()
        output = scrolledtext.ScrolledText(frame, height=15)
        output.pack(expand=1, fill="both")
        def analyze():
            try:
                cap = pyshark.FileCapture(path_entry.get(), only_summaries=True)
                output.delete(1.0, tk.END)
                for pkt in cap[:10]:
                    output.insert(tk.END, str(pkt) + "\n")
            except Exception as e:
                output.insert(tk.END, f"Error: {e}")
        ttk.Button(frame, text="Analyze Packets", command=analyze).pack(pady=5)

    def ddos_tab(self, frame):
        ttk.Label(frame, text="Target IP/Port:").pack(pady=5)
        ip_entry = ttk.Entry(frame); ip_entry.pack(side="left", padx=5)
        port_entry = ttk.Entry(frame); port_entry.pack(side="left")
        ttk.Button(frame, text="Start UDP Flood", command=lambda: threading.Thread(target=self.udp_flood, args=(ip_entry.get(), int(port_entry.get()))).start()).pack(pady=5)

    def udp_flood(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = b'A' * 1024
        while True:
            sock.sendto(data, (ip, port))

    def honeypot_tab(self, frame):
        ttk.Button(frame, text="Start Honeypot", command=lambda: threading.Thread(target=self.start_honeypot).start()).pack(pady=20)

    def start_honeypot(self):
        HOST, PORT = "0.0.0.0", 2222
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            messagebox.showinfo("Honeypot", f"Listening on {HOST}:{PORT}")
            while True:
                conn, addr = s.accept()
                print(f"Connection from {addr}")
                conn.send(b"Unauthorized access detected. Disconnecting.")
                conn.close()

    def des_tab(self, frame):
        ttk.Button(frame, text="Encrypt Text", command=lambda: self.encrypt_des()).pack(pady=5)
        ttk.Button(frame, text="Decrypt Text", command=lambda: self.decrypt_des()).pack(pady=5)

    def rsa_tab(self, frame):
        ttk.Button(frame, text="Encrypt Text", command=lambda: self.encrypt_rsa()).pack(pady=5)
        ttk.Button(frame, text="Decrypt Text", command=lambda: self.decrypt_rsa()).pack(pady=5)

    def aes_tab(self, frame):
        ttk.Button(frame, text="Encrypt Text", command=lambda: self.encrypt_aes()).pack(pady=5)
        ttk.Button(frame, text="Decrypt Text", command=lambda: self.decrypt_aes()).pack(pady=5)

    def ipauth_tab(self, frame):
        ttk.Label(frame, text="Service URL:").pack(pady=5)
        url_entry = ttk.Entry(frame); url_entry.pack()
        ttk.Button(frame, text="Test Access", command=lambda: self.test_ip_auth(url_entry.get())).pack(pady=5)

    # --- Encryption Functions ---
    def encrypt_des(self):
        text = simpledialog.askstring("Input", "Enter text to encrypt:")
        ct = des_cipher.encrypt(pad(text.encode(), DES.block_size))
        messagebox.showinfo("Encrypted", ct.hex())

    def decrypt_des(self):
        hex_ct = simpledialog.askstring("Input", "Enter ciphertext (hex):")
        pt = unpad(des_cipher.decrypt(bytes.fromhex(hex_ct)), DES.block_size)
        messagebox.showinfo("Decrypted", pt.decode())

    def encrypt_rsa(self):
        text = simpledialog.askstring("Input", "Enter text to encrypt:")
        ct = rsa_cipher.encrypt(text.encode())
        messagebox.showinfo("Encrypted", ct.hex())

    def decrypt_rsa(self):
        hex_ct = simpledialog.askstring("Input", "Enter ciphertext (hex):")
        cipher_dec = PKCS1_OAEP.new(RSA.import_key(private_key))
        pt = cipher_dec.decrypt(bytes.fromhex(hex_ct))
        messagebox.showinfo("Decrypted", pt.decode())

    def encrypt_aes(self):
        text = simpledialog.askstring("Input", "Enter text to encrypt:")
        cipher = AES.new(aes_key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
        messagebox.showinfo("Encrypted", (cipher.iv + ct_bytes).hex())

    def decrypt_aes(self):
        hex_ct = simpledialog.askstring("Input", "Enter ciphertext (hex):")
        enc = bytes.fromhex(hex_ct)
        iv, ct = enc[:AES.block_size], enc[AES.block_size:]
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        messagebox.showinfo("Decrypted", pt.decode())

    def test_ip_auth(self, url):
        try:
            resp = requests.get(url)
            messagebox.showinfo("Response", f"Status Code: {resp.status_code}\nBody: {resp.text}")
        except Exception as e:
            messagebox.showerror("Error", e)

if __name__ == "__main__":
    app = EthicalHackingApp()
    app.mainloop()
