# anonymizer_detection.py

import requests

def detect_anonymizer(ip_address):
    try:
        api_url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            hostname = data.get("hostname")
            org = data.get("org")
            
            if hostname or org:
                return True, hostname, org
            else:
                return False, None, None
        else:
            return False, None, None
    except requests.exceptions.RequestException:
        return False, None, None

if __name__ == "__main__":
    ip_address = input("Enter the IP address to detect anonymizer usage: ")
    is_anonymizer, hostname, org = detect_anonymizer(ip_address)
    
    if is_anonymizer:
        print("Anonymizer usage detected:")
        if hostname:
            print(f"Hostname: {hostname}")
        if org:
            print(f"Organization: {org}")
    else:
        print("No anonymizer usage detected.")
