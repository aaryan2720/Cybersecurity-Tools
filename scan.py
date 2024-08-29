import requests

target_url = input("Enter the target URL: ")

def scan_url(url):
    try:
        response = requests.get(url)
        headers = response.headers
        if 'X-XSS-Protection' in headers:
            print(f"X-XSS-Protection header is present: {headers['X-XSS-Protection']}")
        else:
            print("X-XSS-Protection header is missing.")
        if 'Strict-Transport-Security' in headers:
            print(f"Strict-Transport-Security header is present: {headers['Strict-Transport-Security']}")
        else:
            print("Strict-Transport-Security header is missing.")
        if 'Content-Security-Policy' in headers:
            print(f"Content-Security-Policy header is present: {headers['Content-Security-Policy']}")
        else:
            print("Content-Security-Policy header is missing.")
    except requests.exceptions.MissingSchema:
        print("Invalid URL format. Please include 'http://' or 'https://' in the URL.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

scan_url(target_url)
