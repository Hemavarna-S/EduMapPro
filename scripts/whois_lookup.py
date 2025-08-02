#!/usr/bin/env python3
import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python3 whois_lookup.py <domain>")
    sys.exit(1)

domain = sys.argv[1]

try:
    # Always fetch live, real-time WHOIS data
    result = subprocess.check_output(["whois", domain], text=True, timeout=10)
    print(result, flush=True)
except subprocess.TimeoutExpired:
    print(f"WHOIS query for {domain} timed out.", flush=True)
except Exception as e:
    print(f"Error running whois for {domain}: {e}", flush=True)
