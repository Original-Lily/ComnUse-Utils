import requests

def search_github_repos(query):
    url = f"https://api.github.com/search/code?q={query}"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)

        data = response.json()
        items = data.get('items', [])

        for item in items:
            repository = item['repository']['full_name']
            file_name = item['name']
            html_url = item['html_url']
            print(f"Repository: {repository}, File: {file_name}, URL: {html_url}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    query = "INSERT SEARCH TEXT HERE"
    search_github_repos(query)
