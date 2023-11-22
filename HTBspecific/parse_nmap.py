#!/usr/bin/env python

import re

def parse_nmap_output(output):
    # Implement your parsing logic here
    # Example: Extract open ports
    open_ports = re.findall(r"\d+/tcp\s+open", output)
    
    return open_ports

if __name__ == "__main__":
    with open("scan_results.txt", "r") as file:
        nmap_output = file.read()

    open_ports = parse_nmap_output(nmap_output)
    print("Open Ports:", open_ports)
