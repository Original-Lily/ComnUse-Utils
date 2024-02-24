#!/bin/bash

# Usage: ./scan.sh target_ip

target_ip=$1

# Perform a basic Nmap scan
nmap -sP $target_ip       # Ping scan
nmap -sV $target_ip       # Version detection
nmap -A $target_ip        # Aggressive scan
# Add more scans as needed

# Save Nmap output to a file
nmap -A -oN scan_results.txt $target_ip

# Parse Nmap output using Python
python parse_nmap.py
