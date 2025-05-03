# Ethical Hacking 

![Ethical Hacking](https://img.shields.io/badge/Ethical%20Hacking-Toolkit-blue)

A comprehensive collection of scripts and tools for performing network reconnaissance, packet analysis, encryption demonstrations, and basic honeypot setup. Designed for learning and lab assignments in ethical hacking and cybersecurity.

---

## Table of Contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Scripts and Tools](#scripts-and-tools)

  * [nmap\_scans.sh](#1-nmap_scanssh)
  * [hping3\_scans.sh](#2-hping3_scanssh)
  * [wireshark\_analysis.py](#3-wireshark_analysisscript)
  * [ddos\_trinoo\_simulation.py](#4-ddos_trinoo_simulationpy)
  * [honey\_pot.py](#5-honey_potpy)
  * [des.py](#6-desscript)
  * [rsa.py](#7-rsascript)
  * [aes.py](#8-aesscript)
  * [ip\_auth.py](#9-ip_authpy)
* [Usage Examples](#usage-examples)
* [Contributing](#contributing)
* [License](#license)

---

## Overview

This repository provides a curated set of scripts to help security enthusiasts and students:

* Perform various **Nmap** and **hping3** scans for network reconnaissance.
* Analyze packet captures using **PyShark** (Wireshark Python bindings).
* Simulate simple **DDoS** attacks (UDP flood) as in the Trinoo model.
* Deploy a minimal **honeypot** to catch unauthorized connection attempts.
* Demonstrate basic symmetric (**DES**, **AES**) and asymmetric (**RSA**) encryption workflows with PyCryptodome.
* Enforce simple **IP-based authentication** via a Flask microservice.

---

## Prerequisites

* **Bash** shell for scan scripts
* **Python 3.7+**
* **pip** package manager

Optional Python libraries (install via `requirements.txt` or manually):

```bash
pip install pyshark pycryptodome flask
```

---

## Installation

1. Clone the repository:

   ```bash
   ```

git clone [https://github.com/yxshee/ethicalhacking.git](https://github.com/yxshee/ethicalhacking.git)
cd ethicalhacking

````
2. Make shell scripts executable:
   ```bash
chmod +x *.sh
````

3. (Optional) Create and activate a Python virtual environment:

   ```bash
   ```

python3 -m venv venv
source venv/bin/activate

````
4. Install Python dependencies:
   ```bash
pip install -r requirements.txt
````

---

## Scripts and Tools

### 1. `nmap_scans.sh`

Batch Nmap scans for quick reconnaissance:

* **TCP Connect** (`-sT`)
* **SYN Ping** (`-sS`)
* **UDP** (`-sU`)
* **FIN** (`-sF`)
* **OS Detection** (`-O`)
* **Version Detection** (`-sV`)
* Subnet and range scans

### 2. `hping3_scans.sh`

Customized **hping3** scans and flooding:

* **SYN Flood Attack** (`--flood`)
* **FIN Flag Scan**
* Basic port scan variant

### 3. `wireshark_analysis.py`

Leverages **PyShark** to parse and filter `.pcap` files:

* Apply display filters (e.g., `ip.src == ...`)
* Iterate over packets and extract fields

### 4. `ddos_trinoo_simulation.py`

Simple UDP flood threads to simulate a Trinoo-like DDoS attack:

* Configurable target IP/port
* Multi-threaded packet sender

### 5. `honey_pot.py`

Minimal TCP honeypot listening on port 2222:

* Logs connection attempts
* Sends a warning banner and disconnects

### 6. `des.py`

Data Encryption Standard (DES) demo:

* ECB mode with padding/unpadding
* `encrypt()` and `decrypt()` functions

### 7. `rsa.py`

RSA public-key encryption example:

* Key generation (2048-bit)
* OAEP padding for secure encryption/decryption

### 8. `aes.py`

Advanced Encryption Standard (AES) demo in CBC mode:

* Random IV prepended to ciphertext
* Padding utilities for block alignment

### 9. `ip_auth.py`

Flask microservice enforcing IP-based access control:

* `@before_request` to whitelist IPs
* Sample endpoint returning a welcome message

---

## Usage Examples

Run an **Nmap** TCP scan:

```bash
./nmap_scans.sh 10.0.0.5
```

Launch the honeypot:

```bash
python honey_pot.py
```

Encrypt data with AES:

```python
from aes import encrypt, decrypt
ct = encrypt("TopSecret")
print(decrypt(ct))
```

---

## Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
