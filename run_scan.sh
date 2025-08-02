#!/bin/bash

mkdir -p output
echo "[*] Starting EduMap Pro scan..."

if [[ ! -s domains.txt ]]; then
  echo "❌ Error: domains.txt not found or is empty."
  exit 1
fi

nmap --script ./nse/fingerprint_edu_in.nse -p 80,443 -iL domains.txt -oN output/edu_scan_results.txt

if [[ $? -eq 0 ]]; then
  echo "✅ Done! Results saved to output/edu_scan_results.txt"
else
  echo "❌ Scan failed. Check your script or Nmap installation."
fi

