#!/usr/bin/env python3
import sys, re, requests
domain = sys.argv[1]
try:
    html = requests.get(f"http://{domain}", timeout=5).text
    emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+", html))
    print("Emails:", ', '.join(emails) if emails else "None found")
except Exception as e:
    print(f"Error: {e}")
