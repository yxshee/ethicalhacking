# 🛡️ Ethical Hacking Toolkit

![Ethical Hacking](https://img.shields.io/badge/Ethical%20Hacking-Toolkit-blue?style=for-the-badge&logo=hackaday)

A hands-on collection of scripts and tools for learning and demonstrating core concepts in **ethical hacking**, **network security**, and **cryptography**.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Scripts & Tools](#scripts--tools)
- [Contributing](#contributing)
- [License](#license)

---

## 📝 Overview

This repository provides a practical toolkit for:

- **Network reconnaissance** (Nmap, hping3)
- **Packet analysis** (Wireshark/PyShark)
- **DDoS simulation** (Trinoo-like UDP flood)
- **Honeypot deployment** (simple TCP trap)
- **Encryption demos** (DES, AES, RSA)
- **IP-based authentication** (Flask microservice)

Ideal for students, security enthusiasts, and anyone interested in cybersecurity labs or assignments.

---

## ✨ Features

- **Ready-to-run scripts** for scanning, analysis, and simulation
- **Encryption demos** using modern Python libraries
- **Minimal dependencies** and easy setup
- **Clear code** for educational purposes
- **Modular structure** for quick navigation

---

## 📁 Project Structure

```
ethicalhacking/
│
├── algorithms/
│   ├── aes.py              # AES encryption demo
│   ├── des.py              # DES encryption demo
│   ├── ddos_trinoo_simulation.py # DDoS UDP flood simulation
│   ├── honey_pot.py        # Simple TCP honeypot
│   ├── hping3_scans.sh     # hping3 scan/flood scripts
│   ├── ip_auth.py          # Flask IP-based authentication
│   ├── nmap_scans.sh       # Nmap scan scripts
│   ├── rsa.py              # RSA encryption demo
│   └── wireshark_analysis.py # PyShark packet analysis
│
└── README.md               # Project documentation
```

---

## ⚙️ Prerequisites

- **Python 3.7+**
- **pip** (Python package manager)
- **Bash** (for shell scripts)
- **nmap** and **hping3** installed on your system

**Python dependencies:**
```bash
pip install pyshark pycryptodome flask
```

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ethicalhacking.git
   cd ethicalhacking
   ```

2. **Make shell scripts executable:**
   ```bash
   chmod +x algorithms/*.sh
   ```

3. **(Optional) Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Python dependencies:**
   ```bash
   pip install pyshark pycryptodome flask
   ```

---

## 🧑‍💻 Usage Examples

- **Run an Nmap scan:**
  ```bash
  ./algorithms/nmap_scans.sh 192.168.1.1
  ```

- **Launch the honeypot:**
  ```bash
  python algorithms/honey_pot.py
  ```

- **Encrypt and decrypt with AES:**
  ```python
  from algorithms.aes import encrypt, decrypt
  ct = encrypt("TopSecret")
  print(decrypt(ct))
  ```

- **Start the IP-auth Flask app:**
  ```bash
  python algorithms/ip_auth.py
  ```

---

## 🛠️ Scripts & Tools

| Script/Tool                  | Description                                      |
|------------------------------|--------------------------------------------------|
| `nmap_scans.sh`              | Batch Nmap scans (TCP, SYN, UDP, OS, etc.)       |
| `hping3_scans.sh`            | SYN flood, FIN scan, and SYN scan with hping3    |
| `wireshark_analysis.py`      | Analyze `.pcap` files with PyShark               |
| `ddos_trinoo_simulation.py`  | Simulate UDP flood (Trinoo-style DDoS)           |
| `honey_pot.py`               | Simple TCP honeypot on port 2222                 |
| `des.py`                     | DES encryption/decryption demo                   |
| `aes.py`                     | AES encryption/decryption demo                   |
| `rsa.py`                     | RSA keygen, encrypt, decrypt demo                |
| `ip_auth.py`                 | Flask app with IP whitelist authentication       |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---
