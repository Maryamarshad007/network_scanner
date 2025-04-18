import os
import platform
import subprocess

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def scan_with_nmap(ip):
    print(f"\n[??] Running Nmap scan on {ip}...\n")
    result = subprocess.getoutput(f"nmap -sV --script=vuln {ip}")
    print(result)
    with open("nmap_report.txt", "w") as file:
        file.write(result)
    print("\n[?] Report saved to nmap_report.txt")

def check_firewall_status():
    print("\n[???] Checking Firewall status...\n")
    if platform.system() == "Windows":
        result = subprocess.getoutput("netsh advfirewall show allprofiles")
    elif platform.system() == "Linux":
        result = subprocess.getoutput("sudo ufw status")
    else:
        result = "Firewall check not supported on this OS."
    print(result)

def main():
    clear_screen()
    print("?? NETWORK VULNERABILITY SCANNER & FIREWALL ANALYZER ??")
    target_ip = input("\nEnter target IP address (e.g. 192.168.1.1): ")

    scan_with_nmap(target_ip)
    check_firewall_status()

if __name__ == "__main__":
    main()
