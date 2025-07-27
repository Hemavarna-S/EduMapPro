#!/usr/bin/env python3
import sys, whois
domain = sys.argv[1]
info = whois.whois(domain)
print(f"Domain: {domain}\nRegistrar: {info.registrar}\nOrg: {info.org}\nCountry: {info.country}\nCreated: {info.creation_date}\nExpires: {info.expiration_date}")
