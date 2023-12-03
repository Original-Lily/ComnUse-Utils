import ssl
import socket
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    try:
        # Create an SSL context
        context = ssl.create_default_context()

        # Establish a connection to the server
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the SSL/TLS certificate
                cert = ssock.getpeercert()

                # Extract relevant certificate information
                subject = dict(x[0] for x in cert['subject'])
                issuer = dict(x[0] for x in cert['issuer'])
                expiration_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')

                # Print certificate information
                print(f"SSL/TLS Certificate Information for {hostname}:{port}")
                print(f"Subject: {subject}")
                print(f"Issuer: {issuer}")
                print(f"Valid Until: {expiration_date}")

    except (socket.error, ssl.SSLError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_hostname' with the actual hostname you want to check
    target_hostname = 'your_hostname'

    # Specify an optional port (default is 443 for HTTPS)
    target_port = 443

    # Check the SSL/TLS certificate for the target hostname
    check_ssl_certificate(target_hostname, target_port)
