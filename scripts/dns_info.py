#!/usr/bin/env python3
import sys, dns.resolver
domain = sys.argv[1]
for rtype in ["A","MX","NS","TXT"]:
    try:
        answers = dns.resolver.resolve(domain, rtype)
        print(f"{rtype}:", ', '.join([r.to_text() for r in answers]))
    except: print(f"{rtype}: Not found")
