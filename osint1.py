# dns_lookup.py
import dns.resolver

def get_dns_records(domain):
    records = {}
    for record_type in ['A', 'MX', 'NS', 'TXT', 'CNAME']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [answer.to_text() for answer in answers]
        except:
            records[record_type] = []
    return records

if __name__ == "__main__":
    domain = input("Enter domain: ")
    dns_records = get_dns_records(domain)
    print(dns_records)
