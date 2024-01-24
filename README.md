# ipgrep

A simple tool for searching IPs belonging to specified network in text.

Usage:

```
python3 ipgrep.py [-h] [-l | -e | -r [IP_RANGE ...]] [-f FILE]

options:
  -h, --help            show this help message and exit
  -l, --local           search for IPs in internal networks
  -e, --external        search for IPs in external networks
  -r [IP_RANGE ...], --range [IP_RANGE ...]
                        IP address ranges in CIDR format
  -f FILE, --file FILE
```

Networks must be specified using CIDR notation.