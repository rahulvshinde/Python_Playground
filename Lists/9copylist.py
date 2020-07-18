# 9. Write a Python program to clone or copy a list.

my_list = [1,2,3]

def copylist(my_list):
    new_list = []
    for item in my_list:
        new_list.append(item)
    return new_list

def copylist1(my_list):
    new_list = list(my_list)
    return new_list
print("Copied list {}".format(copylist(my_list)))
print("Copied list {}".format(copylist1(my_list)))