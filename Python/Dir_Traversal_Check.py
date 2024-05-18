#pip install python-requests
import requests

def check_directory_traversal(url, sensitive_file):
    try:
        target_url = f"{url}/{sensitive_file}/../"
        response = requests.get(target_url)
        if "Sensitive Information" in response.text:
            print(f"The URL is vulnerable to directory traversal: {target_url}")
        else:
            print(f"The URL is not vulnerable to directory traversal: {target_url}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_url = 'your_target_url'
    sensitive_file = 'your_sensitive_file'
    check_directory_traversal(target_url, sensitive_file)
