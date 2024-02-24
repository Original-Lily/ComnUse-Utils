#pip install python-nmap
import nmap

def perform_port_scan(target_ip, ports='1-1000'):
    # Create Nmap scanner object
    nm = nmap.PortScanner()

    # Perform a TCP SYN scan on the specified ports
    nm.scan(target_ip, ports, arguments='-sS')

    # Print scan results
    for host in nm.all_hosts():
        print(f"Results for {host}:")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                print(f"Port {port}: {state}")

if __name__ == "__main__":
    # Replace 'your_target_ip' with the actual target IP address
    target_ip = 'your_target_ip'
    
    # Perform a port scan on the target IP
    perform_port_scan(target_ip)
