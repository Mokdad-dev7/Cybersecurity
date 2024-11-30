# Assignments Guide for Cybersecurity Road-map  

This document provides detailed assignments for practical learning, based on cybersecurity fundamentals and specializations.

---

## **Phase 1: Foundational Knowledge**  

### **1. Networking Basics**  
**Assignment**: Create a diagram explaining the OSI model and compare it to the TCP/IP model.  
- **Steps**:  
  1. Research both models and their layers.  
  2. Create a table or diagram showing equivalencies (e.g., OSI's "Application" maps to TCP/IP's "Application").  
  3. Include protocols like HTTP, DNS, TCP, UDP, and IP with real-world examples.  

### **2. Linux Fundamentals**  
**Assignment**: Master 20 essential Linux commands.  [Labex](https://labex.io) 
- **Steps**:  
  1. Set up a Linux virtual machine (e.g., Kali or Ubuntu).  
  2. Practice commands: `ls`, `cd`, `chmod`, `grep`, `awk`, etc.  
  3. Create a cheat sheet explaining their usage.
    

---

## **Phase 2: Core Cybersecurity Skills**  

### **3. Packet Analysis with Wireshark**   [Labex](https://labex.io)
**Assignment**: Analyze captured packets for a simulated attack.  
- **Steps**:  
  1. Use Wireshark to capture traffic while accessing a local HTTP server.  
  2. Filter for suspicious activity, such as unusual protocols or high traffic volume.  
  3. Document findings with screenshots and explanations.  

### **4. Cryptography Basics**  
**Assignment**: Encrypt and decrypt a file using OpenSSL.  
- **Steps**:  
  1. Research symmetric and asymmetric encryption.  
  2. Use OpenSSL to encrypt a file with AES:  
     ```bash
     openssl enc -aes-256-cbc -in plaintext.txt -out encrypted.txt  
     ```  
  3. Write a short summary explaining the importance of encryption.  

---

## **Phase 3: Specialized Skills Development**  

### **5. Vulnerability Scanning with Nmap**  
**Assignment**: Perform a comprehensive scan of a virtual network.  
- **Steps**:  
  1. Create a local network using virtual machines.  
  2. Run advanced Nmap commands, such as:  
     ```bash
     nmap -A -p- 192.168.1.0/24  
     ```  
  3. Analyze results for open ports and vulnerabilities.  

### **6. Web Application Security**  
**Assignment**: Exploit a simulated SQL injection vulnerability.  
- **Steps**:  
  1. Set up the Damn Vulnerable Web App (DVWA).  
  2. Perform SQL injection using payloads like:  
```sql
	 ' OR '1'='1'; --  
```  
  1. Document the vulnerability and propose mitigation strategies.

---

## **Phase 4: Practical and Advanced Skills**  

### **7. Incident Response Simulation**  
**Assignment**: Draft an incident response plan for a simulated attack.  
- **Steps**:  
  1. Research the key phases: Identification, Containment, Eradication, Recovery, and Lessons Learned.  
  2. Create a scenario involving a ransomware attack.  
  3. Draft a plan, including roles and tools (e.g., SIEMs).  

### **8. Threat Hunting with Splunk**  
**Assignment**: Detect a brute-force login attack using logs.  
- **Steps**:  
  1. Install Splunk Free and ingest a sample log dataset.  
  2. Set up a query to detect multiple failed login attempts from the same IP:  

     ```sql
     index=security sourcetype="auth" action="failed" | stats count by src_ip  
     ```  
  3. Document findings and mitigation steps.  

---

## **Phase 5: Real-World Application**  

### **9. Capture-The-Flag Challenges**  
**Assignment**: Solve beginner CTF challenges on TryHackMe.  
- **Steps**:  
  1. Start with “Introduction to Pentesting” or “Linux Fundamentals”.  
  2. Take notes on each challenge, including tools used and techniques learned.  
  3. Share solutions and insights in your portfolio.  

### **10. Malware Analysis**  
**Assignment**: Reverse engineer a harmless malware sample.  
- **Steps**:  
  1. Use tools like Ghidra or IDA Free.  
  2. Focus on identifying key functionalities (e.g., file modifications or persistence).  
  3. Write a report detailing your analysis and findings.  

---

## **Additional Resources**  
- [roadmap.sh Cybersecurity Roadmap](https://roadmap.sh/cyber-security)  
- [TryHackMe Learning Platform](https://tryhackme.com)  
- [Open Web Application Security Project (OWASP)](https://owasp.org)
- [Labex](https://labex.io)
- Books: "The Web Application Hacker's Handbook" and "Practical Malware Analysis."  

---

Progressively update your portfolio with completed assignments and milestones!
