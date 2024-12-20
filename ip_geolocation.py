# ip_geolocation.py
import requests

def get_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    location = get_geolocation(ip)
    print(location)
