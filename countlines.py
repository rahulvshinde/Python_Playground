def countlines(fname):
    cnt=0
    with open(fname) as f:
        for line in f:
            cnt +=1
        print (cnt)
countlines('sample.txt')
