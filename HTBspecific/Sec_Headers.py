#pip install python-requests
import requests

def check_security_headers(url):
    try:
        # Send a GET request to the target URL
        response = requests.get(url)

        # Check for common security headers
        headers_to_check = ['Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']

        print(f"Security Headers for {url}:")

        for header in headers_to_check:
            if header in response.headers:
                print(f"{header}: {response.headers[header]}")
            else:
                print(f"{header}: Not present")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_target_url' with the actual URL of the website you want to check
    target_url = 'your_target_url'

    # Check the target website for common security headers
    check_security_headers(target_url)
