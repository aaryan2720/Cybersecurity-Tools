import requests
from  bs4 import BeautifulSoup

bad_char = ["'", "\"", ";", "--", "#", "/*", "*/", "union", "select", "insert", "update", "delete", "drop", "alter", "create", "truncate", "1=1", "'1'='1'", "OR 1=1"]

def spider_inputs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find('form')
    if not form:
        print("No form found")
        return []
    return form.find_all('input')

def test_inputs(url, inputs):
    results = {}
    if not inputs:
        print("No input fields to test.")
        return results

    for input_fields in inputs:
        name = input_fields.get('name')
        if name:
            for char in bad_char:
                payload = {name: char}
                response = requests.post(url, data=payload)
                key = f"{url} input field: {name} payload: {char}"
                results[key] = response.status_code
    return results


def main():
    url = input("Enter a URL to scan ")

    inputs = spider_inputs(url)
    if not inputs:
        return
    
    results = test_inputs(url, inputs)
    for key, value in results.items():
        print(f"{key} and status code {value}") 

if __name__ == "__main__":
    main()

