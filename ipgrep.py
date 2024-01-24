#!/usr/bin/env python3

import sys
import re
import ipaddress
import argparse

def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='python3 ipgrep.py',
        description='tool for searching IP ranges in text files'
    )
    net_group = parser.add_mutually_exclusive_group()
    net_group.add_argument(
        "-l", 
        "--local",
        action="store_true",
        help="search for IPs in internal networks"
    )
    net_group.add_argument(
        "-e", 
        "--external",
        action="store_true",
        help="search for IPs in external networks"
    )
    net_group.add_argument(
        "-r",
        "--range",
        nargs="*",
        metavar="IP_RANGE",
        help="IP address ranges in CIDR format"
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="FILE"
    )
    return parser

def search_for_ips(file, networks, reverse=False):

    def belongs_to_net(addr):
        found = False
        for network in networks:
            try:
                net = ipaddress.ip_network(network)
                address = ipaddress.ip_address(addr)
                if address in net:
                    found = True
            except ValueError:
                return False
        return found ^ reverse
            
    def check_line(line):
        pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})") # simple extraction of 4 numbers separated by dots
        result = re.search(pattern, line)
        if result is not None:
            address = result.group()
            if belongs_to_net(address):
                return True
        return False
    
    stream = open(file, 'r')
    
    for line in stream:
        if (check_line(line)):
            print(line, end='')
    
    if stream is not sys.stdin:
        stream.close()    

def search_for_local_or_external_ips(file, flag):
    networks = ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"]
    search_for_ips(file, networks, flag)

def main():
    parser = init_parser()
    
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    if args.local:
        search_for_local_or_external_ips(args.file, False)
    elif args.external:
        search_for_local_or_external_ips(args.file, True)
    elif args.range is not None:
        search_for_ips(args.file, args.range)

if __name__ == '__main__':
    main()