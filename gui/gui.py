import sys
import subprocess
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QVBoxLayout,
                             QPushButton, QTextEdit, QLabel, QMessageBox, QFileDialog)
from PyQt5.QtGui import QFont

class EduMapProGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduMap Pro - Fingerprinting & Info Gathering")
        self.setGeometry(200, 200, 800, 600)
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.font = QFont("Courier", 10)

        # Tabs
        self.scan_tab = self.create_tab("Run Nmap scan", self.run_scan)
        self.whois_tab = self.create_tab("WHOIS Lookup", self.run_whois)
        self.dns_tab = self.create_tab("DNS Info", self.run_dns)
        self.ssl_tab = self.create_tab("SSL Info", self.run_ssl)
        self.emails_tab = self.create_tab("Extract Emails", self.run_emails)

        self.tabs.addTab(*self.scan_tab)
        self.tabs.addTab(*self.whois_tab)
        self.tabs.addTab(*self.dns_tab)
        self.tabs.addTab(*self.ssl_tab)
        self.tabs.addTab(*self.emails_tab)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def create_tab(self, label_text, callback):
        widget = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Enter .edu.in domains (one per line):")
        input_box = QTextEdit()
        input_box.setFont(self.font)
        output_area = QTextEdit()
        output_area.setFont(self.font)
        output_area.setReadOnly(True)
        btn = QPushButton(label_text)
        btn.clicked.connect(lambda: callback(input_box, output_area))
        layout.addWidget(label)
        layout.addWidget(input_box)
        layout.addWidget(btn)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(output_area)
        widget.setLayout(layout)
        return widget, label_text

    def run_script(self, script, domains, output_area):
        domains_text = domains.toPlainText().strip()
        if not domains_text:
            QMessageBox.warning(self, "Input Error", "Please enter at least one domain.")
            return
        for domain in domains_text.splitlines():
            try:
                result = subprocess.check_output([sys.executable, f"./scripts/{script}.py", domain],
                                                stderr=subprocess.STDOUT, universal_newlines=True)
                output_area.append(f"\n[+] {domain}:\n{result}")
            except subprocess.CalledProcessError as e:
                output_area.append(f"❌ Error for {domain}: {e.output}")

    def run_scan(self, domains, output_area):
        domains_text = domains.toPlainText().strip()
        if not domains_text:
            QMessageBox.warning(self, "Input Error", "Enter domains.")
            return
        with open("domains.txt", "w") as f: f.write(domains_text)
        output_area.append("[*] Running Nmap scan...")
        try:
            result = subprocess.check_output(
                ["nmap", "--script", "./nse/fingerprint_edu_in.nse", "-p", "80,443", "-iL", "domains.txt"],
                stderr=subprocess.STDOUT, universal_newlines=True)
            with open("output/edu_scan_results.txt", "w") as out:
                out.write(result)
            output_area.append(result)
            output_area.append("\n✅ Scan complete! Results saved to output/edu_scan_results.txt\n")
        except subprocess.CalledProcessError as e:
            output_area.append(f"❌ Error running scan:\n{e.output}")

    def run_whois(self, domains, output_area): self.run_script("whois_lookup", domains, output_area)
    def run_dns(self, domains, output_area): self.run_script("dns_info", domains, output_area)
    def run_ssl(self, domains, output_area): self.run_script("ssl_info", domains, output_area)
    def run_emails(self, domains, output_area): self.run_script("extract_emails", domains, output_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = EduMapProGUI()
    gui.show()
    sys.exit(app.exec_())
