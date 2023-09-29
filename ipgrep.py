#!/usr/bin/env python3

import sys
import re
import ipaddress

def search_for_ips(file, network):

    def belongs_to_net(addr):
        try:
            net = ipaddress.ip_network(network)
            address = ipaddress.ip_address(addr)
            return address in net
        except: 
            return False

    def check_line(line):
        pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})") # simple extraction of 4 numbers separated by dots
        result = re.search(pattern, line)
        if result is not None:
            address = result.group()
            if belongs_to_net(address):
                return True
        return False
    
    if file is None:
        stream = sys.stdin
    else:
        stream = open(file, 'r')
    
    for line in stream:
        if (check_line(line)):
            print(line, end='')
    
    if stream is not sys.stdin:
        stream.close()
            

def main():
    argcount = len(sys.argv)
    if (argcount != 2 and argcount != 3):
        exit(1)
    if (argcount == 2):
        file = None
        network = sys.argv[1]
    else:
        file = sys.argv[1]
        network = sys.argv[2]
    search_for_ips(file, network)

if __name__ == '__main__':
    main()