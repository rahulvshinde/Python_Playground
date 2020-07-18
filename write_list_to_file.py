def writelisttofile(fname):
    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    with open(fname, "w") as f:
        for c in color:
            f.write("%s\n" % c)
    content = open('sample.txt')
    print(content.read())


writelisttofile('sample.txt')
