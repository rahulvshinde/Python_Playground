from functools import reduce
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flatten1 = []
flatten = [item for items in l for item in items]
for items in l:
    for item in items:
        flatten1.append(item)
flatten2 = reduce((lambda x,y: x+y),l)
print(flatten, flatten1, flatten2)
