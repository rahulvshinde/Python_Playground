from collections import Counter
def wordfrequency(fname):
    cnt=Counter()
    with open(fname, "r") as f:
        # words = Counter(f.read().split())
        words = f.read().split()
        for word in words:
            if word == "PHP":
                cnt[word] +=1
    print (cnt)
print(wordfrequency('sample.txt'))