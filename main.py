#import shi
import socket
import requests
import dns.resolver

#banner
def banner():
    print("NVS - Network Vulnerability Scanner")

#defined stuff
def scan_open_ports(host):
    print(f"Scanning ports on {host}...")
    open_ports = []
    for port in range(1, 1025):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((host, port)) == 0:
                    open_ports.append(port)
        except Exception:
            pass
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports.")

#more defined stuff
def check_http_headers(url):
    print(f"Checking headers for {url}...")
    try:
        response = requests.get(url)
        headers = response.headers
        for header, value in headers.items():
            print(f"{header}: {value}")
        if 'X-Frame-Options' not in headers:
            print("X-Frame-Options missing.")
        if 'X-Content-Type-Options' not in headers:
            print("X-Content-Type-Options missing.")
    except Exception as e:
        print("Couldn't fetch headers.")

#check dns
def check_dns(target):
    print(f"Resolving DNS for {target}...")
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']
        answer = resolver.resolve(target)
        for ip in answer:
            print(f"IP: {ip}")
    except Exception:
        print("DNS resolution failed.")
#startup
def main():
    banner()
    target = input("Target domain/IP: ")
    choice = input("Choose scan type (1: Ports, 2: Headers, 3: DNS): ")
#choices
    if choice == '1':
        scan_open_ports(target)
    elif choice == '2':
        url = target if target.startswith("http") else f"http://{target}"
        check_http_headers(url)
    elif choice == '3':
        check_dns(target)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
