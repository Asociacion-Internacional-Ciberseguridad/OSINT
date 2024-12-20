# whois_lookup.py
import whois

def whois_lookup(domain):
    return whois.whois(domain)

if __name__ == "__main__":
    domain = input("Enter domain: ")
    data = whois_lookup(domain)
    print(data)
