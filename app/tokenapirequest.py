import requests

def make_api_request(token):
    url = 'http://localhost:5000/api/dashboard'  # Adjust URL if necessary
    headers = {
        'Authorization': f'Bearer {token}',
    }
    
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

def main():
    token = input("Enter token to include in request: ")
    make_api_request(token)

if __name__ == "__main__":
    main()

