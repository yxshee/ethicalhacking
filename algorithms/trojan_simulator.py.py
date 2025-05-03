
# Educational file-replicator “trojan” that copies itself into a target directory

import os
import shutil
import time

MALICIOUS_COPY = "trojan_copy.py"

def replicate(target_dir):
    src = os.path.realpath(__file__)
    dst = os.path.join(target_dir, MALICIOUS_COPY)
    shutil.copy2(src, dst)
    print(f"[+] Replicated to {dst}")

if __name__ == "__main__":
    # directories to “infect” (for demo, subfolders in cwd)
    victims = [d for d in os.listdir('.') if os.path.isdir(d)]
    print("Simulating trojan propagation...")
    for victim in victims:
        try:
            replicate(victim)
        except Exception as e:
            print(f"[-] Could not replicate into {victim}: {e}")
    print("Done. (Educational only!)")
    time.sleep(1)
