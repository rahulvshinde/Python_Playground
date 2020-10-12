import re
ip = []
with open("sample.txt", "r") as f:
    for text in f.readlines():
        print(text)
        ip.append(re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$', text))
print(ip)
