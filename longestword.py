def longestword(fname):
    with open(fname, "r") as f:
        words = f.read().split()
    max_len = len(max(words, key=len))
    word: str
    for word in words:
        if len(word) == max_len:
            print (word)
longestword('sample.txt')