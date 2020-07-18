import os
def filesize(fname):
    statinfo = os.stat(fname)
    print (statinfo.st_size)
filesize('sample.txt')
