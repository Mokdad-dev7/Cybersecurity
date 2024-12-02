import os

def create_folder_structure(base_dir):
    # Define folders and files
    folders = [
        "05-Resources",
        "06-Topics",
        "07-Exercises",
    ]

    files = {
        
        "05-Resources/Books.md": """
# Recommended Books

* **The Web Application Hacker's Handbook** by Dafydd Stuttard and Marcus Pinto
* **Hacking: The Art of Exploitation** by Jon Erickson 1 
* **Metasploit: The Penetration Testing Framework** by David Kennedy, Jim O'Gorman, and Devon Kearns
""",
        "05-Resources/Courses.md": """
# Online Courses

* **Cybersecurity Fundamentals** on Coursera
* **Ethical Hacking Specialization** on Coursera
* **Offensive Security Certified Professional (OSCP)**
""",
        "05-Resources/Tools.md": """
# Essential Tools

* **Kali Linux**
* **Wireshark**
* **Burp Suite**
* **Metasploit**
* **Nmap**
""",
        "06-Topics/Networking/Notes.md": """
# Networking Notes

* **TCP/IP Model**
* **OSI Model**
* **Network Protocols**
* ...
""",
        "06-Topics/Networking/Labs/NetworkAnalysis.md": """
# Network Analysis Lab

* **Objectives:**
  * Analyze network traffic using Wireshark
  * Identify common network attacks
* **Tasks:**
  * Capture network traffic
  * Filter and analyze packets
  * Identify suspicious activity
""",
        "06-Topics/Networking/Labs/NetworkSecurity.md": """
# Network Security Lab

* **Objectives:**
  * Configure network security devices (firewalls, IDS/IPS)
  * Perform vulnerability scanning
* **Tasks:**
  * Configure a firewall
  * Deploy an intrusion detection system
  * Scan for vulnerabilities
""",
        "06-Topics/Ethical-Hacking/Notes.md": """
# Ethical Hacking Notes

* **Reconnaissance**
* **Scanning**
* **Exploitation**
* **Post-Exploitation**
* **Reporting**
""",
        "06-Topics/Ethical-Hacking/Tools/WebAppPenetrationTesting.md": """
# Web Application Penetration Testing Tools

* **Burp Suite**
* **OWASP ZAP**
* **Nikto**
""",
        "06-Topics/Ethical-Hacking/Tools/SocialEngineering.md": """
# Social Engineering Techniques

* **Phishing**
* **Vishing**
* **Tailgating**
* **Pretexting**
""",
        "06-Topics/Cryptography/Notes.md": """
# Cryptography Notes

* **Symmetric Encryption**
* **Asymmetric Encryption**
* **Hash Functions**
* **Digital Signatures**
""",
        "06-Topics/Cryptography/Code/Encryption.py": """
# Python script for encryption and decryption
# ...
""",
        "06-Topics/Incident-Response/Playbooks.md": """
# Incident Response Playbooks

* **Incident Detection and Analysis**
* **Containment**
* **Eradication**
* **Recovery**
* **Lessons Learned**
""",
        "06-Topics/Incident-Response/Templates/IncidentReport.docx": """
# Incident Report Template

* **Incident Details**
* **Timeline**
* **Root Cause Analysis**
* **Lessons Learned**
""",
        "06-Topics/Penetration-Testing/Notes.md": """
# Penetration Testing Methodology

* **Planning**
* **Information Gathering**
* **Vulnerability Scanning**
* **Exploitation**
* **Post-Exploitation**
* **Reporting**
""",
        "06-Topics/Penetration-Testing/Reports/PenetrationTestReport.docx": """
# Penetration Test Report Template

* **Executive Summary**
* **Methodology**
* **Findings**
* **Recommendations**
""",
        "07-Exercises/CTF1.md": """
# CTF 1: Basic Networking

* **Challenges:**
  * Network Scanning
  * Port Scanning
  * Service Identification
""",
        "07-Exercises/CTF2.md": """
# CTF 2: Web Application Hacking

* **Challenges:**
  * SQL Injection
  * Cross-Site Scripting (XSS)
  * Cross-Site Request Forgery (CSRF)
"""
    }

    # Create folders
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

    # Create files, ensuring parent directories exist
    for file, content in files.items():
        file_path = os.path.join(base_dir, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the parent folder exists
        with open(file_path, "w") as f:
            f.write(content)
            print(f"Created file: {file_path}")

if __name__ == "__main__":
    # Set the base directory
    base_dir = "."  # Current directory

    # Create the folder structure
    create_folder_structure(base_dir)
