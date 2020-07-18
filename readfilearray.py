def readfile(fname):
    data = []
    with open(fname, "r") as f:
        for line in f:
            data.append(line)
        print data
readfile('sample.txt')