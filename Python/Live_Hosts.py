#pip install scapy
from scapy.all import *

def scan_for_live_hosts(target_network, timeout=2):
    ip_range = [f"{target_network}.{i}" for i in range(1, 255)]

    live_hosts = []

    for ip in ip_range:
        icmp_request = IP(dst=ip)/ICMP()
        reply = sr1(icmp_request, timeout=timeout, verbose=False)

        if reply and reply.haslayer(ICMP) and reply[ICMP].type == 0:
            live_hosts.append(ip)
            print(f"Host {ip} is live.")

    if not live_hosts:
        print("No live hosts found on the network.")

if __name__ == "__main__":
    target_network = 'your_target_network'
    timeout_seconds = 2
    scan_for_live_hosts(target_network, timeout=timeout_seconds)
