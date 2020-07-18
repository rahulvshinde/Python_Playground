list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 7, 8, 10, 8, 2]


def findcommon(list1, list2):
    return list(set(list1) & set(list2))


def findcommon1(list1, list2):
    new_list = []
    for item in list1:
        if item in list2:
            new_list.append(item)
    return new_list


def findcommon2(list1, list2):
    return list(set(list1).intersection(list2))


# print("{l1} and {l2} has these common items: {dup}".format(l1=list1, l2=list2, dup=findcommon(list1, list2)))
# print("{l1} and {l2} has these common items: {dup}".format(l1=list1, l2=list2, dup=findcommon1(list1, list2)))
# print("{l1} and {l2} has these common items: {dup}".format(l1=list1, l2=list2, dup=findcommon2(list1, list2)))
#######################################################################################################################

"""
12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

new_list = []
new_list1 = []


def removeelement(my_list):
    for i in range(len(my_list)):
        if i not in (0, 4, 5):
            new_list.append(my_list[i])
    return new_list


def removeelement1(my_list):
    new_list1 = [my_list[item] for item in range(len(my_list)) if item not in (0, 4, 5)]
    return new_list1


# print(removeelement(my_list))
# print(removeelement1(my_list))


#######################################################################################################################

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

def print3darray():
    my_array = [[['*' for col in range(6)] for col in range(4)] for col in range(3)]
    return my_array


# print(print3darray())
#######################################################################################################################

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []


def oddlist(my_list):
    new_list = [my_list[item] for item in range(len(my_list)) if not item % 2]
    return new_list


# print(oddlist(my_list))

#######################################################################################################################

# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of
# numbers between 1 and 30 (both included).

def squarelist():
    my_list3 = []
    for i in range(1, 31):
        if i <= 5 or i > 25:
            my_list3.append(i ** 2)
    return my_list3


# print(squarelist())
#######################################################################################################################

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square
# of numbers between 1 and 30 (both included).

def squarelist1():
    my_list4 = []
    for i in range(6,31):
        my_list4.append(i**2)
    return my_list4
print(squarelist1())
















