"""
offending IP addresses during the DDoS attack
Log File:
192.168.0.1 — — [23/Apr/2017:05:54:36 -0400] “GET / HTTP/1.1” 403 3985 “-” “Mozilla/5.0 (Windows NT 10.0; WOW64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36”
"""

import re
from collections import Counter


def log_parser(lfile):
    myreg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(lfile, 'r') as file:
        log = file.read()
        ips = re.findall(myreg, log)
        ipcount = Counter(ips)
        for item, value in ipcount.items():
            print("IP Addr: {} ----> Count: {}".format(item, value))
log_parser("access.log")