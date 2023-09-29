#!/usr/bin/env python3

import sys
import re
import ipaddress

def belongs_to_net(addr, network):
    try:
        net = ipaddress.ip_network(network)
        address = ipaddress.ip_address(addr)
        return address in net
    except: 
        return False


def search_for_ips(file, network):
    pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})") # simple extraction of 4 numbers separated by dots
    with open(file, 'r') as source:
        for line in source:
            result = re.search(pattern, line)
            if result is not None:
                address = result.group()
                if belongs_to_net(address, network):
                    print(line, end='')

def main():
    file = sys.argv[1]
    network = sys.argv[2]
    search_for_ips(file, network)

if __name__ == '__main__':
    main()