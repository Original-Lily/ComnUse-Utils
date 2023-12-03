#pip install scapy
from scapy.all import *

def scan_for_live_hosts(target_network, timeout=2):
    # Generate a range of IP addresses based on the target network
    ip_range = [f"{target_network}.{i}" for i in range(1, 255)]

    live_hosts = []

    for ip in ip_range:
        # Craft an ICMP (ping) request packet
        icmp_request = IP(dst=ip)/ICMP()

        # Send the packet and wait for a response
        reply = sr1(icmp_request, timeout=timeout, verbose=False)

        # Check if a response was received
        if reply and reply.haslayer(ICMP) and reply[ICMP].type == 0:
            live_hosts.append(ip)
            print(f"Host {ip} is live.")

    if not live_hosts:
        print("No live hosts found on the network.")

if __name__ == "__main__":
    # Replace 'your_target_network' with the actual target network (e.g., '192.168.1')
    target_network = 'your_target_network'

    # Optionally adjust the timeout (in seconds)
    timeout_seconds = 2

    # Scan the target network for live hosts
    scan_for_live_hosts(target_network, timeout=timeout_seconds)
