import socket

def check_open_ports(target_host, start_port, end_port):
    open_ports = []

    try:
        # Iterate through the range of ports and attempt a connection
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                result = s.connect_ex((target_host, port))

                # If the connection attempt is successful, the port is open
                if result == 0:
                    open_ports.append(port)

    except socket.error as e:
        print(f"Error: {e}")

    # Print the list of open ports
    if open_ports:
        print(f"Open ports on {target_host}: {open_ports}")
    else:
        print(f"No open ports found on {target_host} in the specified range.")

if __name__ == "__main__":
    # Replace 'your_target_host', 'your_start_port', and 'your_end_port' with the actual target host and port range
    target_host = 'your_target_host'
    start_port = 1
    end_port = 1000

    # Check for open ports on the target host in the specified range
    check_open_ports(target_host, start_port, end_port)
