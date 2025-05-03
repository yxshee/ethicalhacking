#!/bin/bash
# Nmap scan scripts for Assignment

TARGET=$1

echo "TCP Connect Scan"
nmap -sT -F $TARGET

echo "SYN Scan"
nmap -sS -F $TARGET

echo "UDP Scan"
nmap -sU -F $TARGET

echo "FIN Scan"
nmap -sF -F $TARGET

echo "OS Detection"
nmap -O -F $TARGET

echo "Version Detection"
nmap -sV -F $TARGET

echo "Subnet Scan (Class C)"
nmap 192.168.10.0/24

echo "IP Range Scan"
nmap 10.1.1.5-100
