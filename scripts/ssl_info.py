#!/usr/bin/env python3
import sys
import re
import requests

if len(sys.argv) < 2:
    print("Usage: python3 email_extract.py <domain>", flush=True)
    sys.exit(1)

domain = sys.argv[1]
url = f"http://{domain}"

print(f"🔍 Fetching homepage for {domain}...", flush=True)

try:
    response = requests.get(url, timeout=5)
    html = response.text

    print(f"✅ Fetched, extracting emails...", flush=True)

    # Better email regex
    emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html))

    if emails:
        print("Emails found:", ', '.join(sorted(emails)), flush=True)
    else:
        print("Emails: None found", flush=True)

except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching {url}: {e}", flush=True)
except Exception as e:
    print(f"❌ General error: {e}", flush=True)

