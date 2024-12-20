# breach_checker.py
import requests

def check_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"User-Agent": "Python OSINT", "hibp-api-key": "your_api_key"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return "No breaches found"

if __name__ == "__main__":
    email = input("Enter email: ")
    breaches = check_breach(email)
    print(breaches)
