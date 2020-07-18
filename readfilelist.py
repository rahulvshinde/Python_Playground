def readfilelinebyline(fname):
    with open(fname) as f:
        content_list=f.readlines()
        print (content_list)
readfilelinebyline('sample.txt')