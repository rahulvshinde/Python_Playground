from itertools import islice
def appendfile(fname):
    with open(fname, "w") as f:
        f.write("Appending text to the end")
    txt = open(fname)
    print txt.read()
appendfile('sample.txt')
