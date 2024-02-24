#pip install python-requests
import requests

def check_directory_traversal(url, sensitive_file):
    try:
        # Craft the URL with a potential directory traversal payload
        target_url = f"{url}/{sensitive_file}/../"

        # Send a GET request to the crafted URL
        response = requests.get(target_url)

        # Check if the response indicates a successful directory traversal (e.g., look for specific content)
        if "Sensitive Information" in response.text:
            print(f"The URL is vulnerable to directory traversal: {target_url}")
        else:
            print(f"The URL is not vulnerable to directory traversal: {target_url}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_target_url' and 'your_sensitive_file' with the actual target URL and sensitive file
    target_url = 'your_target_url'
    sensitive_file = 'your_sensitive_file'

    # Check the target URL for directory traversal vulnerability
    check_directory_traversal(target_url, sensitive_file)
