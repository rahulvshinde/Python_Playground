def readfile(fname):
    with open(fname, "r") as f:
        data = f.readlines()
        print data
readfile('sample.txt')