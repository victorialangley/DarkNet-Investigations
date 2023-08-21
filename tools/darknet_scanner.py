# darknet_scanner.py

import requests
import json

def scan_darknet_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            keywords = ["illegal", "contraband", "anonymity", "hidden services"]
            matches = [keyword for keyword in keywords if keyword in content]
            if matches:
                return True, matches
            else:
                return False, []
        else:
            return False, []
    except requests.exceptions.RequestException:
        return False, []

if __name__ == "__main__":
    site_url = input("Enter the URL of the site to scan: ")
    is_darknet, keywords = scan_darknet_site(site_url)
    
    if is_darknet:
        print("This site exhibits characteristics of a darknet site.")
        print("Detected keywords:", ", ".join(keywords))
    else:
        print("This site does not appear to be a darknet site.")
