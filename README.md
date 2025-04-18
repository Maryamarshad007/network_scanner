# Network Security Scanner

A quick tool to scan for open ports and check firewall status on any device.

# What You'll Need
- Python 3 (already installed on most computers)
- Nmap scanning tool

# Get Ready
1. Install Nmap:
   - Windows: Download from [nmap.org](https://nmap.org/download.html) (just run the installer)
   - Mac/Linux: Open terminal and run:  
     bash
     sudo apt install nmap  # Linux
     brew install nmap     # Mac
    

2. Get the Scanner:
   - Download `network_scanner.py` from this project

# How to Run It
1. Open terminal/command prompt
2. Type:  
    bash
   python network_scanner.py
   (On Mac/Linux use sudo if needed: sudo python3 network_scanner.py)

When asked, type the IP address you want to scan (like 192.168.1.1)

What Happens Next
Scans for open ports and services Checks if firewall is on/off
Saves results to nmap_report.txt in the same folder

Example output:
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http


Firewall Status: Active
Important Notes
 Only scan devices you own or have permission to scan
 First scan may take 2-5 minutes
 On company/school networks, ask IT first

Troubleshooting
If you get errors:
Make sure Nmap is installed correctly
Try running as Administrator/sudo
Check Python is installed (python --version)

This version:
1 Flows naturally like human-written docs
2 Uses simple bullet points and spacing
3 Contains all needed info in one place
4 Has clear headings and action steps
5 Includes practical examples and warnings
