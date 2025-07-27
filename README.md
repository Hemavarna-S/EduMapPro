# 🎓 EduMapPro
> Advanced Indian `.edu.in` domain fingerprinting & information gathering toolkit  
> Hybrid: Nmap NSE script + Python GUI + multi-tool modules
> NOTE : ONLY FOR ETHICAL AND KNOWLEDGE BASED FOR SELF LEARNING ONLY!!

---

## ✨ Features

✅ Fingerprint server banner, CMS, JavaScript frameworks (WordPress, Moodle, React, Angular, etc.)  
✅ SSL/TLS certificate info (issuer, validity)  
✅ DNS records (A, MX, NS, TXT)  
✅ WHOIS lookup (registrar, organization, country, dates)  
✅ Email scraping from homepage  
✅ Clean & modern PyQt5 GUI (multi-tab, copy/save output)  
✅ Save scan results to text / JSON  
✅ Ethical & research use only

---

## 📂 Project Structure

```bash
EduMapPro/
├── gui/                   # PyQt5 GUI
│   └── gui.py
├── nse/                   # Nmap NSE script
│   └── fingerprint_edu_in.nse
├── scripts/               # Python info modules
│   ├── dns_info.py
│   ├── ssl_info.py
│   ├── whois_lookup.py
│   └── extract_emails.py
├── output/                # Results saved here
├── domains.txt            # Input list of domains
├── run_scan.sh           # Quick scan shell script
├── requirements.txt
└── README.md
