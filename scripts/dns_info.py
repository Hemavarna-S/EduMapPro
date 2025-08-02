#!/usr/bin/env python3
import sys
import dns.resolver

if len(sys.argv) < 2:
    print("Usage: python3 dns_lookup.py <domain>")
    sys.exit(1)

domain = sys.argv[1]

# Set resolver timeout to keep it real-time
resolver = dns.resolver.Resolver()
resolver.lifetime = 3.0  # total timeout
resolver.timeout = 2.0   # per try

for rtype in ["A", "MX", "NS", "TXT"]:
    try:
        answers = resolver.resolve(domain, rtype)
        print(f"{rtype}: {', '.join(r.to_text() for r in answers)}", flush=True)
    except dns.resolver.NoAnswer:
        print(f"{rtype}: No answer", flush=True)
    except dns.resolver.NXDOMAIN:
        print(f"{rtype}: Domain does not exist", flush=True)
    except dns.exception.Timeout:
        print(f"{rtype}: Query timed out", flush=True)
    except Exception as e:
        print(f"{rtype}: Error - {e}", flush=True)

