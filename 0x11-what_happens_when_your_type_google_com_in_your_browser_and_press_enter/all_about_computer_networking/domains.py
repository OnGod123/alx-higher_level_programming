#!/usr/bin/env python3
import socket

def resolve_dns(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"The IP address of {domain_name} is: {ip_address}")
    except socket.gaierror as e:
        print(f"Failed to resolve DNS for {domain_name}: {e}")

# Example usage
resolve_dns("google.com")

