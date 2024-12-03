
# Lab 1: Basic Networking

* **Challenges:**
  * Network Scanning
  * Port Scanning
  * Service Identification
* **Nmap Basic TCP Scan**
  * TCP Connect Scan IS !
    A TCP Connect Scan is a network scanning technique used to determine the open ports on a target system. It is one of the most straitforward methods for port scanning and is often employed by security professianals and network administrators to assess the security posture of systems.
    Key Details

1. **Purpose**:
    
    - The primary goal of a TCP Connect Scan is to identify which ports on a target machine are open and accepting connections. This information can help in vulnerability assessment and penetration testing.
2. **How It Works**:
    
    - A TCP Connect Scan works by attempting to establish a full TCP connection with each port on the target system.
    - The process involves sending a SYN (synchronize) packet to the target port:
        - If the port is open, the target responds with a SYN-ACK (synchronize-acknowledge) packet, indicating that it is ready to establish a connection.
        - The scanner then sends an ACK (acknowledge) packet back to complete the three-way handshake, establishing a full connection.
        - If the port is closed, the target responds with an RST (reset) packet.
3. **Advantages**:
    
    - **Simplicity**: It uses standard TCP/IP protocols, making it easy to implement.
    - **Reliability**: Since it establishes full connections, it provides accurate results regarding open ports.
4. **Disadvantages**:
    
    - **Detection**: Because it completes the TCP handshake, this method can be easily detected by intrusion detection systems (IDS) or firewalls.
    - **Resource Intensive**: Establishing full connections can consume more resources compared to other scanning techniques like SYN scans.
5. **Use Cases**:
    
    - Network administrators use TCP Connect Scans for inventorying services running on their networks.
    - Security professionals may use this scan as part of penetration testing efforts to identify potential attack vectors.

### Example Command

In tools like Nmap, you can perform a TCP Connect Scan using:

```bash
nmap -sT <target_ip>
```

Here, `-sT` specifies that Nmap should perform a TCP Connect Scan against `<target_ip>`.

### Conclusion

A TCP Connect Scan is an effective method for discovering open ports on devices within a network but comes with trade-offs in terms of stealthiness and resource usage. Understanding its mechanics helps in both defensive security practices and offensive security assessments.
