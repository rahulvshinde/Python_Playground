from functools import reduce

l=[[1,2,3],[4,5,6]]
print (l)
flat_list=[]
for items in l:
    for item in items:
        flat_list.append(item)

print (flat_list)

flatten = reduce(lambda x,y:x+y, l)
print(flatten)