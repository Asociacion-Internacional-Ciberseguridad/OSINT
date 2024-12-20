# subdomain_scanner.py
import requests

def find_subdomains(domain):
    subdomains = ["intranet","www", "mail", "ftp", "test", "dev"]
    found = []
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                found.append(url)
        except:
            pass
    return found

if __name__ == "__main__":
    domain = input("Enter domain: ")
    subdomains = find_subdomains(domain)
    print("Found subdomains:", subdomains)
