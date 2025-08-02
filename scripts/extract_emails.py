#!/usr/bin/env python3
import sys
import re
import requests

if len(sys.argv) < 2:
    print("Usage: python3 email_extract.py <domain>")
    sys.exit(1)

domain = sys.argv[1]

try:
    # First try HTTP
    url = f"http://{domain}"
    response = requests.get(url, timeout=5)
    
    # If redirect or failed, optionally try HTTPS (uncomment next lines if you like)
    # if response.status_code != 200:
    #     url = f"https://{domain}"
    #     response = requests.get(url, timeout=5)
    
    html = response.text

    # Better email regex (avoids trailing < or > etc.)
    emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html))

    if emails:
        print("Emails:", ', '.join(sorted(emails)), flush=True)
    else:
        print("Emails: None found", flush=True)

except requests.exceptions.RequestException as e:
    print(f"Error fetching {url}: {e}", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)
