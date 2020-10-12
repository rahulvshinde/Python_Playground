s = "3+2*2"
def calculate(s):
    mystr = []
    signs = ['+', '-', '*', '/']
    res = 0
    for st in s:
        mystr.append(st)
    for i, myst in enumerate(mystr):
        if myst not in signs:
            pass
        else:
            if myst == signs[3]:
                res = mystr[i - 1] // mystr[i + 1]
            elif myst == signs[2]:
                res = mystr[i - 1] * mystr[i + 1]
            elif myst == signs[1]:
                res = mystr[i - 1] - mystr[i + 1]
            elif myst == signs[0]:
                res = mystr[i - 1] + mystr[i + 1]

print(calculate(s))