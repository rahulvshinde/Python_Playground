"""Suppose under this directory /web there are 50,000 - html files

List all the files which has phone numbers with below pattern
(xxx)-xxx-xxxx
xxx-xxx-xxxx"""

import re
def findPhoneNumber(fname):
    phonepattern =re.compile(r'''
    \(?     # The particular regex might optionally start with a (
    (\d{3})   # Followed by the area code
    \)?     # Followed optionally by a parenthesis
    -       # Followed by a hyphen
    (\d{3}) # Followed by three digits 
    -       # And a hyphe
    (\d{4}) # And last 4 digits
    ''', re.VERBOSE)
    phonepattern1 = re.compile(r'\(?(\d{3})\)?-(\d{3})-(\d{4})')
    with open(fname, "r") as file:
        f = file.read()
        return phonepattern1.findall(f)

print(findPhoneNumber("test.txt"))
