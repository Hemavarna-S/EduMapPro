#!/bin/bash
mkdir -p output
echo "[*] Running EduMap Pro scan..."
nmap --script ./nse/fingerprint_edu_in.nse -p 80,443 -iL domains.txt -oN output/edu_scan_results.txt
echo "[*] Done! Results saved to output/edu_scan_results.txt"
