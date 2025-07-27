#!/usr/bin/env python3
import sys, ssl, socket
domain = sys.argv[1]
ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
    s.settimeout(5)
    s.connect((domain, 443))
    cert = s.getpeercert()
    print(f"Subject: {cert.get('subject')}\nIssuer: {cert.get('issuer')}\nValid From: {cert.get('notBefore')}\nValid To: {cert.get('notAfter')}")
