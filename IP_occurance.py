import re
from collections import Counter

cnt = Counter()
ipre = re.compile(r'^(?P<ip>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) - -')
with open(infilename) as infile:
    for line in infile:
            m = ipre.match(line)
            if m is not None:
                ip = m.groupdict()['ip']
                cnt[ip] += 1
    print(ip)