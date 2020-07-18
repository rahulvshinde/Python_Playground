# 18. Write a Python program to generate all permutations of a list in Python.

from itertools import permutations

my_list = [1, 2, 3]


def mypermutaions():
    perm = permutations(my_list)
    for item in perm:
        print(list(item))


# print(mypermutaions())
#######################################################################################################################

# 19. Write a Python program to get the difference between the two lists.
my_list1 = [2, 3, 4]
my_list2 = [3, 4, 5]
my_list3 = []
my_list4 = []
for item in my_list1:
    if item not in my_list2:
        my_list3.append(item)
# print(my_list3)


my_list4 = list(set(my_list1) - set(my_list2))
# print(my_list4)

my_list4 = [i for i in my_list1 + my_list2 if i not in my_list1 or i not in my_list2]
# print(my_list4)

#######################################################################################################################

# 20. Write a Python program access the index of a list.
my_list = [1, 2, 3, 4, 53, 546, 2323, 55, -1, 32]

# for i in range(len(my_list)):
#     print("Index: {} and Value: {}".format(i,my_list[i]))

#######################################################################################################################
# 21. Write a Python program to convert a list of characters into a string.

my_list = [1, 2, 3]
mystr = ""
mystr1 = ""
for i in my_list:
    mystr += str(i)
print(mystr1.join(str(my_list)))
print(mystr)

#######################################################################################################################
# 22. Write a Python program to find the index of an item in a specified list.
my_list = [1, 2, 3, 4, 53, 546, 2323, 55, -1, 32]
x = 4
i = 0
for item in my_list:
    if item is not x:
        i += 1
    else:
        print("Index: {}".format(i))
print(my_list.index(4))
