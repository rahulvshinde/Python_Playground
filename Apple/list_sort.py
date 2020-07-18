from collections import Counter
numlist = [1,2,3,8,4,9,0,5]

#method 1
numlist.sort(reverse=True)
print(numlist)

#method 2
for i in range(len(numlist)):
    for j in range(i+1,len(numlist)):
        if numlist[i]>numlist[j]:
            numlist[i],numlist[j] = numlist[j],numlist[i]

print(Counter(numlist))
