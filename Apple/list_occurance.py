inp = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

freq = {}
for item in inp:
    if item in freq:
        freq[item] +=1
    else:
        freq[item] = 1
for key, value in freq.items():
    print("{}: {}".format(key, value))
