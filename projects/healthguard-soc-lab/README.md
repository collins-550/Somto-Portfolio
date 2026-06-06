# HealthGuard Medical Centre — SOC Investigation

## Overview
A full SOC investigation of a simulated hospital data breach
using Splunk SIEM, Nessus vulnerability scanning, and Python
log analysis.

## Tools Used
- Splunk Enterprise 10.2.3
- Docker & Docker Compose
- Python 3 (custom vulnerability scoring script)
- Kali Linux

## Key Findings
- Attacker IP: 197.210.84.23
- Attack method: Brute force → Lateral movement → Data exfiltration
- Data stolen: ~3.25MB patient records via hastebin.pw
- Total vulnerabilities found: 73

## Files
- HealthGuard_Full_SOC_Report.pdf — Full investigation report
- phase1_python_project.zip — Python vulnerability scoring script

## Skills Demonstrated
- SIEM log analysis (Splunk SPL)
- Threat hunting and incident response
- Vulnerability assessment
- Docker containerization
- Python scripting
