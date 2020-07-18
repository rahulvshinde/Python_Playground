from itertools import islice
def readFile(fname,n):
    with open(fname) as f:
        for line in islice(f,n):
            print line

readFile('sample.txt',2)


