import ssl
import socket
from datetime import datetime

def check_ssl_certificate(hostname, port=443):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

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
    target_hostname = 'your_hostname'
    target_port = 443
    check_ssl_certificate(target_hostname, target_port)
